import getpass
import random

import scrapy

"""
info:
author:CriseLYJ
github:https://github.com/CriseLYJ/
update_time:2019-3-6
"""
import base64
import hashlib
import hmac
import json
import re
import time
from http import cookiejar
from urllib.parse import urlencode
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import execjs
import requests
from PIL import Image
from .chaojiying import Chaojiying_Client


class myZhihuAccount(scrapy.Spider):
    name = 'scrapy_my_zhihu'
    allowed_domains = ['www.zhihu.com']

    # start_urls = ['https://www.zhihu.com/']
    def __init__(self, username: str = None, password: str = None):
        self.username = "13523823288"
        self.password = "ZHJ1995369"

        self.login_data = {
            'client_id': 'c3cef7c66a1843f8b3a9e6a1e3160e20',
            'grant_type': 'password',
            'source': 'com.zhihu.web',
            'username': '',
            'password': '',
            'lang': 'en',
            'ref_source': 'homepage',
            'utm_source': ''
        }
        self.session = requests.session()
        self.session.headers = {
            'accept-encoding': 'gzip, deflate, br',
            'Host': 'www.zhihu.com',
            'Referer': 'https://www.zhihu.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
        self.session.cookies = cookiejar.LWPCookieJar(filename='./cookies.txt')
        # print(response.status_code)

    def start_requests(self):
        return [scrapy.Request(("https://www.zhihu.com"), headers=self.session.headers, callback=self.login)]

    def login(self, response):
        load_cookies = 'en'
        captcha_lang = 'en'
        # if load_cookies and self.load_cookies():
        #     print('读取 Cookies 文件')
        #     if self.check_login():
        #         print('登录成功')
        #         # print("开始获取数据...")
        # #         yield scrapy.Request("https://www.zhihu.com/", headers=self.session.headers, callback=self.parse)
        #         return True
        #     print('Cookies 已过期')
        self._check_user_pass()
        self.login_data.update({
            'username': self.username,
            'password': self.password,
            'lang': captcha_lang  # en
        })

        timestamp = int(time.time() * 1000)
        self.login_data.update({
            'captcha': self._get_captcha(self.login_data['lang']),
            'timestamp': timestamp,
            'signature': self._get_signature(timestamp)
        })

        headers = self.session.headers.copy()
        headers.update({
            'content-type': 'application/x-www-form-urlencoded',
            'x-zse-83': '3_1.1',
            'x-xsrftoken': self._get_xsrf()
        })

        data = self._encrypt(self.login_data)
        login_api = 'https://www.zhihu.com/api/v3/oauth/sign_in'
        resp = self.session.post(login_api, data=data, headers=headers)
        print("data", data)
        # res= FormRequest(url=login_api, headers=headers, formdata=data, callback=self.parse)

        # yield requests
        if 'error' in resp.text:
            print("json.loads(resp.text)['error']: ", json.loads(resp.text)['error'])
        if self.check_login():
            print('登录成功')
            responses_ = self.session.get('https://www.zhihu.com/search?type=content&q=python')
            print(responses_.text)
            # yield scrapy.Request("https://www.zhihu.com/", headers=headers, cookies=self.session.cookies, callback=self.parse)
            return True
        print('登录失败')
        return False

    def error_sdf(self, response):
        pass

    def load_cookies(self):
        """
        读取 Cookies 文件加载到 Session
        :return: bool
        """
        try:
            self.session.cookies.load(ignore_discard=True)
            return True
        except FileNotFoundError:
            return False

    def check_login(self):
        """
        检查登录状态，访问登录页面出现跳转则是已登录，
        如登录成功保存当前 Cookies
        :return: bool
        """
        login_url = 'https://www.zhihu.com/signup'
        resp = self.session.get(login_url, allow_redirects=False)
        print("status_code:", resp.status_code)
        if resp.status_code == 302:
            # print(responses.text)
            self.session.cookies.save()
            return True
        return False

    def _get_xsrf(self):
        """
        从登录页面获取 xsrf
        :return: str
        """
        self.session.get('https://www.zhihu.com', allow_redirects=False)
        for c in self.session.cookies:
            if c.name == '_xsrf':
                print("c.value: ", c.value)
                #
                return c.value
        raise AssertionError('获取 xsrf 失败')

    def _get_captcha(self, lang: str):
        """
        请求验证码的 API 接口，无论是否需要验证码都需要请求一次
        如果需要验证码会返回图片的 base64 编码
        根据 lang 参数匹配验证码，需要人工输入
        :param lang: 返回验证码的语言(en/cn)
        :return: 验证码的 POST 参数
        """
        if lang == 'cn':
            api = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=cn'
        else:
            api = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=en'
        resp = self.session.get(api)
        show_captcha = re.search(r'true', resp.text)

        if show_captcha:
            put_resp = self.session.put(api)
            json_data = json.loads(put_resp.text)
            img_base64 = json_data['img_base64'].replace(r'\n', '')
            with open('./captcha.jpg', 'wb') as f:
                f.write(base64.b64decode(img_base64))
            img = Image.open('./captcha.jpg')
            if lang == 'cn':
                plt.imshow(img)
                print('点击所有倒立的汉字，在命令行中按回车提交')
                points = plt.ginput(7)
                capt = json.dumps({'img_size': [200, 44],
                                   'input_points': [[i[0] / 2, i[1] / 2] for i in points]})
            else:
                chaojiying = Chaojiying_Client('MaxZhang', 'ZHJ1995369',
                                               '946107fc16aed79c8d3a02f2b5548b3e')
                time.sleep(random.random())
                im = open('captcha.jpg', 'rb').read()
                print('chaojiying.PostPic(im, 1902):', chaojiying.PostPic(im, 1902))
                capt = chaojiying.PostPic(im, 1902)['pic_str']
                print("capt:", capt)

            # 这里必须先把参数 POST 验证码接口
            self.session.post(api, data={'input_text': capt})
            return capt
        return ''

    def _get_signature(self, timestamp: int or str):
        """
        通过 Hmac 算法计算返回签名
        实际是几个固定字符串加时间戳
        :param timestamp: 时间戳
        :return: 签名
        """
        ha = hmac.new(b'd1b964811afb40118a12068ff74a12f4', digestmod=hashlib.sha1)
        grant_type = self.login_data['grant_type']
        client_id = self.login_data['client_id']
        source = self.login_data['source']
        ha.update(bytes((grant_type + client_id + source + str(timestamp)), 'utf-8'))
        return ha.hexdigest()

    def _check_user_pass(self):
        """
        检查用户名和密码是否已输入，若无则手动输入
        """
        if not self.username:
            self.username = input('请输入手机号：')
        if self.username.isdigit() and '+86' not in self.username:
            self.username = '+86' + self.username

        if not self.password:
            # 输入密码不可见
            self.password = getpass.getpass("password:")

    @staticmethod
    def _encrypt(form_data: dict):
        with open('./encrypt.js') as f:
            js = execjs.compile(f.read())
            return js.call('Q', urlencode(form_data))

    def parse(self, response):
        print("hello-parse")
        print(response.text)
