# -*- coding: utf-8 -*-
from urllib.parse import quote

import scrapy
from scrapy import Request


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    base_urls = 'https://s.taobao.com/search?q='

    def start_requests(self):
        # KWYWORDS和MAX_PAGE定义在settings里面
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_urls + quote(keyword)
                yield Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)
