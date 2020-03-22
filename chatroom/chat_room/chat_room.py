from flask import Flask,render_template,session,request
from chat_db import Database
import json

app=Flask(__name__)
app.config['SECRET_KEY'] = '123456'
db=Database()

@app.route('/')
def index_login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login',methods=["GET","POST"])
def login(): 
    if request.method=="GET":
        if session.get('username'):
            print('session.',session.get('username'))
            return render_template('/index.html')
        else:
            return render_template('/login.html')
    elif request.method=="POST":
        name=request.json.get('username')
        pwd=request.json.get('password')
        print(name,pwd)
        if db.login(name,pwd):
            session['username']=name
            return json.dumps({'code':'1',"msg":"登录成功"})
        else:
            return json.dumps({'code':'0',"msg":"用户名或密码错误"})

@app.route('/register',methods=["GET","POST"])
def register():
    if request.method=="POST":
        print(request.json.get("dur"))
        if request.json.get("dur")==0:# or request.json.get("dur")=='0':
            uname=request.json.get("uname")
            print(uname)
            d=db.register(uname,'')
            if d:
                data = json.dumps({"code":1,"msg":"用户名可以使用"})
            else:
                data = json.dumps({"code":0,"msg":"用户名已存在"})

            return data
        else:
            print(request.json)
            uname=request.json.get("uname")
            pwd=request.json.get("password")
            email=request.json.get("email")
            print(uname,pwd,email)
            db.register(uname,pwd,email)
            return json.dumps({"code":200,"msg":"注册成功"})            
    elif request.method=="GET":
        return render_template('register.html')

@app.route('/room',methods=['GET','POST'])
def room():
    room_list=json.dumps(db.query_room_list())
    print(room_list)
    if session.get('username'):
        if room_list:
            return json.dumps({'code':'1',"data":room_list,'user':session.get('username')})
        else:
            return json.dumps({'code':'0','data':'null','user':session.get('username')})
    else:
        return json.dumps({'code':'404','data':{"msg":"没有登录"},})

@app.route('/logout')
def logout():
    session['username']=None
    return json.dumps({'code':"1",'msg':"已删除"})

if __name__ == '__main__':
    app.run(debug=True,host="192.168.0.189")