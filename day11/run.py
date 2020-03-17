from flask import Flask,render_template,request

# templates 默认模板目录  放页面的
# static 默认静态资源目录 放img/css/js..等
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('exer2.html')



# 当用户访问127.0.0.1:5000/demo时   给用户显示页面demo1.html
@app.route('/demo')
def demo_view():
    return render_template('demo1.html')

@app.route('/server')
def server():
    return '接收前端AJAX请求成功'

@app.route('/exer_server',methods=['GET'])    
def exer_server():
    uname=request.args.get('uname')
    return f"hello,{uname}"

@app.route('/exer2_server',methods=['GET'])    
def exer2_server():
    uname=request.args.get('uname')
    user_list=['Lily','Bob']
    if uname in user_list:
        return 'Fail'
    else:
        return 'OK'
if __name__ == "__main__":
    app.run(debug=True,host="192.168.0.189")
