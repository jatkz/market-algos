import os
from pymongo import MongoClient, database

class MongoDatabase:
    def __init__(self):
        mongo_conn_string = os.environ.get('MONGO_CONNECTION')
        if mongo_conn_string == "" or mongo_conn_string is None:
            raise Exception("mongo connection env variable not set.")
        database_name = os.environ.get('DB_NAME')
        if database_name == "" or database_name is None:
            raise Exception("database name env variable not set.")

        client = MongoClient(mongo_conn_string)
        self.database = client[database_name]

