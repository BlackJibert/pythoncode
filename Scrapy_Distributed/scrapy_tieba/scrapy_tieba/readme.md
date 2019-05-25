# 爬取贴吧的内容
## 策略
### 1、翻页策略
- 例如，这是某一页的：这是依据关键字‘python’搜索得到的最后一页：
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=46800
其中pn字段代表了总共有多少评论，而每一页有50条评论，因此我们可以得出评论内容大致分为了多少页
但是还有一个问题，那就是评论数都是整数吗？会不会最后一页的内容只有34条呢？
我们首先Request一下，返回首页的信息，里面包含了总的评论数，然后在另外的一个函数里面写请求，只要pn<总的评论数，继续循环


## 异常

## 1、关于爬取内容的异常
- 有些帖子发布的时候，内容为空（只有标题），所以我们在爬取的时候，会有异常出现，这是我们把标题置为标题

## 2、添加user-agent中间件的问题

    'scrapy_tieba.middlewares.RandomUserAgentMiddlewares': 400,

会抛出如下的异常：

    TypeError: expected string or bytes-like object
    不知道怎么解决，所以先行把设置的随机user-agent注释掉

# 3、无法获取时间，可能是需要selenium的助力