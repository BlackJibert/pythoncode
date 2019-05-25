# 使用scrapy+selenium获取头条的内容

## 1、selenium向下操作滚动条

示例：

    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()---改变浏览器显示大小，没有滚动条没法滚动
    driver.get("https://www.toutiao.com/")
    driver.implicitly_wait(10)
    # driver.find_element_by_id("kw").send_keys("selenium")
    # driver.find_element_by_id("su").click()
    sleep(3)
    length = 1200
    #拖动到滚动条底部---向下
    for i in range(0, 10):
        js = "var q=document.documentElement.scrollTop="+str(length)
        driver.execute_script(js)
        sleep(2)
        if driver.find_element_by_xpath('//div[@class="refresh-mode"]'):
            driver.find_element_by_xpath('//div[@class="refresh-mode"]').click()
            # js = "var q=document.documentElement.scrollTop=" + str(length)
            # driver.execute_script(js)
        length += 200

- 解决方案：
    通过使用selenium执行js代码来模拟滚动条向下拉来更新内容，这里是通过向下拉10次

##2、selenium 破解滑动验证码
分为三步：
- 1、模拟点击验证码按钮
- 2、识别验证码缺口
- 3、模拟拖动验证码

    
- 参考：
（1）、https://blog.csdn.net/qq_42293590/article/details/83002040