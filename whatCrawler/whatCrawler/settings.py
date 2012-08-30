# Scrapy settings for whatRequests project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
ITEM_PIPELINES = ['whatCrawler.pipelines.MongoDBPipeline',]
MONGODB_SERVER = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_DB = "whatRequests"
MONGODB_COLLECTION = "requests"

BOT_NAME = 'whatCrawler'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['whatCrawler.spiders']
NEWSPIDER_MODULE = 'whatCrawler.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

