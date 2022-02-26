"""
working with local MongoDB cloud
"""

import pymongo
import urllib.parse

username = urllib.parse.quote_plus('*********')
password = urllib.parse.quote_plus("************")

cluster = pymongo.MongoClient("*************************")


dbname='MY_DB1'
db = cluster[dbname] # connecting to the database named HK_DB1 present in the mongoDB
                    # if the database is not present, it'll autoamtically create it.

collection_name='MY_Collection1'
collection=db[collection_name]  # connectig to the collection


collection.insert_one({"_id": 0, "name": 'ab'})
