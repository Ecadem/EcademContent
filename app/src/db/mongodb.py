from pymongo import MongoClient

from src.settings import (
    MONGO_URI,
    DATABASE,
)

client = MongoClient(MONGO_URI)

class DatabaseObj():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('Creating database instance')
            cls._instance = super(DatabaseObj, cls).__new__(cls)
                
        print('Return existing instance')
        return cls._instance

    def __init__(self) -> None:
        self.client = MongoClient(MONGO_URI)
        self.database = self.client.get_database(DATABASE)
    
    def get_collection(self, collection, filter = {}, as_list = True) -> list:
        data = self.database.get_collection(collection)
        
        if not as_list:
            return data
        
        return list(data.find(filter, { "_id": 0 }))

    def close_conn(self) -> None:
        self.client.close()
        
        


        





