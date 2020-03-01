import pymongo
import os
import sqlite3

class Persister(object):
    def __init__(self, data):
        self.data_to_persist = data
        if "MONGO_DB_DKR" in os.environ.keys():
            mongo_url = os.environ["MONGO_DB_DKR"]
        else:
            mongo_url = "mongodb://localhost:27017/"
        self.mongo_client = pymongo.MongoClient(mongo_url)
        self.toMongo()
        self.toJson()
        self.toSqlLite()

    def toJson(self):
        self.data_to_persist.to_json(r'/usr/src/results/data.json')
        print("Data has been saved to data.json file")

    def toSqlLite(self):
        conn = sqlite3.connect(':memory:')
        self.data_to_persist.to_sql(name='countries', con=conn)
        print("Data saved to SQLite")

    def toMongo(self):
        db = self.mongo_client["zinobedb"]
        country_collection = db["countries"]
        x = country_collection.insert_many(self.data_to_persist.to_dict('records'))
        print(x.inserted_ids)