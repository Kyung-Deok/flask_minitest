from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm
from flask_pymongo import MongoClient
import time

app =Flask(__name__);
app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'
client= MongoClient('mongodb+srv://leekd:0914@test1.sqi24.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
#db 생성
db = client['miniproj']
#collection 생성
user_col = db['user_col']

@app.route("/")
def index():
    return render_template("index.html",template_variable = "KD", template_num = 100, template_dict={1:'01',2:'02',3:'03'})

@ app.route ( "/register", methods = [ "GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # 알람 카테고리에 따라 부트스트랩에서 다른 스타일을 적용(Success,danger)
        flash(f'{form.username.data} 님 가입완료', 'success')
        return redirect(url_for('index'))
    return render_template('register.html',form=form)

# @app.route('/user/<user_name>/<int:user_id>')
# def user(user_name, user_id):
#     return f'Hello, {user_name}({user_id})~'

if __name__ == '__main__':
    app.run(port=8080,debug=True)