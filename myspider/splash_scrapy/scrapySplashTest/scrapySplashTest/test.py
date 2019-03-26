from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class taobao_infos:

    def __init__(self, url):
        self.url = 'https://login.taobao.com/member/login.jhtml'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 10)

    # 处理登陆信息
    def login(self):
        self.browser.get(self.url)
        sleep(6)
        self.browser.find_element_by_xpath('//*[@class="forget-pwd J_Quick2Static"]').click()
        sleep(2)
        self.browser.find_element_by_xpath('//*[@class="weibo-login"]').click()
        sleep(3)
        self.browser.find_element_by_name('username').send_keys('xxxxx')
        sleep(5)
        self.browser.find_element_by_name('password').send_keys('xxxxxxxxx')
        sleep(4)
        self.browser.find_element_by_xpath('//*[@class="btn_tip"]/a/span').click()


url = 'https://login.taobao.com/member/login.jhtml'
a = taobao_infos(url)
a.login()
