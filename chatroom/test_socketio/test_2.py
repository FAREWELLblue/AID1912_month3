from flask import Flask,render_template,request
from flask_socketio import SocketIO,emit,join_room,leave_room
import time
async_mode=None

app=Flask(__name__)

socketio=SocketIO(app,async_mode=async_mode)
@app.route('/')
def index():
    return render_template('test2.html',async_mode=socketio.async_mode)

def sent():
    while True:
        time.sleep(5)
        emit('response',{'data':'自动发送的消息'})
@socketio.on('connect',namespace='/test')
def con():
    sent()

@socketio.on('form_sub',namespace='/test')
def test(message):
    print(message)
    emit('response',{'data':'接收成功'})
    
@socketio.on('join',namespace='/room')
def join(data):
    username=data['username']    
    room=data['room']
    print('-------------------------',room,username)
    join_room(room)
    emit('res',username +'is entered ',room=room)


if __name__ == "__main__":
    socketio.run(app,debug=True,host='192.168.0.189')