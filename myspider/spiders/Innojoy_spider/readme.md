#爬取网站：http://www.innojoy.com/search/index.html
#前提条件：
    在弹出的小框内（子frame）进行登录，然后才可以进行搜索专利
    这里面有两层frame,使用switch_to.frame()来切换到子frame里面

#出现问题：
1、两层frame的跳转
2、异常：StaleElementReferenceException 的处理：
    参考：https://blog.csdn.net/zby_hlx/article/details/79552357

