from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# insert / find / update / delete

# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)

# same_ages = list(db.users.find({},{'_id':False}))
# user = db.users.find_one({'name':'bobby'},{'_id':False})

# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
# db.users.update_many({'name':'bobby'},{'$set':{'age':19}})

# db.users.delete_one({'name':'bobby'})
# db.users.delete_many({'name':'bobby'})

