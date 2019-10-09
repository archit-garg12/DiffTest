from pymongo import *
from bson import json_util

CLIENT = MongoClient('localhost')
DB = CLIENT['cucm_proxy_db']


def pull_data_by_collection(collection_name, field):
    return {document[field]:document for document in DB[collection_name].find()}
