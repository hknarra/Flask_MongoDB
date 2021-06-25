"""
working with local MongoDB client
"""

import pymongo
dbConn = pymongo.MongoClient("mongodb://localhost:27017/")

dbname='hk_DB1'
db = dbConn[dbname] # connecting to the database named hkDB1 present in the mongoDB
                    # if the database is not present, it'll autoamtically create it.


# check if the databse exists in mongoDB
dblist=dbConn.list_database_names() # obtaining all the database names
db_name='hk_DB1'

if dblist.index(db_name)==-1:
    print ("This Database doesn't exist")
else:
    print ("This Database exists \n")


# show all the databases
print(dbConn.list_database_names())


# connecting to a collection(collections are tables in MongoDB)
collection_name='hk_collection1'
collection=db[collection_name]  # connectig to the collection

# cheking if a collection exists
if collection_name in db.list_collection_names():
    print("The collection exists.")
else:
    print("The collection doesn't exist.")


# inserting a row into collection
hk_row1 = {'id': '1235',
 'name': 'hl',
 'profession': 'ASE'
 } # creating key value pairs for inserting into the DB

x = collection.insert_one(hk_row1)  # inserting record into the collection
x.inserted_id  #gives unique of insert


# inserting multiple rows once
hk_rows = [
    {'id': '1234',
     'name': 'hk',
     'profession': 'SE'},
    {
        'id': '5678',
        'name': 'ab',
        'profession': 'associate'},

    {'id': '9123',
     'name': 'bc',
     'profession': 'lead'}
]
# inserting multiple records into the collection
x = collection.insert_many(hk_rows)


# retieving specific record from collection
result= collection.find({})
result[1] #printing the third record


# find brings out all the records, to overcoem this use limit
result_total= collection.find({}).limit(2)
for res in result_total:
    print(res)


# retrieveing specific columns
result_some= collection.find({}, {'id','name'}).limit(2) # retrieveing two columns
# The second parameter in find() specifies which columns to choose
for res in result_some:
    print(res)


# finding the rows based on given criteria
my_db_query={'name':'hk'}

result1= collection.find(my_db_query) # printing rows where name = hk
for res in result1:
    print(res)


# Deleting records from mongo DB:
# finding the rows based on given conditon
my_db_query={'name':'hk'}
x=collection.delete_one(my_db_query) # the deletion step
print(x.deleted_count)


