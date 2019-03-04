# 获取源码
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# from selenium.webdriver.support import expected_conditions as EC
#
# from selenium.webdriver.support.wait import WebDriverWait
#
# browser = webdriver.Chrome()
# ##
# # browser = webdriver.PhantomJS()
#
# try:
#     browser.get('http://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     #获取当前URL
#     # print(browser.current_url)
#     #获取当前的cookies
#     # print(browser.get_cookie)
#     #获取源代码
#     print(browser.page_source)
# finally:
#     browser.close()

# 2、下拉进度条
# from selenium import webdriver
#
# browser =webdriver.Chrome()
# browser.get("http://www.zhihu.com/explore")
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

# 3、切换Frame

# import time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# #切换到子Frame
# browser.switch_to.frame('iframeResult')
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print("NO LOGO")
#
# #返回到父级Frame
# browser.switch_to.parent_frame()
#
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)

# 4、隐式等待
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('http://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)


# 5 显式等待
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
#
# button =wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)

# 6 前进和后退
#
# import time
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# #连续访问3个界面
# browser.get("https://www.baidu.com")
# browser.get("https://www.taobao.com")
# browser.get("http://www.w3school.com.cn/css/index.asp")
#
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.back()
# browser.close()

# 7对Cookies进行操作
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domin': 'www.zhihu.com', 'value': 'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

# 8 选项卡管理
#
# import time
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to.window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to.window(browser.window_handles[0])
# browser.get('https://python.org')

# 9 异常处理

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print("Time Out")
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print("No Element")

finally:
    browser.close()
