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
        self.logined_url = 'https://github.com/settings/profile'
        # 用到了requests的Session()
        self.session = requests.Session()

    # 访问登录界面，获取初试的Cookies，提取出 authwnticity_token

    # 实现一个token
    def token(self):
        respones = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(respones.text)
        print(selector)
        # 逐层获取,以便获取value值
        token = selector.xpath('//div[@id="login"]/form/input[2]/@value')
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
            print("关注人的动态信息：")
            self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            print("处理个人的详情页：")
            self.profile(response.text)

    # 显示关注人的动态信息
    def dynamics(self, html):
        selector = etree.HTML(html)
        # print(html)
        dynamics = selector.xpath('//div[contains(@class,"news")]//div[contains(@class, "alert")]')

        print(dynamics)
        for item in dynamics:
            dynamics = ' '.join(item.xpath('.//div(@class="title")]//text()')).strip()
            print(dynamics)

    # 处理个人详情页
    def profile(self, html):
        selector = etree.HTML(html)
        # print(html)
        name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
        print(name, email)


if __name__ == "__main__":
    user = Login()
    user.login("1257699625@qq.com", "ZHJ1995369369zhj")
    # user.login('1016903103@qq.com', 'cqc@cuiqingcai.com')
