# -*- coding: utf-8 -*-
import scrapy


class CrawlTaobaoSpider(scrapy.Spider):
    name = 'crawl_taobao'
    # allowed_domains = ['taobao.com']
    start_urls = ['https://s.taobao.com/search?q=ipad&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=0']

    # def start_requests(self):
    #    base_url = 'https://s.taobao.com/search?initiative_id=staobaoz_'

    def parse(self, response):
        print("123")
        print(response.text)
