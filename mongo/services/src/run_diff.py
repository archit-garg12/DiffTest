# main function that runs diff

import os
from pymongo import *
from bson_extract import read_bson_data


CLIENT = MongoClient('localhost')
DB = CLIENT['cucm_proxy_db']
DIRECTORY = '../../../dump/cucm_proxy_db/'


def run_all_collections():
    for collection in DB.list_collection_names():
        print(collection)
        old_data = read_bson_data(DIRECTORY + collection + '.bson')
        print(old_data)
        # run diff between current collection and collection stored in snapshot

# run_all_collections()


if __name__ == '__main__':
    # print('hello')
    os.system('mongodump -o ../../../dump')
