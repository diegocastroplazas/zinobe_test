import pymongo
import sqlite3

class Persister(object):
    def __init__(self, data):
        self.data_to_persist = data
        self.mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.toMongo()
        self.toJson()
        self.toSqlLite()

    def toJson(self):
        self.data_to_persist.to_json(r'data.json')
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