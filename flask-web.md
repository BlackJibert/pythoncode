## web开发基础

## Flask的Hello World

## Flask的模板

## Flask的消息提示与异常处理



## web开发基础

- 前端知识
- Git与Github
- MVC设计模式
- HTTP协议

前端开发基础

- HTML
- CSS
- JavaScript

前端常用的库与框架

Bootstrap

jquery

angularjs

React



代码管理

MVC设计模式

1、View视图

2、Controller控制器

3、MOdel模型

HTTP协议（超文本协议）

- 基于请求与响应模式
- 无状态

HTTP请求方法

- GET
- POST
- DELETE
- PUT





--------------------------------------

## 2、Flask中的Hello  World

1、Flask应用的基本构成

2、Flask的路由

3、Flask的反向路由

from flask import Flask

app = Flask(__name__)

@app.route('/')

deff hello_world():
	return 'hh'

@app.route('/users',methods=['POST'])

def hello_user:

​	return 'hello user'

@app.route('/users/<id>',methods=['POST'])

def hello_user(id):

​	return 'hello user'+id

@app.route('/query_user')

def query_user():
	id = request.args.get('id')

​	return 'query  user:'+id



- 反向路由 

@app.route('query_url')

def query_url():
	return 'query url:'+url_for('query_user')



if __name__ = '__main__':

​		app.run()





## Flask 模板

1、模板的简单使用

2、条件语句

3、循环语句

4、模板的继承



mitsuhiko

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def hello_world():

​	

​	return render_template('index.html',content = content)



if __name_=='__main__'

​	app.run()

