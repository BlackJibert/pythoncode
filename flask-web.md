## web开发基础

## Flask的Hello World

## Flask的模板

## Flask的消息提示与异常处理



## 一、web开发基础

- 前端知识
- Git与Github
- MVC设计模式
- HTTP协议

#### 1、前端开发基础

- HTML
- CSS
- JavaScript

#### 2、前端常用的库与框架

Bootstrap

jquery

angularjs

React

####  3、代码管理

#### 4、 MVC设计模式

- View视图
- Controller控制器
- MOdel模型

#### 5、 HTTP协议（超文本协议）

- 基于请求与响应模式
- 无状态

#### 6、HTTP请求方法

- GET
- POST
- DELETE
- PUT





--------------------------------------

## 二、Flask中的Hello  World

- 1、Flask应用的基本构成
- 2、Flask的路由
- 3、Flask的反向路由

from flask import Flask

app = Flask(____name____)

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

​	app.run()



--------------------------------------------------------



## 三、Flask 模板

1、模板的简单使用

2、条件语句

3、循环语句

4、模板的继承

- flask的创作者：mitsuhiko

github首页：https://github.com/misuhiko

Jinjia2 模板引擎



from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def hello_world():

​	content = "hello world!"

​	return '<h1>helloworld</h1>'

​	return render_template('index.html',content = content)

if __name_=='__main__'

​	app.run()



在templates中创建模板index.html

在body中添加

​	{{ content }}



- 实际应用中，我们将user对象传给模板引擎
- 创建models.py

-------------------------------------------

models.py

class User(object):
	def __init__(self,user_id,user_name)

​		self.user_id = user_id

​		self.user_name = user_name

-----------------------------------

在app中

from models import User

------------------------------------

创建User模板user_index.html

在body中：

​	<h1> hello {{ user.user_name}}</h1>



----------------------------

创建新的路由

@app route('/user')

def user_index():
	user = User(1,"zhj")

​	return render_template("user_index.html",user = user)



---------------------------------------------------

### 条件语句

在前端传入一个user_id ,如果user_id 为1，就传回用户名，如果不是1，就传回不

存在这个用户，两个知识点：参数传递，模板中的条件语句。

- 1、先写一个路由

@app.route('/query_user/<user_id>')

def query_user(user_id):
	user =None

​	if int(user_id)==1:
		user =User(1,'zhj')

​	return render_template("user_id.html",user= user)



- 2、创建模板user_id.html

怎么书写条件语句呢？
在body中：

​	{%   if  user   %}

​		hello {{user.user_name}}

​	{% else %}

​		no this user

​	{% endif %}





-----------------------

### 循环语句

- 1、定义新的路由

@app.route('/users')

def user_list():
	users=[]

​	for i in range(1,11):
		user = User(i, 'jikexueyuan'+str(i))

​		users.appent(user)

​	return render_template("user_list.html",users = users)



- 2、 编写这个模板user_list.html

在body中，输出所有的用户：
使用：
	{%for user in users %}

​	{{user.user_id}}  {{user.user_name}}<br>

​	{%endfor%}  #用户结束循环



----------------------------

### 模板继承:

把不变的部分建成一个基类

- 1、 新建模板，base.html

在body中：

​	<div>

​		<h1>Header    zhj</h1>

​	</div>

​	中间变化的部分，我们定义为block：

​		{% block content%}

​		{% endblock %}

​	<div>

​		<h1>Footer    zhj</h1>

​	</div>

​	

由此，基类已经定义完成。

- 2、再创建一个子类 one_base.html

在子类中，首先要继承基类。

{% extend “base.html” %}

{%block content %}

​	<h2>这是第一页</h2>

{%endblock%}



定义第二个子类 two_base.html

{% extend “base.html” %}

{%block content %}

​	<h2>这是第二页</h2>

{%endblock%}



- 3、 定义路由

@app.route('/one')

def one_base():
	return render_template("one_base.html")



@app.route('/two')

def two_base():
	return render_template("two_base.html")

使用继承：实现了代码的复用，非常方便的。



## 四、Flask的消息提示与异常处理

  

三个知识点：

- 消息提示
- 抛出异常
- 异常处理



#### 1、消息提示

当在登陆时，需要输入用户名和密码，当这两者任意为空时，会提示“请输入账号”或者提示“密码不能为空”之类的。可能还会有验证码之类的。输入验证码之后，可能又会提示“用户名或者密码错误”，当我们每一步操作，出现了问题，系统都会提示。

在flask中，如何实现这样的功能呢？
flask中提供了消息闪现机制，方便我们在应用中进行消息提示。引入flask方法。

------------------------

##### （1）简单在页面实现消息提示消息提示

from flask import Flask,flash,render_template

@app.route('/')

def hello_world():

​	flash("hello zhj")

​	return render_teplate("index_find.html")



在配置消息提示时，我们需要配置 

​	app.secret_key = ‘123’

flask会使用它对消息进行加密



定义模板index_find.html，来输出消息提示。

在body中:

​	<h1>hello zyx</h1>

​	<h2>{{get_flashed_messages()[0]}</h2>

#其中，get_flashed_messages返回的是一个数组，我们只定义了一条消息，所以我们写0就好了。

---------------------------

##### （2） 模拟在浏览器出现消息提示（“用户名不存在”类似）

我们开始定义表单，模拟出客户操作出现的情况：

<form action="/login" method="post">

<input type="text" name="username">

<input type="password"  name="password">

<input type="submit"  value="Submit">

</form>

接着去编辑路由的逻辑：

我们需要调用前端表单传来的，引入request包

@app.route('/login',methos=['post'])

def login():
form = request.form

username = form.get('username')

password = form.get(password'')

if not username:
	flash("please input username")

​	return render_template('index_find.html')

if not password:

​	flash("please input password")

​	return render_template('index_find.html')



if username == 'zhj123' and password=='zhj123456' :

​	flash('login success')

else:

​	flash("username or password is wrong")

​	return render_template("index_find.html")

------------------------------------------------

#### 2、异常处理：

在flask中提供了装饰器来处理异常

@app.errorhandler(404)

def not_found(e):

​	return render_template("404.html")

###### 不太明白not_found(e)为什么会有个e呢？

去定义模板404.html:

在body中：

​	<h1>你要找的页面去火星了</h1>

​	<h2>抱歉，该页面不存在！</h2>

-------------------------------------------

#### 3、主动抛出异常

在应用中也可以主动抛出404异常，使用页面来捕获。

##### （1）定义路由：

@app.route('/users/<user_id>')

def users(user_id):
	if  int(user_id)==1:

​		return   render_template("user.html")

​	else:

​		abort(404)

##### （2）定义模板

定义模板user.html

在body：
	<h1>User exception</h1>



​	



​	























