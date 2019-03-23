# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "crawl1"
    # allowed_domains = ["example.com"]
    # start_urls = ['http://example.com/']
    start_urls = ['http://httpbin.org/get']

    # response 处理
    def parse(self, response):
        print(response.text)
        # pass
