# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Images360Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 两个属性collection和tabel,都定义为images字符串，分别代表MongoDB存储的Collection名称
    # MySQL存储的表名称
    collection = table = "images"
    id = scrapy.Field()
    title = scrapy.Field()
    tags = scrapy.Field()
    url = scrapy.Field()
    height = scrapy.Field()
    width = scrapy.Field()
