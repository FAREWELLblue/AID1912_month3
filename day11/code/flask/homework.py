from flask import Flask,request,render_template

# template_folder = "templates"
# 模板就是包含了特殊语法的html
# Flask中所有的模板默认放在templates目录中 如果templates目录没有制定,需要手动创建
# 自定义模板目录 在文件中修改模板目录后 记得在目录结构中创建相对应的目录
# static_folder="static"静态目录
app=Flask(__name__)

@app.route('/')
def index_view():
    return render_template('homework.html')

@app.route('/test')
def test_view():
    level = request.args.get('level')
    print(level)
    if level=='all':
        return '全部难度的内容'
    elif level=='easy':
        return '初级难度的内容'
    elif level=='mid':
        return '中级难度的内容'
    elif level=='hard':
        return '高级难度的内容'
    else:
        return "获取数据失败"

if __name__ == '__main__':
    app.run(debug=True,host='192.168.0.189')