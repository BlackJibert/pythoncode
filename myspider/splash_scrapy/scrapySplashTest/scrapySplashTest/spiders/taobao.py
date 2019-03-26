# -*- coding: utf-8 -*-
from urllib.parse import quote

import scrapy
from scrapy_splash import SplashRequest

from ..items import ProductItem

# from ..items import ProductItem

script = """
function main(splash, args)
    splash.images_enabled = false
    assert(splash:go(args.url))
    assert(splash:wait(args.wait))
    js =string.format("document.querySelector('#mainsrp-pager div.form > input').value =%d;document.querySelector('#mainsrp-pager div.form >span.btn.J_Submit').click()", args.page)
    splash:evaljs(js)
    assert(splash:wait(args.wait))
    return splash:html()
end
"""

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    base_url = 'https://s.taobao.com/search?q='

    def start_requests(self):
        # driver = webdriver.Chrome()
        # try:
        #     driver.get('https://login.taobao.com/member/login.jhtml')
        #     click_ = driver.find_element_by_xpath('//div[@class="login-switch"]/i[@id="J_Quick2Static"]')
        #     sleep(1)
        #     driver.execute_script("arguments[0].click();", click_)
        #     sleep(2)
        #     # new_url =driver.current_url
        #     # driver.get(new_url)
        #     sleep(2)
        #     input_name = driver.find_element_by_id('TPL_username_1')
        #     input_name.clear()
        #     input_name.send_keys('13523823288')
        #     sleep(2)
        #     input_pwd =driver.find_element_by_id('TPL_password_1')
        #     input_pwd.send_keys('ZHJ1995369369')
        #     sleep(2)
        #     print(driver.current_url)
        #     input_pwd.send_keys(Keys.ENTER)
        # except :
        #     print("error")
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword)
                yield SplashRequest(url, callback=self.parse, endpoint='execute',
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
