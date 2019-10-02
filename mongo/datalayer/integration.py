# MONGO_CLIENT = MongoClient(mongo_url)
# CM_DB = MONGO_CLIENT[mongo_db]


def return_objects_by_query(collection, **query):
    """
    Function to return mongo objects based on specific query

    :param collection (string): String of collection/method name
    :param query (dict): Query dictionary
    :return (list): List of mongo objects
    """

    return list(CM_DB[collection].find(dict(query)))

print('sup')
