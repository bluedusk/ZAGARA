# -*- coding: utf-8 -*- 

from scrapy.exceptions import DropItem
from pymongo import MongoClient
import time
from logger import Logger


class TestPipeline(object):


    items = []

    def __init__(self):
        print '__init__'    
    #called every 
    def process_item(self, item, spider):
        self.items.append(item)
        #print item
        print 'process_item'
        return item

    def open_spider(self, spider):
        print 'open_spider'

    def close_spider(self, spider):
        print self.items
        print 'close_spider'

class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word in unicode(item['description']).lower():
                raise DropItem("Contains forbidden word: %s" % word)
        else:
            return item


#
class MongoDBPipeline(object):

    collection_name = 'aqi'
    items = []


    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        print '------------connect to mongodb:', self.mongo_uri

        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        #insert to mongodb when close spider
        print '------------insert data:',len(self.items)
        print self.items
        self.db[self.collection_name].insert_many(self.items)
        self.client.close()

    def process_item(self, item, spider):

        self.items.append(item)
        #self.db[self.collection_name].insert(dict(item))
        return item


logger = Logger().getlog()

class MongoDBPipeline1(object):


    collection_name = 'aqi_hour'
    items = []


    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        #print '[open spider] ------------connect to mongodb:', self.mongo_uri
        logger.debug("[open spider] ------------> connect to mongodb:%s",  self.mongo_uri)

        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        print self.items
        # logger = Logger().getlog()

        logger.debug("[close spider] ------------> Done scrawl, insert data to aqi_hour:%s", len(self.items))
        if len(self.items)>0:
            self.db[self.collection_name].insert_many(self.items)
        self.client.close()

    def process_item(self, item, spider):
        #print item['hour']
        if item['hour'] == time.localtime()[3]:
            logger.debug("[process item] add to array ------------>%s",item);
            self.items.append(item)
            return item
        else:
            logger.debug("[process item] DropItem ------------>%s",item);
            raise DropItem("DropItem----> Its not the aqi for this hour!")
        #self.db[self.collection_name].insert(dict(item))
        