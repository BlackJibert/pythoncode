# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTiebaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    collection = "tieba"
    title = scrapy.Field()
    # 发帖内容
    content = scrapy.Field()
    # 帖子的地址
    url = scrapy.Field()
    # 发帖作者
    author = scrapy.Field()
    # 回帖的个数
    comment_nums = scrapy.Field()
    # 回帖的所占的页数
    comment_pages = scrapy.Field()
    # 回帖内容
    comments = scrapy.Field()
