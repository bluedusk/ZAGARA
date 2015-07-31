
from pymongo import MongoClient
from datetime import datetime


#connecting to local
client = MongoClient()
#connect with ip
# conn = pymongo.Connection(host="192.168.1.202") 
db = client.mydb # database
users = db.aqi # collections
#users = db['users'] # collections with []



items = [{'city': 'beijing',
 'crawlTime': '21:15',
 'date': '2015-07-26',
 'updateTime': u'20:00',
 'value': u'158'}, {'city': 'shanghai',
 'crawlTime': '21:15',
 'date': '2015-07-26',
 'updateTime': u'20:00',
 'value': u'142'}, {'city': 'guangzhou',
 'crawlTime': '21:15',
 'date': '2015-07-26',
 'updateTime': u'20:00',
 'value': u'76'}, {'city': 'chengdu',
 'crawlTime': '21:15',
 'date': '2015-07-26',
 'updateTime': u'20:00',
 'value': u'87'}]


# for item in users.find():
#     print(item)

#users.insert_many(items)

db.aqi.insert({'city':'shanghai', 'aqi':'150', 'date':'20150101', 'updateTime':'13:00','crawlTime':datetime.now().strftime('%H:%M')})

# print("----------------------------------")

# print(users.find_one())
# print("----------------------------------")
# print(users.find_one({"city": 'shanghai'}))

# print("----------------------------------")

# print(users.find_one())

#*/1 * * * * python ~/MyWork/ws-py/ZAGARA/zagara/db/mongo.py  >> ~/hi.log 2>&1

 