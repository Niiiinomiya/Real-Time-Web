from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import subprocess


app = Flask(__name__)
CORS(app)  # 允许所有来源的跨域请求
app.static_folder = os.path.abspath('output')
@app.route('/uploadvideo', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'})

    # 保存文件到指定位置
    upload_folder = 'uploads/'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = os.path.join(upload_folder, 'video.mp4')
    file.save(file_path)

    return jsonify({'message': 'Video uploaded successfully', 'file_path': file_path})

@app.route('/uploadimg', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'})

    # 保存文件到指定位置
    upload_folder = 'uploads/'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = os.path.join(upload_folder, 'img.jpg')
    file.save(file_path)

    return jsonify({'message': 'Image uploaded successfully', 'file_path': file_path})


@app.route('/generate-video', methods=['POST'])
def generate_video():
    command = "python image_animation.py -i uploads/img.jpg -c checkpoints/taichi-cpk.pth.tar -v uploads/video.mp4"
    subprocess.call(command, shell=True)
    return jsonify({'message': 'video generate successfully'})


@app.route('/getvideo', methods=['GET'])
def get_video():
    output_file = os.path.abspath('output/testfront.avi')
    return send_file(output_file, as_attachment=True)
if __name__ == '__main__':
    app.run(host='localhost', port=8080)