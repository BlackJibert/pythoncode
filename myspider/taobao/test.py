import requests

# 定义Login类，初始化一些变量
from lxml import etree


class Login(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
            , 'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com'
        # 用到了requests的Session()
        self.session = requests.Session()

    # 访问登录界面，获取初试的Cookies，提取出 authwnticity_token

    # 实现一个token
    def token(self):
        respones = self.session.get(self.login_url, headers=self.headers)
        select = etree.HTML(respones.text)
        print(select)
        token = select.xpath('//div/input[1]/@value')[0]
        print("token:", token)
        return token

    # login方法
    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf-8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }

        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            # self.dynamics(response.text)
            print(123)

        response = self.session.post(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            # self.profile(response.text)
            print(234)


a = Login()
a.login("1257699625@qq.com", "ZHJ1995369369zhj")
