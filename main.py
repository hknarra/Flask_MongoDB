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