# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZhihuWeiboScrapyPipeline(object):

    def __init__(self, mongo_db, mongo_uri):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'), mongo_db=crawler.settings.get('MONGO_DB'))
        # return cls(mongo_db=crawler.settings.get('MONGO_DB'), mongo_uri=crawler.settings.get('MONGO_URI'))

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        pass

    def close_spider(self, spider):
        pass
