from flask import Flask,render_template,session,request

app=Flask(__name__)
app.config['SECRET_KEY'] = '123456'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login')
def login():
    name=request.args.get('name')
    print(name)
    session['name']=name
    return 'login success'

@app.route('/index')
def get_session():
    name=session.get('name')
    return name

if __name__ == '__main__':
    app.run(debug=True,host='192.168.0.189',port=8000)