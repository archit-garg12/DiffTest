import json
import pymongo
import inspect
import datetime


class MongoCollection(pymongo.collection.Collection):
    # override methods
    def insert_one(self, document, bypass_document_validation=False, session=None):
        document['_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        super(MongoCollection, self).insert_one(document)



# class MongoDatabase(pymongo.database.Database):
#     # override methods
#     def __getitem__(self, item):
#         return MongoCollection(self, item)


def set_collection(database_name, collection_name):
    return MongoCollection(database_name, collection_name)
#
pymongo.database.Database.__getitem__ = set_collection
# pymongo.collection.Collection = MongoCollection
x = pymongo.MongoClient('localhost')['cucm_proxy_db']
y = MongoCollection(x, 'listHuntList')
y.insert_one({'sup': 'sup2'})
for val in y.find():
    print(val)
# print(inspect.signature(MongoCollection.__init__))
# print(MongoCollection.__init__)
# print(type(x))
# print(type(x).__dict__['__getitem__'])

# class MongoData:
#     """
#     Class for representing Mongo Data
#     Attributes:
#         method (string): String for method name
#         timestamp (string): String to represent current timestamp
#         cucm_id (string): String to represent cucm ip address
#     """
#
#     def __init__(self, method, timestamp, cucm_id):
#         """
#         Constructor for Mongo Data
#
#         :param method: String for method name
#         :param timestamp: String to represent current timestamp
#         :param cucm_id: String to represent cucm ip address
#         """
#
#         self._method = method
#         self._timestamp = timestamp
#         self._data_list = mongo_integration.return_objects_by_query(method, current_time=timestamp, cucm_id=cucm_id)
#
#     def __len__(self):
#         """
#         Len Dunder Method to return length of mongo objects
#
#         :return (int): Length of data list returned by the constructor input
#         """
#
#         return len(self._data_list)
#
#     def timestamp(self):
#         return self._timestamp
#
#     def method(self):
#         return self._method
#
#     def data_list(self):
#         return self._data_list


