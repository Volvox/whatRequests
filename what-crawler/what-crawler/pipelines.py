
# class WhatcrawlerPipeline(object):
#     def process_item(self, item, spider):
#         return item

import pymongo
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log
class whatRequestsPipeline(object):
    def process_item(self, item, spider):
        return item
class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        
    def process_item(self, item, spider):
    	valid = True
        for data in item:
          # check if the data is not null
       	  if not data:
            valid = False
            raise DropItem("Missing %s of titles from %s" %(data, item['url']))
        if valid:
          self.collection.insert(dict(item))
          log.msg("Item wrote to MongoDB database %s/%s" %
                  (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                  level=log.DEBUG, spider=spider) 
        return item