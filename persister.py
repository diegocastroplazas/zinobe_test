import pymongo

class Persister(object):
    def __init__(self, data):
        self.data_to_persist = data
        self.mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.toMongo()

    def toJson(self):
        pass

    def toSqlLite(self):
        pass

    def toMongo(self):
        db = self.mongo_client["zinobedb"]
        country_collection = db["countries"]
        '''
        for country_data in self.data_to_persist.iterrows():
            country_collection.insert_one(country_data.to_dict('dict'))
        '''
        x = country_collection.insert_many(self.data_to_persist.to_dict('records'))
        print(x.inserted_ids)