from flask import Flask,request

app = Flask(__name__)

# 访问127.0.0.1:5000/ 显示这是项目的首页
# 访问127.0.0.1:5000/detail 显示这是项目的详情页面
@app.route('/')
@app.route('/index')
def index_view():
    url='<a href = "/detail">detail</a>'
    return f'项目的首页,{url}'

@app.route('/detail')
def detail_view():
    return '项目的详情页面'

@app.route('/show/<uname>/<int:age>')
def show_view(uname,age):
    return f'hello,{uname}{age}'

@app.route('/server',methods=['POST','GET'])
def server():
    # 接收前端提交的数据并显示
    # 通过request对象接收get请求
    # print(request.args)
    # print(request.args['uname'])# 通过键索引值
    # uname=request.args['uname']

    # 接收POST请求提交的数据
    # print(request.form)
    # uname=request.form['uname']
    uname=request.form.get('uname','')
    return f'欢迎{uname}'


if __name__ == '__main__':
    app.run(debug=True)