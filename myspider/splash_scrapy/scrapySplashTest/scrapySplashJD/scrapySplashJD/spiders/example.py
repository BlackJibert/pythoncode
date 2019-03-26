# -*- coding: utf-8 -*-
from urllib.parse import quote

import scrapy
from scrapy_splash import SplashRequest

from ..items import MongoPipelineItem

script = """
function main(splash, args)
    splash.images_enabled = false
    assert(splash:go(args.url))
    assert(splash:wait(args.wait))
    js =string.format("document.querySelector('#J_bottomPage span.p-skip > input').value=%d;document.querySelector('#J_bottomPage span.p-skip > a.btn.btn-default').click()", args.page)
    splash:evaljs(js)
    assert(splash:wait(args.wait))
    return splash:html()
end
"""


class ExampleSpider(scrapy.Spider):
    name = 'example'
    # allowed_domains = ['example.com']
    base_url = 'https://search.jd.com/search?keyword='

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword)
                yield SplashRequest(url, callback=self.parse, endpoint='execute',
                                    args={'lua_source': script, 'page': page, 'wait': 7})

    def parse(self, response):
        products = response.xpath(
            '//div[@id="J_goodsList"]/ul[contains(@class,gl-warp )]//li[@class="gl-item"]'
        )
        for product in products:
            item = MongoPipelineItem()
            item['shop'] = ''.join(product.xpath(
                './div[@class="gl-i-wrap"]//div[@class="p-shop"]/span[@class="J_im_icon"]/a/@title').extract_first()).strip()
            # item['title'] = 'hello'
            item['price'] = ''.join(
                product.xpath('./div[@class="gl-i-wrap"]//div[@class="p-price"]//i/text()').extract_first()).strip()
            item['title'] = ''.join(product.xpath(
                './div[@class="gl-i-wrap"]//div[contains(@class,"p-name")]/a//text()').extract()).strip().replace("\n",
                                                                                                                  "").replace(
                "\t", "").replace("\r", "").replace(" ", "")
            item['deal'] = ''.join(
                product.xpath('./div[@class="gl-i-wrap"]//div[@class="p-commit"]/strong//text()').extract()).strip()
            print(item)
            yield item
