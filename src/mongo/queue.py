from mongo.connection import MongoDatabase

class AnalyticsQueue(MongoDatabase):
    def collection(self):
        return self.database["AnalyticsQueue"]

    def get(self):
        return self.collection().find_one({})

    def remove(self, symbol, work_name):
        self.collection().delete_one({"symbol": symbol, "workName": work_name})
