from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Klee:GenshinTarot@genshintarot.no45cbt.mongodb.net/?retryWrites=true&w=majority&appName=GenshinTarot"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

enemies = client["GenshinTarotCards"]
a = enemies["Enemy"].find_one()
print(a)

character = client["GenshinTarotCards"]
b = list(character["Characters"].find({"Name": {"$ne":"Template"}}))
# print(b)
ch = [x["Name"] for x in b]
print(ch)

import random
random.shuffle(ch)
print(ch)