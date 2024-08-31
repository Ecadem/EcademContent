import json
from datetime import datetime

from src.db.mongodb import DatabaseObj

db = DatabaseObj()

def get_response(collection: str, recent: bool = None, n_firsts: int = 3) -> list:
    data = db.get_collection(collection)
    
    if data[0].get("last_update"):
        data = sorted(data, key = lambda x: datetime.strptime(x["last_update"], "%d-%m-%Y"))
    
    if recent:
        return data[:n_firsts]
    
    return data

def add_tags(data: list) -> list:
    tags = sorted(get_response("tags"), key = lambda x: x["tag_id"])
    
    for proj in data:    
        pj_tags = proj["tags"]

        for i, tag in enumerate(pj_tags):
            pj_tags[i] = tags[tag - 1]

    return data








        
            


#     columns = [
#         "ID",
#         "name",
#         "class",
#         "style",
#     ]

#     tags, conn =  get_response( SELECT_TAGS, 
#                           columns, 
#                           conn, 
#                           recent = False 
#                         )    

#     for data_point in data:
#         tags_list = []
#         tags_needed = data_point["tags"].split(",")

#         for tag in tags:
#             if tag["ID"] in tags_needed:
#                 tags_list.append(tag)
        
#         data_point["tags"] = tags_list

#     return data,  conn