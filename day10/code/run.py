from flask import Flask

# 将当前模块构建成flask应用 flask应用可以接收客户端(浏览器)请求 并给出响应
# B/S架构
app = Flask(__name__)

#http://127.0.0.1:5000/
#@app.route表示路由 通过路由来匹配请求的地址 然后根据不同的地址选择不同的视图函数处理请求
@app.route('/')
def index_view():
    '''
        视图函数    处理前端浏览器发送的请求 将处理的结果响应给浏览器
        响应的结果是通过视图函数的return语句返回给浏览器的,所以视图函数必须要有返回值
        视图函数都是唯一的,不能重名
    :return:
    '''
    return '<h1>这是我的第一个flask应用</h1>'

if __name__ == "__main__":
    #如果当前模块是在主程序中运行,
    # 调用run()函数
    # run函数会通过flask应用启动一个自带的小型web服务器,仅供测试和开发阶段使用,项目上线后需要替换成专业的web服务器
    # 默认的服务器的地址是从127.0.0.1:5000启动,可以使用传参的方式修改ip地址和端口号
    # run(host=None,port=None,,debug=None)
    app.run(debug=True)
