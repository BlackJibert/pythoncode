from time import sleep
from lxml import etree
from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Scrapy_Distributed.scrapy_taobao.scrapy_taobao.spiders.chaojiying import Chaojiying_Client
from Scrapy_Distributed.scrapy_taobao.scrapy_taobao.spiders.get_proxy import create_proxyauth_extension
from time import sleep

from PIL import Image
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Scrapy_Distributed.scrapy_taobao.scrapy_taobao.spiders.chaojiying import Chaojiying_Client
from Scrapy_Distributed.scrapy_taobao.scrapy_taobao.spiders.get_proxy import create_proxyauth_extension

# 代理服务器
proxy_host = 'proxy.abuyun.com'
proxy_port = '9020'
# 代理隧道验证信息
proxy_user = 'HX2N4D0N26NDQ04D'
proxy_pass = '9773B54281C83554'

proxy_meta = 'http://%(user)s:%(pass)s@%(host)s:%(port)s' % {
    'host': proxy_host,
    'port': proxy_port,
    'user': proxy_user,
    'pass': proxy_pass
}
proxies = {
    'http': proxy_meta,
    'https': proxy_meta,
}

print(proxy_meta)

base_url = 'https://login.taobao.com/member/login.jhtml'
Chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(proxies)
proxyauth_plugin_path = create_proxyauth_extension(
    proxy_host="http-dyn.abuyun.com",
    proxy_port=9020,
    proxy_username="HX2N4D0N26NDQ04D",
    proxy_password="9773B54281C83554"
)

# Chrome_options.add_argument("--start-maximized")
# 以插件的形式使用阿布云代理服务器
Chrome_options.add_extension(proxyauth_plugin_path)
# Chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=Chrome_options)
browser.get(base_url)
# 5秒内如果没有成功加载这个 login-switch这个'按钮'，就抛出异常
wait = WebDriverWait(browser, 5)
# 由手机登录界面登录切换到由账号和密码登录
# browser.find_element_by_xpath('//div[@class="login-switch"]').click()
switch_button = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="login-switch"]')))
# switch_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="login-switch"]')))
switch_button.click()
sleep(1)
# 切换到使用微博账号来登录淘宝
weibo_login = browser.find_element_by_xpath('//ul[@class="entries"]//a[@class="weibo-login"]')
weibo_login.click()

# print(switch_button)
# wait2 = WebDriverWait(driver, 5)
# input_name = wait2.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"username-field")]/input[id="TPL_username_1"]')))
# input_name.send_keys('13523823288')
# wait3 = WebDriverWait(driver, 5)
# input_password = wait3.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"pwd-field")]/input[id="TPL_password_1"]')))
# input_password.send_keys('ZHJ1995369369')
# 定位微博账号
input_name = browser.find_element_by_xpath('//div[contains(@class,"username")]/input[@name="username"]')
input_name.clear()
input_name.send_keys('13523823288')
sleep(1)
# 定位微博密码
input_password = browser.find_element_by_xpath('//div[contains(@class,"password")]//input[@name="password"]')
input_password.clear()
sleep(1)
input_password.send_keys('ZHJ1995')
# print(browser.current_url)
# browser.get(browser.current_url)
# browser.get_cookies()
# 获取当前网页代码
yangzhengma_src = browser.page_source
# print(yangzhengma_src)
yangzhengma_src = etree.HTML(yangzhengma_src)
# 获取验证码链接
yanzhengma = yangzhengma_src.xpath('//div[contains(@class,"verify")]/a/img/@src')
print(yanzhengma)
# 进行下载，然后使用超级鹰进行识别
# if urllib.request.urlretrieve(yanzhengma[0], filename="yanzhengma.jpg"):
#     img = Image.open('./yanzhengma.jpg')
#     # 识别的验证码和链接，网页打开的验证码，三者不相同
#     chaojiying = Chaojiying_Client('MaxZhang', 'ZHJ1995369', '946107fc16aed79c8d3a02f2b5548b3e')
#     im = open('yanzhengma.jpg', 'rb').read()
#     print('chaojiying.PostPic(im, 1005):', chaojiying.PostPic(im, 1005))
#     capt = chaojiying.PostPic(im, 1005)['pic_str']
#     print("capt:", capt)
#     input_yanzhengma = browser.find_element_by_xpath('//div[contains(@class,"verify")]/input')
#     input_yanzhengma.send_keys(capt)
#     # input_yanzhengma.send_keys()
#     input_ok = browser.find_element_by_xpath('//div[@class="btn_tip"]/a[@class="W_btn_g"]')
#     input_ok.click()
# else:

# # browser.close()
# sleep(1)driver.get_screenshot_as_file('pei.png')
# 当前网页截图
browser.get_screenshot_as_file(r'photo.png')
# 找到验证码在网页中的位置
imgelement = browser.find_element_by_xpath('//div[contains(@class,"verify")]//img')
# 定位验证码在截图中的位置
location = imgelement.location
size = imgelement.size
print(location)
print(size)
left = imgelement.location['x']
top = imgelement.location['y']
elementWidth = imgelement.location['x'] + imgelement.size['width']
elementHeight = imgelement.location['y'] + imgelement.size['height']
picture = Image.open(r'photo.png')
picture = picture.crop((left, top, elementWidth, elementHeight))
# 保存验证码图片
picture.save(r'photo2.png')
# 直接使用（付费）超级鹰的接口来识别识别验证码 【超级鹰用户名，密码，】
chaojiying = Chaojiying_Client('MaxZhang', 'ZHJ1995369', '946107fc16aed79c8d3a02f2b5548b3e')
im = open('photo2.png', 'rb').read()
# 其中代号1005为验证码的类型，可以登录超级鹰官网，来对比具体的验证码的代号 【http://www.chaojiying.com/price.html】
print('chaojiying.PostPic(im, 1005):', chaojiying.PostPic(im, 1005))
capt = chaojiying.PostPic(im, 1005)['pic_str']
print("capt:", capt)
input_yanzhengma = browser.find_element_by_xpath('//div[contains(@class,"verify")]/input')
input_yanzhengma.send_keys(capt)
# 定位到登录按钮，点击进行登录
browser.find_element_by_xpath('//div[@class="btn_tip"]/a[@class="W_btn_g"]').click()
# sleep(2)
