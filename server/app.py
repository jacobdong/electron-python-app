import os

from flask import Flask, send_file
import service.files as files

app = Flask(__name__)


@app.route('/')
def home():
    info = {
        "name": "starter_server",
        "version": "1.0.0"
    }
    return info


@app.route('/test')
def test():
    return {'info': 'info'}


@app.route('/image')
def get_image():
    # 这里替换为您实际的图片路径
    image_path = '__static/test.jpg'
    # 使用send_file函数发送图片文件
    return send_file(image_path, mimetype='image/png')


@app.route('/service')
def get_image_info():
    # 相对路径
    relative_path = '__static/test.jpg'
    # 获取入口程序所在的目录
    entry_dir = os.path.dirname(os.path.abspath(__file__))
    # 获取相对路径的绝对路径
    absolute_path = os.path.join(entry_dir, relative_path)

    print(f"入口文件地址：{entry_dir}")
    print(f"目标文件地址：{absolute_path}")
    return files.get_file_metadata(absolute_path)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=50000)
