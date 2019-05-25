flask相比django更加灵活,可以随便选择扩展

## requirements 文件使用
一键安装在新环境中
1.输出,生成requirements.txt:
pip3 freeze >requirements.txt

2.安装
pip3 install -r requirements.txt

## Flask程序运行过程
1.当客户端想要获取资源时,一般会通过浏览器发起HTTP请求
2.此时,Web服务区会把来自客户端的所有请求都交给Flask程序实现
3.程序实例使用Werkzeug来路由分发(URL请求和 视图函数之间的对应关系)
4.根据每个URL请求,找到具体的视图函数并进行调用.
- 在Flask程序中,路由的实现一般是通过程序实例的装饰器来实现
5.Flask调用视图函数后,可以返回两种内容:
- 字符串内容
- HTML文档


##Jinja2模板引擎


