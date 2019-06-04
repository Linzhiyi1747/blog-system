from flask import Flask,render_template,request,redirect,url_for,session
import MySQLdb
import os
from datetime import timedelta
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24) 
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1) 
db = MySQLdb.connect("localhost", "work", "work1234", "blog", charset='utf8' ) #建立数据库连接
cursor = db.cursor()

#index和home要合并，用if

#登录前首页
@app.route('/', methods=['GET', 'POST'])   
def index():
    return render_template('index.html')

#登录后首页
#记得在前面加上转换器，固定变量类型
@app.route('/home/<user_name>/', methods=['GET', 'POST'])   
def home(user_name):
    return render_template('home.html')

#注册
@app.route('/register/',methods=['GET','POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	else:
		username = request.form['username']
		password = request.form['password']
		'''
		1. 检查重名 :
		if : 
			return '<h3>用户已存在</h3>'  
		else：
		可以在模版里写 JavaScript
		'''
		sql = 'INSERT INTO users(usernames,passwords) VALUES (%s,%s)'
		cursor.execute(sql,[username,password])
		db.commit()
		db.close()
		'''注册成功？：
                1. button那儿加一个onclick="miao() ，自己设定函数，当..TRUE才提交表单
                2. 页面跳转：https://blog.csdn.net/qq_36803558/article/details/81333691
				'''
		return redirect(url_for('index'))
		
#登录
@app.route('/signin/',methods=['GET','POST'])
def signin():
	if request.method == 'GET':
		return render_template('signin.html')
	else:
		username = request.form['username']
		password = request.form['password']
		sql = 'select count(usernames) from blog.users\
		where usernames = %s and passwords = %s'
		cursor.execute(sql,[username,password])
		results = cursor.fetchall()
		db.commit()
		db.close()
		if results[0][0] == 0:
		    return '用户名或密码错误！'#做一个页面
		else:
		    session['user'] = username
		    session.permanent = True
		    #弹出登陆成功
		    return redirect(url_for('home',user_name=username))
'''		
#注销用户
@app.route('/logout)		
def logout():
	session.clear()
	return redirect(url_for('index'))
'''

if __name__ == '__main__':
    app.run()
