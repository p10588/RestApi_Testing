from flask import Flask

# 创建 Flask 应用程序实例
app = Flask(__name__)

# 创建一个路由，定义页面的访问路径和处理函数
@app.route('/webhook')
def hello_world():
    return 'Hello, World!'

# 如果这个脚本被直接运行，而不是作为模块导入，启动 Flask 服务器
if __name__ == '__main__':
    app.run()