# -*- coding: utf-8 -*-
import re

import scrapy
from bs4 import BeautifulSoup

from ..items import ScrapyTiebaItem


class TeibaSpider(scrapy.Spider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    # start_urls = ['http://tieba.com/']
    # 搜索关键字
    keywords = 'python'
    # 用作翻页，加50进入下一页
    pn = 0
    base_url = "http://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%s" % (keywords, pn)

    def start_requests(self):
        # # while True:
        #     #判断'下一页'是否存在，存在的话则对pn字段加50进入下一页
        #     if response.xpath('//div[@id="frs_list_pager"]/a[contains(@class,"next")]//text()'):
        #         # next_ = response.xpath('//div[@id="frs_list_pager"]/a[contains(@class,"next")]')
        #         # print("下一页： ", next_)
        #         page = response.xpath('//div[@id=]/span[contains(@class,"pagination-current")]//text()')
        #         print(page)
        #         self.pn += 50
        #         self.base_url ="http://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%s" % (self.keywords, self.pn)
        #         yield scrapy.Request(url=self.base_url, callback=self.parse)
        #     else:
        #         print('内容到底！')
        #         break
        # while self.pn <= 100:
        #     yield scrapy.Request(url=self.base_url, callback=self.parse)
        #     self.pn += 50
        #     self.base_url ="http://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%s" % (self.keywords, self.pn)
        yield scrapy.Request(url=self.base_url, callback=self.next_requests)

    def next_requests(self, response):
        # 使用extract()把内容提取出来
        pages = response.xpath('//div[@id="frs_list_pager"]/a[contains(@class,"last")]/@href').extract_first()
        # soup = BeautifulSoup(response.text, 'lxml')
        # print(123, soup)
        # pages = soup.find(id="frs_list_pager")
        # 以'pn='进行分割成为两部分，来获取总评论数
        print("pages:", pages)
        pages_ = re.split('pn=', pages)
        print(type(pages_))
        print("评论总条数： ", int(pages_[1]))
        pages__ = int(pages_[1])
        # pages__ = 500
        while self.pn <= pages__:
            yield scrapy.Request(url=self.base_url, callback=self.detail)
            self.pn += 50
            self.base_url = "http://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%s" % (self.keywords, self.pn)

    # 进入评论页面的爬取
    def detail(self, response):
        # 找到所有的列表评论
        soup = BeautifulSoup(response.text, 'lxml')
        # links = soup.find_all("a", attrs={"class": "sister", "target": "_blank"})
        # 进行多属性的匹配
        list_ = soup.find_all("li", attrs={'class': "j_thread_list"})

        for one_of_list in list_:
            item_ = ScrapyTiebaItem()
            title = one_of_list.find(class_="j_th_tit").get_text().replace(" ", '').replace('\n', '').replace('\r', '')
            item_['title'] = title
            try:
                content = one_of_list.find('div', attrs={"class": "threadlist_abs"}).get_text().replace('\n',
                                                                                                        '').replace(" ",
                                                                                                                    '')
                item_['content'] = content
            except:
                # 若内容为空，则将标题存入
                item_['content'] = item_['title']
            url = one_of_list.find(class_="j_th_tit").a['href']
            url = "http://tieba.baidu.com" + url
            item_['url'] = url
            # yield item_
            # print(url)
            yield scrapy.Request(url=url, meta={'item_': item_}, callback=self.parse)

    def parse(self, response):
        item_ = response.meta['item_']
        # print(item_)
        # time_ = response.xpath('//div[contains(@class,"l_post")]/div[@class="d_author"]').extract_first().replace('\n', '').replace(" ", '').replace("\t", '')

        author = response.xpath(
            '//div[contains(@class,"l_post")]//div[contains(@class,"louzhubiaoshi")]/@author').extract_first()
        item_['author'] = author
        time_ = response.xpath('//div[@class="d_post_content_main"]//li').extract()
        # 回复贴的个数
        comment_nums = response.xpath('//div[@id="thread_theme_5"]//text()').extract()[2]
        # comment_nums = int(comment_nums)
        item_['comment_nums'] = comment_nums

        # 回复贴几页
        comment_pages = response.xpath('//div[@id="thread_theme_5"]//text()').extract()[4]
        item_['comment_pages'] = comment_pages
        # 回帖的内容
        # comments = response.xpath('//div[contains(@class,"j_l_post")]//div[contains(@class,"j_d_post_content")]')

        soup = BeautifulSoup(response.text, 'lxml')
        comments_ = soup.find_all('div', attrs={"class": "l_post"})
        # print(comments_)
        comments = []
        for comment in comments_:
            co = {}
            com_author = comment.find(class_="d_author").get_text().replace(' ', '').replace('\n', '').replace('\t', '')
            com_content = comment.find("div", attrs={"class": "p_content"}).find("div",
                                                                                 class_="d_post_content").get_text().replace(
                ' ', '').replace('\n', '').replace('\t', '')
            co['author'] = com_author
            co['content'] = com_content
            time_ = comment.find("ul", class_='.p_tail')
            print(time_)
            comments.append(co)
            # print(com_author)
            # print(com_content)
            # print('---------------')
            # comment_author = comment.xpath('//div[contains(@class,"louzhubiaoshi")]/@author').extract_first()
            # print(comment_author)
            # comment_content = comment.xpath('//text()')
            # comments = response.xpath('//div[contains(@class,"j_l_post")]//div[contains(@class,"j_d_post_content")]//text()').extract()[comment]
            # comments_.append(comments)
        item_['comments'] = comments
        # pass
        # yield item_
