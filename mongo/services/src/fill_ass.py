import pymongo
import json



x = pymongo.MongoClient('localhost')['cucm_proxy_db']['listHuntList']
x.insert_one({'sup': 'sup2'})