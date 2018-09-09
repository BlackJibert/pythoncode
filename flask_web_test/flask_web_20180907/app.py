from flask import Flask,render_template
from models import User
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

#传递参数
@app.route('/user')
def hello_user():
    user = User(1, "ZHJ")
    return render_template("user_index.html", user=user)

#条件语句
@app.route('/query_user/<user_id>')
def query_user(user_id):
    user=None
    if int(user_id) == 1:
        user = User(1, 'zhj')
    return render_template("user_id.html", user=user)

#循环语句
@app.route('/users')
def user_list():
    users=[]
    for i in range(1,11):
        user =User(i,'zhj'+str(i))
        users.append(user)
    return render_template("user_list.html",users= users)

#模板继承
@app.route('/one')
def one_base():
    return render_template("one_base.html")

@app.route('/two')
def two_base():
    return render_template("two_base.html")

if __name__ == '__main__':
    app.run()
