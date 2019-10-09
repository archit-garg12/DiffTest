import datetime
import pymongo

class MongoCollection(pymongo.collection.Collection):
    # override methods
    def insert_one(self, document, bypass_document_validation=False, session=None):
        document['_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        super(MongoCollection, self).insert_one(document)


class MongoDatabase(pymongo.database.Database):
    def __getitem__(self, item):
        return MongoCollection(self, item)


class MongoClient(pymongo.MongoClient):
    def __getitem__(self, item):
        return MongoDatabase(self, item)


if __name__ == '__main__':
    pymongo.MongoClient = MongoClient
