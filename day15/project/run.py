from flask import Flask,render_template,request
import json,time


app=Flask(__name__)

@app.route('/')
def index_view():
    return render_template('index.html')

@app.route('/data')
def get_data():
    size=request.args.get('size')
    with open('comment.data') as f:
        data=json.loads(f.read())
        # 如果是第一次请求
        if not size:
            datas=data[:10]
        else:
            size=int(size)
            datas=data[size:size+10]

        if datas:
            return json.dumps({'code':200,'data':datas})
        else:
            return json.dumps({'code':201,'error':"没有语句了,别刷了,求你啦!"})
                

    # print(json.loads(data)[0])
    # for item in json.loads(data):
    #     if len(datas)<10:
    #         datas.append(item)
    # 打开文件comment.data读取里面的数据,将读取到的数据转成JSON格式的字符串
    # 将对象中的前10条数据取出 放入datas
    # json.loads 串转对象
    # return json.dumps({'code':200,'data':datas})

@app.route('/add',methods=['post'])
def add_data():
    username=request.json.get('username')
    content=request.json.get('content')
    print(username,content)
    with open('comment.data') as f:
        all_data=json.loads(f.read())
    with open('comment.data','w')as f:
        # {"num": 30, "username": "nnnnn ", "time": "2019-12-25 10:48:58", "content": "werlwjerfioeujtoehgoierhjgre"}
        new_data={
            'num':len(all_data),
            'username':username,
            'time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),
            'content':content
        }
        all_data.append(new_data)
        json_str=json.dumps(all_data)
        f.write(json_str)
    return json.dumps({'code':200,'msg':"内容发布成功"})


if __name__ == "__main__":
    app.run(debug=True)