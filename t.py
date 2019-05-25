# import time
#
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.options import Options
#
# TB_LOGIN_URL = 'https://login.taobao.com/member/login.jhtml'
# # CHROME_DRIVER = './browser/chromedriver.exe'
#
#
# class SessionException(Exception):
#     """
#     会话异常类
#     """
#
#     def __init__(self, message):
#         super().__init__(self)
#         self.message = message
#
#     def __str__(self):
#         return self.message
#
#
# class SessionDriver:
#
#     def __init__(self):
#         self.browser = None
#
#     def get_session(self, username, password):
#         cookies = {}
#         try:
#             self.__init_browser()
#             self.__switch_to_password_mode()
#             time.sleep(0.5)
#             self.__write_username(username)
#             time.sleep(0.5)
#             self.__write_password(password)
#             time.sleep(0.5)
#             if self.__lock_exist():
#                 self.__unlock()
#             self.__submit()
#             # 提取cookie
#             for cookie in self.browser.get_cookies():
#                 cookies[cookie['name']] = cookie['value']
#         finally:
#             self.__destroy_browser()
#
#         return cookies
#
#     def __switch_to_password_mode(self):
#         """
#         切换到密码模式
#         :return:
#         """
#         if self.browser.find_element_by_id('J_QRCodeLogin').is_displayed():
#             self.browser.find_element_by_id('J_Quick2Static').click()
#
#     def __write_username(self, username):
#         """
#         输入账号
#         :param username:
#         :return:
#         """
#         username_input_element = self.browser.find_element_by_id('TPL_username_1')
#         username_input_element.clear()
#         username_input_element.send_keys(username)
#
#     def __write_password(self, password):
#         """
#         输入密码
#         :param password:
#         :return:
#         """
#         password_input_element = self.browser.find_element_by_id("TPL_password_1")
#         password_input_element.clear()
#         password_input_element.send_keys(password)
#
#     def __lock_exist(self):
#         """
#         判断是否存在滑动验证
#         :return:
#         """
#         return self.__is_element_exist('#nc_1_wrapper') and self.browser.find_element_by_id(
#             'nc_1_wrapper').is_displayed()
#
#     def __unlock(self):
#         """
#         执行滑动解锁
#         :return:
#         """
#         bar_element = self.browser.find_element_by_id('nc_1_n1z')
#         ActionChains(self.browser).drag_and_drop_by_offset(bar_element, 350, 0).perform()
#         time.sleep(0.5)
#         self.browser.get_screenshot_as_file('error.png')
#         if self.__is_element_exist('.errloading > span'):
#             error_message_element = self.browser.find_element_by_css_selector('.errloading > span')
#             error_message = error_message_element.text
#             self.browser.execute_script('noCaptcha.reset(1)')
#             raise SessionException('滑动验证失败, message = ' + error_message)
#
#     def __submit(self):
#         """
#         提交登录
#         :return:
#         """
#         self.browser.find_element_by_id('J_SubmitStatic').click()
#         time.sleep(0.5)
#         if self.__is_element_exist("#J_Message"):
#             error_message_element = self.browser.find_element_by_css_selector('#J_Message > p')
#             error_message = error_message_element.text
#             raise SessionException('登录出错, message = ' + error_message)
#
#     def __init_browser(self):
#         """
#         初始化selenium浏览器
#         :return:
#         """
#         options = Options()
#         # options.add_argument("--headless")
#         options.add_argument('--proxy-server=http://127.0.0.1:9000')
#         self.browser = webdriver.Chrome( options=options)
#         self.browser.implicitly_wait(3)
#         self.browser.maximize_window()
#         self.browser.get(TB_LOGIN_URL)
#
#     def __destroy_browser(self):
#         """
#         销毁selenium浏览器
#         :return:
#         """
#         if self.browser is not None:
#             pass
#             # self.browser.quit()
#
#     def __is_element_exist(self, selector):
#         """
#         检查是否存在指定元素
#         :param selector:
#         :return:
#         """
#         try:
#             self.browser.find_element_by_css_selector(selector)
#             return True
#         except NoSuchElementException:
#             return False
#
#
# def get_session(username, password):
#     return SessionDriver().get_session(username, password)
# get_session('13523823288','ZHJ1993569369')
# import re
# src = "security/afafsff/?ip=123.4.56.78&id=45"
# se = re.search('\d+.\d+.\d+.\d+', src).group()
# print(type(se))
# print(se)
# 先计算出和，然后循环每个数据，用和减去当前的数据 并除去2
# numbers = [1, 3, 5, 7, 7, 2, 4, 20]
#
# total = sum(numbers)
#
# fore = 0
# for number in numbers:
#    if fore < (total - number)/2:
#       fore += number
#    elif fore == (total - number)/2:
#        print(number)
#        break
#    else:
#        print('not found')
#        break
#
# li = [3, 3, 1, 2, 3]
# def main():
#      mid = len(li)/2
#      for l in li:
#          count = 0
#          i = 0
#          mark = 0
#          while True:
#              if l == li[i]:
#                  count += 1
#                  temp = i
#              i += 1
#              if count > mid:
#                  mark = temp
#                  return (mark,li[mark])
#              if i > len(li) - 1:
#                  break
#
# if __name__ == "__main__":
#     print(main())

# def dominate_point(a):
#     # set_b = (3,0)
#     set_b = set(a)
#     for set_value in set_b:
#         canditae_dominate = set_value
#         count = 0
#         for key, value in enumerate(a):
#             if canditae_dominate == value:
#                 count += 1
#             if count >= len(a)/2 and value == canditae_dominate:
#                 print("下标位置:", key) # 最后一些出现的位置
#                 print("出现最多的数", canditae_dominate)
#                 print("出现的次数", count)
# dominate_point([3,3,0,3,3,6])
# import requests
# data={
#     'name':"germey",
#     'age':22
# }
# r = requests.get('http://httpbin.org/get',params = data)
# print(r.text)
# import requests
# r= requests.get('https://github.com/favicon.ico')
# print(r.content)
# with open('favicon.ico','wb') as f:
#     f.write(r.content)

# import requests
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)
# print('-----------------')
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r2 = s.get('http://httpbin.org/cookies')
# print(r2.text)

# import requests
#
# data = {
#     'data: 106!s5mmc0clJSnH8BoHH6TzBl95kaySnj7JQzGhUUam0LHtKj4U56cmfrfC2y5bmPH7btxFTJoudp7PUjzSSwfWKM268SjAiHaFweyZo7EA+rSrmfsAymuMJ0kXwzXFCAZkKLN9b0l8U+cGUA9TUEIbHHm1O4rkysTJZcfMzd24GS1VOkpkRX91sx6uV8klx5/JPChB6mK5v7T9Lrjj6y/L46jj6E/dNVLH5uN+3UU7/uLU6q8H6yAKu617qvopzyGj/YDmxITHscVwnDKe9Pxd/mZdqv4IIHHw6rZppuiQsOMObG8PiVm0/M8e9X4IXTAh/X8jxuM2sxIhpqUSvxiP/Ew/ql5HXTLj4u2I6R6HQ5VbeSbwzd1B0aI0BECCm+BcVn413J7VAcHVKYPujFTNFKbHbRaskfGqNsIM51bOSNhYp7d0HmeRhSu0gvMTsTTc0CVxc7adFG5dCJogNQcXwepnzN1OyDXhEtxyDlSwNMZ7U6N2DyvI30z0WlgHbzLWJs5dEjCuCqyHuSZF+j17KvNaytvxZqwXcZMl+KQ9CL7HiCBBT8SpWX5YXi454A6G3EiQczt1+WTFLPY8+braAiiQDoJdSk/2vlA+FNViKfttuAommweuBhazDVV9IsO9eA2z7jnAph7M01MlH5lCFly+tNm+A0eFNaRszCLCSlRBxDv/xK2470RhEW5HFZHZn5PwhdAbyUD/dmKwBOX8ZSgLJsyW0s7Pl4pkE+2ovgOKUM7L9ppxV2ye2SFD1jDhLR3p4isvCw8ram=='
#     'xa': 'CF_APP_TBLogin_PC',
#     'xt': 'f68baf797e1a9277cc39a079b2f5555c6805b378',
#     'efy': '1',
# }
# s =requests.post('https://ynuf.aliapp.org/service/um.json', data=data)
# print(s.text)
# import requests
#
# proxy_host = 'http-dyn.abuyun.com'
# proxy_port = '9020'
# # 代理隧道验证信息
# proxy_user = 'HX2N4D0N26NDQ04D'
# proxy_pass = '9773B54281C83554'
#
# proxy_meta = 'http://%(user)s:%(pass)s@%(host)s:%(port)s'% {
#     'host': proxy_host,
#     'port': proxy_port,
#     'user': proxy_user,
#     'pass': proxy_pass
# }
# proxies={
#     'http': proxy_meta,
#     'https': proxy_meta,
# }
#
# re = requests.get('http://httpbin.org/get', proxies=proxies)
# print(re.status_code)

# # 连接数据库
# client = pymongo.MongoClient('mongodb://{0}:{1}@{2}:{3}'.format("admin", "admin123", '118.25.94.130', 27017))
# db = client['Tieba']
# table = db['tieba_2']
#
# # 读取数据
# data = pd.DataFrame(list(table.find()))
#
# # 选择需要显示的字段
# data = data[['title', 'author']]
#
# # 打印输出
# print(data)
# import requests
# headers = {
#     'Referer': 'https://item.jd.com/46047782510.html',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
#
# # res = requests.get('https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv282&productId=46047782510&score=0&sortType=5&page=21&pageSize=10&isShadowSku=0&rid=0&fold=1',headers=headers)
# res = requests.get("https://www.amazon.cn/s?k=python&page=2",headers=headers)
# print(res.text)
# comment = re.findall('{"productAttr":.*}', res.text)
# comm_dict = json.loads(comment[0])  # 将json对象obj解码为对应的字典dict
# print(comment)
# js_ = json.loads(comment[0])
# print(js_['comments'])
# for i in js_['comments']:
#     print(i)
# print(type(comment))
# id_ = re.search('\d+', 'https://item.jd.com/46611856075.html').group()
# print(id_)

A = [1, 2]
B = [A] * 5
print(B)
B[0][1] = 9
print(B)
