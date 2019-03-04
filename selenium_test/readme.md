# selenium是一个自动化测试工具，利用它可以驱动浏览器执行特定的动作，如点击，下拉等操作，同时
还可以获取浏览器当前呈现的页面的源代码，做到可见即可爬

## 1、访问页面
"""
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()
"""
- 我们就获取了淘宝页面的源代码，随后浏览器关闭


## 2、查找结点

## 3、节点交互
selenium 驱动浏览器执行一些操作，让浏览器模拟一些动作：
   输入文字，send_keys()方法
   清空文字，clear()方法
   点击按钮，click()方法
   睡眠，sleep()\
   利用查找节点找到找到输入框，然后输入文字，接着找到按钮的节点，接着点击

## 4、动作链
比如：鼠标拖曳，键盘按键等
将一个节点从一处拖到另外一处

- 动作链文档：
    http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains

## 5、执行JavaScript
对于某些操作，Selenium API并没有提供，比如，下拉进度条，他可以直接模拟运行JavaScript，此时使用execute_script()方法即可实现

"""
from selenium import webdriver

    browser =webdriver.Chrome()
    browser.get("http://www.zhihu.com/explore")
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    browser.execute_script('alert("To Bottom")')

"""
## 6、获取节点信息
在通过page_source属性可以获取网页的源代码，接着就可以使用解析库（正则，BS,pyquery）,
同时selenium 也提供了选择节点的方法，返回的是WebElement类型。

### 6.1获取属性值
先找到这个节点，然后通过get_attribute('class'),就可以获取它的值

### 6.2获取文本值

bs的是get_text()
pyquery是text()
WebElement也是text属性

先找到这个节点，然后.text()就行了

# 6.3 获取id,位置，标签名和大小
.id
.location
.tag_name
.size

# 6.4 切换Frame

网页中有一种节点叫做iframe，也就是字Frame，相当于页面的子页面，它的结构和外部网页的结构完全一致。selenium打开页面后，默认是在
父级Frame里面操作，此时如果页面中还有子Frame,它是不能获取到子Frame里面的节点的。需要使用switch_to.frame()方法来切换Frame

## 6.5 延时等待
在selenium中，get方法会在网页框架加载结束后结束执行，此时如果获取page_source，可能并不是浏览器完全加载完成的页面，如果某些页面有额外的Ajax请求，
我们在网页源码中也不一定能成功获取到，所以，我们需要延时等待一定时间。

- 隐式等待
    当查找节点没有立即出现的时候，隐式等待一段时间再查找DOM，默认的时间是O

from selenium import webdriver
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('http://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)

- 显式等待
他指定要查找的节点，然后指定一个最长等待的时间。如果在规定的时间内加载出来了这个节点，就返回查找的节点；如果到了规定时间依然没有
加载出来该节点，就会抛出超时异常。
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))

button =wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)

关于等待条件，还有很多，比如判断标题内容，判断某个节点内是否出现了某文字，表7-1列出了所有的等待条件


## 前进和后退

平时用浏览器都有前进和后退，selenium 也可以完成这个操作，它使用了back()方法后退，使用forward()方法前进。

import time
from selenium import webdriver

browser = webdriver.Chrome()
#连续访问3个界面
browser.get("https://www.baidu.com")
browser.get("https://www.taobao.com")
browser.get("http://www.w3school.com.cn/css/index.asp")

browser.back()
time.sleep(1)
browser.forward()
browser.back()
browser.close()


# 6.7 Cookies
使用selenium 可以方便的对Cookies进行操作，例如获取、添加、删除Cookies等，示例如下：
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name': 'name', 'domin': 'www.zhihu.com', 'value': 'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())

#6.8 选项卡管理

在访问网页的时候，会开启一个个选项卡，在selenium中，我们也可以对选项卡进行操作

import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
browser.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://python.org')

#6.9 异常处理

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

    