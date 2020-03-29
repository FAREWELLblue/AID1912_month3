from flask import Flask,render_template,session,request
from flask_socketio import SocketIO,emit
from chat_db import Database
import datetime
import json
import time

app=Flask(__name__)
app.config['SECRET_KEY'] = '123456'
db=Database()
socketio=SocketIO(app)

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
    if request.method=="GET":
        if session.get('username'):
            if request.args.get('req')=='room_list':
                room_list=json.dumps(db.query_room_list())
                print(room_list)
                if room_list:
                    data = json.dumps({'code':'1',"data":room_list,'user':session.get('username')})
                else:
                    data = json.dumps({'code':'0','data':'null','user':session.get('username')})
            else:
                data = json.dumps({'code':'200','user':session.get('username'),'room':session.get('rname')})
        else:
            data = json.dumps({'code':'404','data':{"msg":"没有登录"},})
            
    elif request.method=="POST":
        r_name=request.json.get("r_name")
        r_intro = request.json.get('r_intro')
        owner=session.get('username')
        # print(owner,'创建',r_name,'简介',r_intro)
        if db.insert_chat_room(r_name,r_intro,owner):
            data = json.dumps({"code":'1','msg':'创建完成'})
        else:
            data = json.dumps({"code":'0','msg':'创建失败'})
    return data
            

@app.route('/chat_room',methods=["post",'get'])
def chat_room():
    if request.method=='GET':
        session['rname']=request.args.get('rname')
        return render_template('room.html')
    elif request.method=='POST':
        if request.json.get('msg')=='say':
            time_now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
            u_name=request.json.get('user')
            mes=request.json.get('message')
            r_name=request.json.get('r_name')
            print(u_name,mes,time_now,r_name)
            if db.insert_chat_record(u_name,mes,time_now,r_name):
                data = json.dumps({'code':'11','msg':"发送成功"})
            else:
                data = json.dumps({'code':'40','msg':"发送失败"})
        elif request.json.get('msg')=='read':
            r_name=request.json.get('rname')
            print('room-name----------',r_name)
            records=db.query_chat_record(r_name)
            if records:
                records=list(map(list,records))
                for record in records:
                    for item in record:
                        if isinstance(item,datetime.datetime):
                            item = item.strftime('%Y-%m-%d %H:%M:%S')
                            del record[-1]
                            record.append(item)
                print(records)
                data=json.dumps({'code':'12','data':records})
            else:
                data=json.dumps({'code':'42','msg':'无聊天记录'})
        else:
            data=json.dumps({'code':'41','msg':'无法识别ajax代码'})
        return data
        

@app.route('/logout')
def logout():
    session['username']=None
    return json.dumps({'code':"1",'msg':"已删除session中username"})

# @socketio.on('/join')
# def on_join(data):
#     username=data['username']


if __name__ == '__main__':
    # app.run(debug=True,host="127.0.0.1")
    socketio.run(app,debug=True,host="192.168.0.189")
