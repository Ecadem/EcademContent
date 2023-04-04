import pandas as pd
import json
from time import sleep

from .settings import (
    get_connection,
)

from .querys.querys import (
    SELECT_TAGS,
)


def get_response( query, cols, conn, recent = None ):
    n_trys = 0
    
    while n_trys < 4:
        try:
            conn.query(query)
            results = conn.store_result()
            items = results.fetch_row(maxrows=0)
            if recent:
                
                df = pd.DataFrame(items, columns = cols).head(3)
            else:
                df = df = pd.DataFrame(items, columns = cols)

            return json.loads(df.to_json(orient="records")), conn
        except:

            print("Entro a error")
            conn = get_connection()
            n_trys += 1
            sleep(2)
            continue


def add_tags( data, conn ):
    
    columns = [
        "ID",
        "name",
        "class",
        "style",
    ]

    tags, conn =  get_response( SELECT_TAGS, 
                          columns, 
                          conn, 
                          recent = False 
                        )    

    for data_point in data:
        tags_list = []
        tags_needed = data_point["tags"].split(",")

        for tag in tags:
            if tag["ID"] in tags_needed:
                tags_list.append(tag)
        
        data_point["tags"] = tags_list

    return data,  conn