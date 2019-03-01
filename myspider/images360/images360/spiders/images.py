# -*- coding: utf-8 -*-
from json import loads
from urllib.parse import urlencode

import scrapy
from images360.items import Images360Item


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']

    # start_urls = ['http://images.so.com/']

    # 重写Spier中的start_requests方法:指定开始Url
    def start_requests(self):
        base_url = "http://image.so.com/zj?"
        param = {'ch': "photography", 'listtpye': "new", "temp": "1"}
        # 可以根据需要爬取不同数量的图片，此处只爬取60张图片
        for page in range(2):
            param["sn"] = page * 30
            full_url = base_url + urlencode(param)
            yield scrapy.Request(url=full_url, callback=self.parse)

    def parse(self, response):
        # 获取到的内容是json数据
        #     # 用json.loads(）解析数据
        #     # 此处的response没有content
        model_dict = loads(response.text)
        # print(model_dict["list"])
        for element in model_dict["list"]:
            item = Images360Item()
            item["title"] = element["group_title"]
            item["tags"] = element["tag"]
            item["height"] = element["cover_height"]
            item["weight"] = element["cover_width"]
            item["url"] = element["qhimg_thumb_url"]
            yield item
