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
            if recent and "last_update" in cols:
                
                df = pd.DataFrame(items, columns = cols)
                df["last_update"] = df["last_update"].str.decode("utf-8")
                df["last_update"] = pd.to_datetime(df["last_update"], dayfirst=True)
                df = df.sort_values(by="last_update", ascending=False).head(3)
                df["last_update"] = df["last_update"].dt.strftime("%d-%b-%Y")
                # df["last_update"] = df["last_update"].str.encode("utf-8")
            elif recent and "last_update" not in cols:
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