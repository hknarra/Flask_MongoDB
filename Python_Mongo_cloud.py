"""
working with local MongoDB cloud
"""

import pymongo
import urllib.parse

username = urllib.parse.quote_plus('mongokittu')
password = urllib.parse.quote_plus("kittu@1mongo")

cluster = pymongo.MongoClient("mongodb+srv://{}:{}@cluster0.svyqr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


dbname='HK_DB1'
db = cluster[dbname] # connecting to the database named HK_DB1 present in the mongoDB
                    # if the database is not present, it'll autoamtically create it.

collection_name='HK_Collection1'
collection=db[collection_name]  # connectig to the collection


collection.insert_one({"_id": 0, "name": 'hk'})
