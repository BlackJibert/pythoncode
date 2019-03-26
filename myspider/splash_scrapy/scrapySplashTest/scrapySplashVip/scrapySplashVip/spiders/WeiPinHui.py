# -*- coding: utf-8 -*-
import scrapy


class WeipinhuiSpider(scrapy.Spider):
    name = 'WeiPinHui'
    # allowed_domains = ['https://www.vip.com']
    start_urls = 'https://www.vip.com/'

    def start_requests(self):
        pass

    def parse(self, response):
        pass
