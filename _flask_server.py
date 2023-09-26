from flask import Flask, request, jsonify
import os
import time
import sys

app = Flask(__name__)
def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)
    print('Restart')

# 이미지를 저장할 디렉토리 설정
UPLOAD_FOLDER = '/home/air-020/IG'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        print('connect')
        # 업로드된 이미지를 저장
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))

        return jsonify({'message': 'File uploaded and processed successfully'}), 200

if __name__ == '__main__':
    try:
        m_n =19073
        app.run(host='192.168.229.227', port=m_n)
    except:
        time.sleep(1)
        restart()



