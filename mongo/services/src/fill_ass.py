# temporary fill script

import pymongo
import json

x = pymongo.MongoClient('localhost')['cucm_proxy_db']['listHuntList']

for i in range(1000):
    x.insert_one({'sup': i})