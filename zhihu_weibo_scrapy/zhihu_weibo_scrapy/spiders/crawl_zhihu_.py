# from scrapy_splash import SplashRequest
import scrapy
from scrapy.http import Request


class CrawlZhihuSpider(scrapy.Spider):
    name = 'zhihu_'
    username = "13523823288"
    password = "ZHJ1995369"
    login_data = {
        'client_id': 'c3cef7c66a1843f8b3a9e6a1e3160e20',
        'grant_type': 'password',
        'source': 'com.zhihu.web',
        'username': '',
        'password': '',
        'lang': 'en',
        'ref_source': 'homepage',
        'utm_source': ''
    }
    headers = {
        'accept-encoding': 'gzip, deflate, br',
        'Host': 'www.zhihu.com',
        'Referer': 'https://www.zhihu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }

    def start_requests(self):
        # def start_requests(self):  # 用start_requests()方法,代替start_urls
        """第一次请求一下登录页面，设置开启cookie使其得到cookie，设置回调函数"""
        return [Request('https://www.zhihu.com', meta={'cookiejar': 1}, headers=self.headers, callback=self.parse)]

    def parse(self, response):
        Cookie1 = response.headers.getlist('Set-Cookie')  # 查看一下响应Cookie，也就是第一次访问注册页面时后台写入浏览器的Cookie
        cookie_dict = {}
        cookie_list = []
        for cookie in Cookie1:
            cookie = str(cookie, encoding="utf8")
            cookie2 = cookie.split(';')
            for cookie3 in cookie2:
                cookie4 = cookie3.split('=')
                for cookie5 in cookie4:
                    # print(cookie5)
                    cookie_list.append(cookie5)
        for index, value in enumerate(cookie_list):
            if index % 2 == 0:
                cookie_dict[value] = cookie_list[index + 1]
        print(cookie_dict)
        yield Request('https://www.zhihu.com/api/v3/oauth/sign_in', headers=self.headers, cookies=cookie_dict,
                      callback=self.get_)

    def get_(self, reponse):
        # print(reponse.text)
        pass
