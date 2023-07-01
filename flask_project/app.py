#coding=utf-8
#功能：Flask创建网页
#编写者：俺

# 导入flask库的类 Flask
from flask import Flask,render_template

# 类的实例化
app=Flask(__name__)
# 定义路由
@app.route('/')
# 定义视图函数
def index():
    #返回html模板
    return render_template('index.html')

#定义子页面的路由及视图函数
@app.route('/page1')
def page1():
    return render_template('page1.html')

# 启动web应用程序 开启debug
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
