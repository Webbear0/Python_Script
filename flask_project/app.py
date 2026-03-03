#coding=utf-8
#功能：Flask创建网页

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
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/docs.html')
def docs():
    return render_template('docs.html')

@app.route('/download.html')
def download():
    return render_template('download.html')

# 启动web应用程序 开启debug
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)
