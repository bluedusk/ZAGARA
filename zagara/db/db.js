//初始化数据库脚本

use mydb

//drop & create tables
db.aqi_hour.drop()

//db.createCollection('aqi');
//db.createCollection('aqi_y');
db.createCollection('aqi_hour');
db.aqi_hour.insert({'city':'shanghai', 'aqi':'150', 'year':'2015', 'month':'5','day':'6','hour':'11','updateTime':'13:00','crawlTime':'13:30'})


db.aqi_hour.find()
// db.getCollectionNames().forEach(function(collection) {
//   print(collection);
// });