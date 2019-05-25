from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 代理服务器
from Scrapy_Distributed.scrapy_taobao.scrapy_taobao.spiders.get_proxy import create_proxyauth_extension

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
Chrome_options.add_extension(proxyauth_plugin_path)
# Chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=Chrome_options)
browser.get(base_url)
# 5秒内如果没有成功加载这个 login-switch这个'按钮'，就抛出异常
wait = WebDriverWait(browser, 5)
# 由手机登录界面登录切换到由账号和密码登录
# browser.find_element_by_xpath('//div[@class="login-switch"]').click()
# switch_button = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="login-switch"]')))
switch_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="login-switch"]')))
switch_button.click()
# print(switch_button)
# wait2 = WebDriverWait(driver, 5)
# input_name = wait2.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"username-field")]/input[id="TPL_username_1"]')))
# input_name.send_keys('13523823288')
# wait3 = WebDriverWait(driver, 5)
# input_password = wait3.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"pwd-field")]/input[id="TPL_password_1"]')))
# input_password.send_keys('ZHJ1995369369')

input_name = browser.find_element_by_xpath(
    '//form[@id="J_Form"]/div[contains(@class,"username-field")]/input[@id="TPL_username_1"]')
input_name.send_keys('13523823288')
sleep(1)
input_password = browser.find_element_by_xpath(
    '//form[@id="J_Form"]/div[contains(@class,"pwd-field")]//input[@id="TPL_password_1"]')
input_password.send_keys('ZHJ1995369369')
# browser.close()
sleep(1)
while True:
    try:
        # 定位滑块元素,如果不存在，则跳出循环
        show = browser.find_element_by_xpath("//*[@id='nocaptcha']")
        showval = show.value_of_css_property("display")
        if not show.is_displayed():
            break
        source = browser.find_element_by_xpath("//*[@id='nc_1_n1z']")
        sleep(3)
        # 定义鼠标拖放动作
        # ActionChains(driver).drag_and_drop_by_offset(source,400,0).perform()
        # driver.save_screenshot('login-screeshot-11.png')
        action = ActionChains(browser)
        sleep(1)
        action.click_and_hold(source).perform()
        for index in range(20):
            try:
                action.move_by_offset(2, 0).perform()  # 平行移动鼠标
                # browser.save_screenshot('login-screeshot-i-'+str(index)+'.png')
            except Exception as e:
                print(e)
                break
            if (index == 19):
                action.release()
                sleep(1)
                # browser.save_screenshot('login-screeshot-i-'+str(index)+'.png')
            else:
                sleep(0.01)  # 等待停顿时间
                # sleep(0.1)
        # print(show.get_attribute("outerHTML"))
        sleep(2)
        # browser.save_screenshot('login-screeshot-0.png')
        # 查看是否认证成功，获取text值 //*[@id="nc_1__scale_text"]/span
        text = browser.find_element_by_xpath("//*[@id='nc_1__scale_text']/span")
        if text.text.startswith(u'验证通过'):
            print('成功滑动')
            break
        if text.text.startswith(u'请点击'):
            print('成功滑动')
            break
        if text.text.startswith(u'请按住'):
            continue
    except Exception as e:
        print(e)
        browser.find_element_by_xpath("//div[@id='nocaptcha']/div/span/a").click()
browser.find_element_by_xpath("//*[@id='J_SubmitStatic']").click()
sleep(2)
