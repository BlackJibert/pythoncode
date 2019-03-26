# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class ScrapysplashjdPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    def __init__(self, mongo_db, mongo_uri):
        self.mongo_db = mongo_db
        self.mongo_uri = mongo_uri

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_db=crawler.settings.get('MONGO_DB'), mongo_uri=crawler.settings.get('MONGO_URI'))

    def open_spider(self, spider):
        # self.client = pymongo.MongoClient(self.mongo_uri)
        # 授予权限
        self.client = pymongo.MongoClient('mongodb://{0}:{1}@{2}:{3}'.format("admin", "admin123", 'localhost', 27017))
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[item.collection].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
