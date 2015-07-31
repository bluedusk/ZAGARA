# Scrapy settings for dirbot project

SPIDER_MODULES = ['zagara.spiders']
NEWSPIDER_MODULE = 'zagara.spiders'
DEFAULT_ITEM_CLASS = 'zagara.items.Website'
DOWNLOAD_DELAY = 1  #seconds of delay 


#ITEM_PIPELINES = {'zagara.pipelines.FilterWordsPipeline': 1}
ITEM_PIPELINES = {'zagara.pipelines.MongoDBPipeline': 1}



MONGO_URI = 'localhost:27017'
MONGO_DATABASE = 'mydb'
MONGODB_COLLECTION = 'aqi'