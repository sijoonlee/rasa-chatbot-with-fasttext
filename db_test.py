from pymongo import MongoClient
import pprint
client = MongoClient('mongodb://127.0.0.1:27017')
db = client.slc_db
collection = db.teachers
pprint.pprint(collection.find_one({"name":{'$regex':'donna'}})['room'])
pprint.pprint(collection.find_one({"name":"James"}))