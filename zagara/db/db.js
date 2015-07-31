use mydb


db.aqi.drop()

db.createCollection('aqi');
db.aqi.insert({'city':'shanghai', 'aqi':'150', 'date':'20150101', 'updateTime':'13:00','crawlTime':'13:30'})


db.aqi.find()
// db.getCollectionNames().forEach(function(collection) {
//   print(collection);
// });