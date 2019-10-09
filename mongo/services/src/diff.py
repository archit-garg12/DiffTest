from mongo_extract import pull_data_by_collection
from bson_extract import read_bson_data


class MongoData():
    def __init__(self, collection_name, type='mongo'):
        if type == 'mongo':
            self._data = pull_data_by_collection(collection_name)
        elif type == 'bson':
            self._data = read_bson_data(collection_name)

    def data(self):
        return self._data

    def id_list(self):
        return [document for document in self._data]

x = MongoData('listHuntList')
print(x.data())