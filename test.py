# driver = webdriver.Chrome()
# # driver = webdriver.Firefox()---改变浏览器显示大小，没有滚动条没法滚动
# driver.get("https://www.toutiao.com/")
# driver.implicitly_wait(10)
# # driver.find_element_by_id("kw").send_keys("selenium")
# # driver.find_element_by_id("su").click()
# sleep(3)
# length = 1200
# #拖动到滚动条底部---向下
# for i in range(0, 10):
#
#     js = "var q=document.documentElement.scrollTop="+str(length)
#     driver.execute_script(js)
#     sleep(2)
#     if driver.find_element_by_xpath('//div[@class="refresh-mode"]'):
#         driver.find_element_by_xpath('//div[@class="refresh-mode"]').click()
#         # js = "var q=document.documentElement.scrollTop=" + str(length)
#         # driver.execute_script(js)
#     length += 200
# #滚动左右滚动条---向右
# js2 = "var q=document.documentElement.scrollLeft=10000"
# driver.execute_script(js2)
# sleep(3)
# #滚动左右滚动条---向左
# js3 = "var q=document.documentElement.scrollLeft=0"
# driver.execute_script(js3)

# #控制滚动条逐步滚动
# for y in range(15):
#      js = "window.scrollBy(0,100)"
#      driver.execute_script(js)
#      sleep(1)
# scrollTo(x,y) 中，x为必须参数，表示要在窗口文档显示区左上角显示的文档的x坐标；y也为必须参数，表示要在窗口文档显示区左上角显示的文档的y坐标
# driver.execute_script("window.scrollTo(0,1000)")
# #滑动--- #  scrollBy(x,y)中，x为必须参数，表示向右滚动的像素值；y也为必须参数，表示向下滚动的像素值
# driver.execute_script("window.scrollBy(100,10000)")

# def debug(func):
#     def wrapper(*args,**kwargs):
#
#         print("entry:{}".format(func.__name__))
#         return func(*args,**kwargs)
#     return wrapper
# @debug
# def hello(someing):
#     print("hello {}".format(someing))
#
# hello("zhang")


# import time
# from random import randint
#
# for i in range(1, 35):  # 打印抬头
#     print('')
#
# heartStars = [2, 4, 8, 10, 14, 20, 26, 28, 40, 44, 52, 60, 64, 76]  # *的位置
# heartBreakLines = [13, 27, 41, 55, 69, 77]  # 空格的位置
# flowerBreakLines = [7, 15, 23, 31, 39, 46]  # 玫瑰的空列位置
#
#
# def addSpaces(a):  # 添加空列
#     count = a
#     while count > 0:
#         print(' ', end='')
#         count -= 1
#
#
# def newLineWithSleep():  # 添加空行
#     time.sleep(0.3)
#     print('\n', end='')
#
#
# play = 0
# while play == 0:
#     Left_Spaces = randint(8, 80)
#     addSpaces(Left_Spaces)
#     # print("比心心:", "\n")
#     for i in range(0, 78):  # 比心的形状
#         if i in heartBreakLines:
#             newLineWithSleep()
#             addSpaces(Left_Spaces)
#         elif i in heartStars:
#             print('*', end='')
#         elif i in (32, 36):
#             print('M', end='')
#         elif i == 34:
#             print('O', end='')
#         else:
#             print(' ', end='')
#
#     newLineWithSleep()
#     addSpaces(randint(8, 80))
#     print("H a p p y  M o t h e r ' s   D a y !", end='')
#     # print("\n", "献花花:")
#     newLineWithSleep()
#     newLineWithSleep()
#
#     Left_Spaces = randint(8, 80)
#     addSpaces(Left_Spaces)
#     for i in range(0, 47):  # 向母亲献花
#         if i in flowerBreakLines:
#             newLineWithSleep()
#             addSpaces(Left_Spaces)
#         elif i in (2, 8, 12, 18):
#             print('{', end='')
#         elif i in (3, 9, 13, 19):
#             print('_', end='')
#         elif i in (4, 10, 14, 20):
#             print('}', end='')
#         elif i in (27, 35, 43):
#             print('|', end='')
#         elif i in (34, 44):
#             print('~', end='')
#         elif i == 11:
#             print('o', end='')
#         else:
#             print(' ', end='')
#
#     print('\n', end='')  # 儿子给您的祝福

# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2019-05-07 00:20:48
# @Last Modified by:   gunjianpan
# @Last Modified time: 2019-05-07 22:34:22
#
# import js2py
# import re
#
# from util.util import basic_req, echo
#
# """
#   * 66ip @http
#     js decoder
# """
#
# IP66_URL = 'http://www.66ip.cn/'
# PRE_URL = '{}favicon.ico'.format(IP66_URL)
#
# header = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'Host': 'www.66ip.cn',
#     'Referer': 'http://www.66ip.cn/',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3785.0 Safari/537.36'
# }
#
#
# def generate_cookie():
#     ''' eval 66ip.cn test in 19.5.7 '''
#     req = basic_req(IP66_URL, 2, header=header)
#     basic_cookie = req.cookies.get_dict()
#
#     ''' !important \b in py -> \x80 '''
#     req_text = r'{}'.format(req.text)
#
#     ''' get the script will be eval '''
#     script_text = re.findall('<script>(.*?)</script>', req_text)[0]
#     script_text = script_text.replace(
#         '{eval(', '{aaa=').replace(');break', ';break')
#     script_eval = r'{}'.format(js2py.eval_js(script_text + 'aaa'))
#     echo(0, script_eval)
#
#     try:
#         ''' replace document & window '''
#         params = re.findall(
#             r'(__jsl_clearance=.*?)\'\+\(function\(\){(.*?join\(\'\'\))}\)\(\)', script_eval)
#         wait_eval = params[0][1].replace(
#             "document.createElement('div')", "{}").replace("", '')
#         wait_replace = re.findall(
#             r'=(.{1,5}\.firstChild\.href;)', wait_eval)[0]
#         wait_eval = wait_eval.replace(wait_replace, '"http://www.66ip.cn/";')
#
#         ''' eval & encoder cookie '''
#         other_param = js2py.eval_js(
#             'function ddd() {window={};' + wait_eval + '}ddd()')
#         cookie = '{}; {}{}'.format(encoder_cookie(
#             basic_cookie), params[0][0], other_param)
#         echo(1, 'cookie', cookie)
#
#         return cookie
#     except:
#         generate_cookie()
#
#
# def encoder_cookie(cookie_dict: {}) -> str:
#     return '; '.join(['{}={}'.format(ii, jj)for ii, jj in cookie_dict.items()])
#
#
# def req_ip66():
#     ''' 66ip.cn js decoder '''
#     header['Cookie'] = generate_cookie()
#
#     req_text = basic_req(IP66_URL, 3, header=header)
#     echo(2, req_text)
#     return req_text
#
#
# if __name__ == "__main__":
#     req_ip66()

# def check_is_admin(f):
#     def wrapper(*args, **kwargs):
#         if kwargs.get('username') != 'admin':
#             raise Exception("This user is not allowed to get food")
#         return f(*args, **kwargs)
#     return wrapper
#
# class Storage(object):
#     @check_is_admin
#     def get_food(self, username, food):
#         return Storage.get(food)
#     @check_is_admin
#     def put_food(self, username, food):
#         return Storage.put(food)

#
# def print_msg():
#     # print_msg 是外围函数
#     msg = "zen of python"
#     def printer():
#         # printer 是嵌套函数
#         print(msg)
#     return printer
# another = print_msg()
# another()

# a = ['hello', [1, 2, 3]]
# b = a[:]
# print([id(x) for x in a])
# print([id(x) for x in b])
#
# a[0] = 'world'
# a[1].append(4)
# print(a)
# print(b)

# a = ["adf",[1,2,4]]
# b = a[:]
# c = a[:]
# print(id(a), a)
# print(id(b), b)
# print(id(c), c)
#
# a[0] = "hello"
# print(id(a), a)
# print(id(b), b)
# print(id(c), c)


# import copy
# a = [1, 2, 3, 4, ['a', 'b']] #定义一个列表a
# b = a #赋值
# c = copy.copy(a) #浅拷贝
# # c = a[:]
# d = copy.deepcopy(a) #深拷贝
#
# a.append(5)
# print(a)
# #[1, 2, 3, 4, ['a', 'b'], 5] #a添加一个元素5
# print(b)
# #[1, 2, 3, 4, ['a', 'b'], 5] #b跟着添加一个元素5
# print(c)
# #[1, 2, 3, 4, ['a', 'b']] #c保持不变
# print(d)
# #[1, 2, 3, 4, ['a', 'b']] #d保持不变
#
# a[4].append('c')
# print(a)
# #[1, 2, 3, 4, ['a', 'b', 'c'], 5] #a中的list(即a[4])添加一个元素c
# print(b)
# #[1, 2, 3, 4, ['a', 'b', 'c'], 5] #b跟着添加一个元素c
# print(c)
# #[1, 2, 3, 4, ['a', 'b', 'c']] #c跟着添加一个元素c
# print(d)
# #[1, 2, 3, 4, ['a', 'b']] #d保持不变
#
# #说明如下：
# #1.外层添加元素时， 浅拷贝c不会随原列表a变化而变化；内层list添加元素时，浅拷贝c才会变化。
# #2.无论原列表a如何变化，深拷贝d都保持不变。
# #3.赋值对象随着原列表一起变化
