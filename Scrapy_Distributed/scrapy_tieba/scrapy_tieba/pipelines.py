# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class ScrapyTiebaPipeline(object):

    def process_item(self, item, spider):
        return item


class TiebagPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        # 授予权限，由于本地的mongodb设置了权限
        # self.client = pymongo.MongoClient('mongodb://{0}:{1}@{2}:{3}'.format("admin", "admin123", '118.25.94.130', 27017))
        self.client = pymongo.MongoClient(
            'mongodb://{0}:{1}@{2}:{3}'.format("admin", "admin123", self.mongo_uri, 27017))
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[item.collection].insert(dict(item))
        # self.db[item.collection].update(dict(item), {"$set": item['img_url']})
        return item

    def close_spider(self, spider):
        self.client.close()
