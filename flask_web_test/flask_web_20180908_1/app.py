from flask import Flask,flash,render_template,request,abort

app = Flask(__name__)
app.secret_key="123"

#1、简单在页面实现消息提示
@app.route('/')
def hello_world():
    # return 'Hello World!'
    # flash("I am zhj")
    return render_template("message_alert.html")
# @app.route('/')
#模拟在浏览器出现消息提示：
@app.route('/alert', methods=['POST'])
def login():
    form = request.form
    username = form.get('username')
    password = form.get('password')
    if not username:
        flash("please input usename")
        return render_template('message_alert.html')
    if not password:
        flash("please input password")
        return render_template("message_alert.html")

    if username == 'zhj123' and password == 'zhj123456':
        flash("login success")
        return render_template("message_alert.html")
    else:
        flash("username or password is wrong ")
        return render_template("message_alert.html")

#2、异常处理
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

#3、主动抛出异常
@app.route('/users/<user_id>')
def users(user_id):
    if int(user_id) == 1:
        return render_template("user.html")
    else:
        abort(404)
if __name__ == '__main__':
    app.run()
