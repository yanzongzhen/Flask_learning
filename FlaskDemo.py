from flask import Flask
from flask import render_template
from flask import request,redirect,url_for,flash
import os

base_path = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

#数据分析
def userPrase():
    with open(os.path.join(base_path, 'userinfo.txt'),'r') as f:
        data = f.read().split('\n')
        for i in data:
            user = i.split('|')
            yield{
                "name":user[0][4:],
                "password":user[1][3:]
            }

def loginAuth(name,pw):
    for i in userPrase():
        if name == i['name'] and pw == i['password']:
            return True

@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    return render_template("index.html",name=name )

#login
@app.route('/login/')
def Login_page_handler():
    return render_template("login.html")

@app.route('/user/login/',methods=['POST','GET'])
def Login_handler():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        response = loginAuth(name,password)
        if response == True:
            return redirect(url_for('hello_world',name=name))
        else:
            return redirect(url_for('Register_page_handler'))
#register
@app.route('/register/')
def Register_page_handler():
    return render_template("register.html")

@app.route('/user/register/',methods=['POST','GET'])
def Register_handler():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        chilpw = request.form['chil-pw']

        with open(os.path.join(base_path, 'userinfo.txt'), 'a') as f:
            f.write("用户名:%s|密码:%s\n" % (name, password))
            f.close()
        return redirect(url_for('Login_page_handler'))


if __name__ == '__main__':
    app.run(debug=True)
