# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = "mvinfo"
    # allowed_domains = ["example.com"]
    # start_urls = ['http://example.com/']
    start_urls = ['http://httpbin.org/ip']

    def start_requests(self):
        return scrapy.Request('http://httpbin.org/get', callback=self.parse)

    # response 处理
    def parse(self, response):
        print(response.text)
        # pass
