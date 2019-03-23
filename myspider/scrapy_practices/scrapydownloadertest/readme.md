#这个测试是关于Downloader Middleware的用法

Downloader Middleware的功能十分强大，修改User-Agent,处理重定向，设置代理，失败重试，设置
Cookies等功能都需要借助它实现

每个Downloader Middlerware都定义了一个或多个方法，核心的方法右如下三个：
- process_request(request, spider)
- process_response(request, response,spider)
- process_exception(request, exception, spider)

我们只需要实现至少其中一个方法，就可以定义一个Downloader Middleware。

这里我们是新建了一个项目，scrapydownloadertest
在middlewares.py中添加了一个新的RandomUserAgentMiddlewarede 类用于修请求时的User_Agent 这种方法比较灵活
我们还在这个类中添加了process_response用于修改Response的状态码