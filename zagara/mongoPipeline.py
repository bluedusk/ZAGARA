

class MongoDBPipeline(object):
    def __init__(self, mongodb_server, mongodb_port, mongodb_db, mongodb_collection):
        connection = pymongo.Connection(mongodb_server, mongodb_port)
        self.mongodb_db = mongodb_db
        self.db = connection[mongodb_db]
        self.mongodb_collection = mongodb_collection
        self.collection = self.db[mongodb_collection]

    @classmethod
    def from_crawler(cls, crawler):
        # 连接mongodb
        return cls('localhost', 27017, 'scrapy', 'items')

    def process_item(self, item, spider):
        result = self.collection.insert(dict(item))
        log.msg("Item %s wrote to MongoDB database %s/%s" % (result, self.mongodb_db, self.mongodb_collection),
                level=log.DEBUG, spider=spider)
        return item