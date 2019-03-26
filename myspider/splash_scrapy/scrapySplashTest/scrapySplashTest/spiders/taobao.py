# -*- coding: utf-8 -*-
from urllib.parse import quote

import scrapy
from scrapy_splash import SplashRequest

# from ..items import ProductItem
from ..items import ProductItem

script = """
function main(splash, args)
    splash.image_enagled = falsh
    assert(splash:go(args.url))
    assert(splash:wait(args.wait))
    js =string.format("document.querySelector('#mainsrp-pager div.form > input').value =%d;
        document.querySelector('#mainsrp-pager div.form >span.btn.J_Submit').click()", args.page)
    splash:evaljs(js)
    assert(splash:wait(args.wait))
    return splash:html()
end
"""


class TaobaoSpider(scrapy.Spider):
    name = 'taobao2'
    # allowed_domains = ['www.taobao.com']
    start_urls = 'https://s.taobao.com/search?q='

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.start_urls + quote(keyword)
                yield SplashRequest(url, callback=self.parse, endpoint='excute',
                                    args={'lua_source': script, 'page': page, 'wait': 7})

    def parse(self, response):
        products = response.xpath(
            '//div[@id="mainsrp-itemlist"]//div[@class="items"][1]//div[contains(@class, "item")]'
        )
        for product in products:
            item = ProductItem()
            item['price'] = ''.join(product.xpath('.//div[contains(@class,"price")]//text()').extract()).strip()
            item['title'] = ''.join(product.xpath('.//div[contains(@class,"title")]//text()').extract()).strip()
            item['shop'] = ''.join(product.xpath('.//div[contains(@class,"shop")]//text()').extract()).strip()
            item['image'] = ''.join(
                product.xpath('.//div[@class="pic"]//div[contanis(@class, "img")]/@data-src').extract()).strip()
            item['deal'] = product.xpath('.//div[contains(@class, "deal-cnt")]//text()').extract_first()
            item['location'] = product.xpath('.//div[contains(@class, "location")]//text()').extract_first()
            yield item
