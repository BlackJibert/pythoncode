# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest, Request


class SpiderpostSpider(scrapy.Spider):
    name = "spiderpost"
    # allowed_domains = ["httpbin.org"]
    # starturls = 'http://httpbin.org/post'
    # "oSqXgiQ0dBFn5aNywI/BLkosYQKNlKd0K4QspnZP1HLLuA/ePxcjU0RItphFoIkOfySKiLQW27AKcmjLmqPmjQ=="
    # "wOgMHIwtyvdS1iwLG05afiq0/+gSkFr0RjS+x6f0nP/DALNvQiBVvuKsLRVMHfDJEtfNdTga2MdmYid0OcqxwQ=="
    starturls = 'https://github.com/login'
    loginurls = 'https://github.com/session'

    def start_requests(self):
        yield Request(self.starturls, callback=self.pre_parse)

    def pre_parse(self, response):
        # print(response.url)
        # pass
        form = response.xpath('//form[@action="/session"]').extract()
        # print(form)
        keys = ['utf8', 'authenticity_token', 'commit']
        values = []
        for key in keys:
            xpath_ = '//form[@action="/session"]//input[@name="%s"]/@value' % key
            value = response.xpath(xpath_).extract()[0]
            values.append(value)
        # print(values)
        postdata = dict(zip(keys, values))
        postdata['login'] = 'pythontest123'
        postdata['password'] = 'github123'
        # print(postdata)
        yield FormRequest(self.loginurls, formdata=postdata, callback=self.login_parse)

    def login_parse(self, response):
        # print(response.url)
        # 检验是否登陆成功
        print(response.xpath('//meta[@name="user-login"]/@content').extract())
