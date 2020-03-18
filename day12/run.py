from flask import Flask,render_template,request
import json

app=Flask(__name__)
7
@app.route('/')
def index():
    return render_template('homework.html')

@app.route('/server')
def server():
    kw=request.args.get('kw')
    search_list=['历史','简介','官网','发展前景']
    data=''
    for i in search_list:
        data+=kw+i+'|'
    return data

# @app.route('/post')
# def post():
#     return render_template('ajax_post.html')

# @app.route('/post_server',methods=["POST"])
# def post_server():
#     #接收post请求中携带的参数
#     print(request.form)
#     uname = request.form.get('uname')
#     print(uname)
#     return f'hello,{uname}'

@app.route('/post',methods=['GET','POST'])
def post_server():
    # 如果用户直接访问127.0.0.1:5000/post (get)将页面显示给用户
    # 如果用户在页面中点击发送post请求 处理请求中的数据并发挥结果.
    if request.method=='GET':
        return render_template('ajax_post.html')
    elif request.method=='POST':
        uname=request.form.get('uname')
        return f'欢迎,{uname}'

@app.route('/getData')
def get_data():
    return render_template('getData.html')

@app.route('/getData_server')
def getData_server():
    #元组 (data,status)
    #The tuple must have the form (body, status, headers), (body, status), or (body, headers)
    # return ('Lily','maria','QTX',200)

    # flaks允许的响应类型有  字符串  字典  元组  和其他封装好的响应类型
    # 字典是flask1.1.1版本新增的允许传递的类型
    # 元组是指flask返回值时的参数可以用元组的方式添加 但是数据不能是定义元组
    # lis=["laowang","Maria","QTX"]
    # 将列表转换成符合JSON格式的字符串
    # data=json.dumps(lis)
    dic={"uname":"laowang","age":18}
    # separators参数表示转成JSON串以后的分割符,默认键值对之间用', '分割,键和值之间用': '分割
    # 如果不需要无意义的空格时,可以制定一个元素(',',':')替换默认值
    data = json.dumps(dic,separators=(',',':'),sort_keys=True)
    
    return data

@app.route('/exer2')
def exer2_view():
    return render_template('exer2.html')

@app.route('/exer2_server',methods=['GET'])    
def exer2_server():
    uname=request.args.get('uname')
    user_list=['Lily','Bob']
    if uname in user_list:
        data = json.dumps({'code':1000,'msg':'用户名已存在'})
    else:
        data = json.dumps({'code':1001,'msg':'OK'})
    return data

@app.route('/register',methods=["POST"])
def register():
    print(request.json)
    uname = request.json.get('uname')
    pwd = request.json.get('pwd'
    print(uname,pwd)
    return 'OK'

# @app.route('/data')
# def data():
    

if __name__ == "__main__":
    app.run(debug=True) 