# Convert bson to json

import bson

DIRECTORY = '/Users/krishnatejaavvari/PycharmProjects/DiffTest/mongo/datalayer/dump/cucm_proxy_db/'


def read_bson_data(collection_name):
    bson_file = DIRECTORY + collection_name + '.bson'
    with open(bson_file, 'rb') as f:
        data = bson.decode_all(f.read())
        return {document['_id'] : document for document in data}


print(read_bson_data('listHuntList'))


# x = read_bson_data('/Users/krishnatejaavvari/PycharmProjects/DiffTest/mongo/datalayer/dump/cucm_proxy_db/listHuntList.bson')
# print(x)
# print(len(x))


# import datetime
#
#
# class MongoCollection(pymongo.collection.Collection):
#     # override methods
#     def insert_one(self, document, bypass_document_validation=False, session=None):
#         document['_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         super(MongoCollection, self).insert_one(document)
#
#
# class MongoDatabase(pymongo.database.Database):
#     def __getitem__(self, item):
#         return MongoCollection(self, item)
#
#
# class MongoClient(pymongo.MongoClient):
#     def __getitem__(self, item):
#         return MongoDatabase(self, item)
#
#
# if __name__ == '__main__':
#     pymongo.MongoClient = MongoClient
