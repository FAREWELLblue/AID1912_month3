from flask import Flask,render_template,request

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

if __name__ == "__main__":
    app.run(debug=True)