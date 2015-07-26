from pymongo import MongoClient

#connecting to local
client = MongoClient()
#connect with ip
# conn = pymongo.Connection(host="192.168.1.202") 
db = client.mydb # database
users = db.aqi # collections
#users = db['users'] # collections with []

for item in users.find():
    print(item)

print("----------------------------------")

print(users.find_one()['aqi'])
print("----------------------------------")
print(users.find_one({"city": 'shanghai'})['aqi'])

print("----------------------------------")

print(users.find_one())