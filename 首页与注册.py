from flask import Flask,render_template,request,redirect,url_for,session
import MySQLdb

app = Flask(__name__)
db = MySQLdb.connect("localhost", "work", "work1234", "blog", charset='utf8' ) #建立数据库连接
cursor = db.cursor()

#首页
@app.route('/', methods=['GET', 'POST'])   
def home():
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
		2. 另一种更方便的数据库连接方式
		user = 
		db.session.add(user)
		db.session.commit()
		'''
		sql = 'INSERT INTO users(usernames,passwords) VALUES (%s,%s)'
		cursor.execute(sql,[username,password])
		db.commit()
		db.close()
		return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
