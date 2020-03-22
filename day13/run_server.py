from flask import Flask,render_template,request
import json
app=Flask(__name__)

@app.route('/cross_server')
def cross_server():
    fun = request.args.get('callback')
    data = {"code":200,"msg":"ok"}
    print(fun+"("+json.dumps(data)+")")
    return fun+"("+json.dumps(data)+")"

# 在run.py中定义路由和视图函数
# 要求访问http://127.0.0.1:500/cross时能看到cross.html
# 在cross.html中,向http://127.0.0.1:5001/cross_server发送get请求获取结果




if __name__ == "__main__":
    #http://127.0.0.1:5001
    app.run(debug=True,port=5001)