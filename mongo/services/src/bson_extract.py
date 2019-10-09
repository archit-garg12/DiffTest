# Convert bson to json
# For comparing the snapshot(BSON) to the current db(JSON)


import bson

DIRECTORY = '/Users/krishnatejaavvari/PycharmProjects/DiffTest/mongo/datalayer/dump/cucm_proxy_db/'


def read_bson_data(collection_name):
    bson_file = DIRECTORY + collection_name + '.bson'
    with open(bson_file, 'rb') as f:
        data = bson.decode_all(f.read())
        return {document['_id'] : document for document in data}


print(read_bson_data('listHuntList'))

