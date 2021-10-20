from flask import Flask, render_template

app =Flask(__name__);

@app.route("/")
def index():
    return render_template("index.html",template_variable = "KD", template_num = 100, template_dict={1:'01',2:'02',3:'03'})

@app.route("/home")
def what():
    return '''<h1>LEE KD</h1>
    <a href="http://localhost:8080/">home</a>
    '''

@app.route("/detect")
def detect():
    return '''<h1>What is this?</h1>
    <a href="http://localhost:8080/">home</a>
    '''

@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'Hello, {user_name}({user_id})~'

if __name__ == '__main__':
    app.run(port=8080,debug=True)