from pymongo import MongoClient
from bson import json_util, ObjectId
import json

config_file = open("./config/mongodb", "r+")
mongodb_address = config_file.read()

client = MongoClient(mongodb_address)
db = client.slc_db
collection = db.teachers

response = json.loads(json_util.dumps(collection.find_one({'name':'donna'})))

print(response['office'])

