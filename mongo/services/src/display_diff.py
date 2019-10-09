"""
Iterates through snapshot json and compares to current db and shows new and removed files
Compares onld snapshot with onld database to check for differences in values for various keys




"""

import pymongo
import bson
from bson_extract import read_bson_data

DIRECTORY = '/users/dominicong/desktop/difftest/mongo/datalayer/cucm_proxy_db/'

client = pymongo.MongoClient('localhost')
db = client['cucm_proxy_db']


def run_all_collections():

    for collection in db.list_collection_names():
        print(collection)
        s = DIRECTORY + collection + '.bson'
        read_bson_data(s)


def _does_id_exist_in_dump(bson_file, object_id):

    with open(bson_file,'rb') as f:
        data = bson.decode_all(f.read())
        for val in data:
            if val['_id'] == object_id:
                return val
        return False


def difference_in_files():

    list_of_new_inserts = []
    for key in db['listHuntlist'].find():
        if _does_id_exist_in_dump(DIRECTORY + 'listHuntlist.bson',key['_id']) == False:
            list_of_new_inserts.append(key)
    print(list_of_new_inserts)


def _check_if_id_removed(collection, object_id):
    for key in db[collection].find():
        if key['_id'] == object_id:
            return True
    return False


def removed_files(bson_file):

    list_of_removed = []

    with open(bson_file,'rb') as f:
        data = bson.decode_all(f.read())
        for val in data:
            if _check_if_id_removed('listHuntlist',val['_id']) == False:
                list_of_removed.append(val)

    print(list_of_removed)


def _difference_in_dump(bson_file,object_data):

    list_of_diff = []
    with open(bson_file,'rb') as f:
        data = bson.decode_all(f.read())
        for val in data:
            if val['_id'] == object_data['_id']:
                for key in val.keys():
                    if val[key] != object_data[key]:
                        list_of_diff.append((key,val[key]))
    #print('hi')
    return list_of_diff


def difference_in_str(collection):

    for val in collection:
        temp_data = _difference_in_dump(DIRECTORY + 'listHuntlist.bson',val)
        if temp_data != []:
            for x in temp_data:
                if type(x[1]) == int and type(val[x[0]]) == int:
                    pass
                elif type(x[1]) == str and type(val[x[0]]) == str:
                    print('%s: (%s -> %s)'%(x[0],x[1],val[x[0]]))


#db['listHuntlist'].insert_one({'test run': 'i like krish avvari'})


#y = bson.objectid.ObjectId('507f1f77bcf86cd799439011')

difference_in_str(db['listHuntlist'].find())
difference_in_files()
removed_files(DIRECTORY + 'listHuntlist.bson')
#run_all_collections()

#deleted 2019-10-06 22:47:02 ObjectId("5d9ad1567c48eeecc12052fd")