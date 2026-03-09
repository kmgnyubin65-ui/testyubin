from flask import Flask, send_from_directory
import os

# Flask 애플리케이션 생성
app = Flask(__name__)

# HTML 파일이 저장된 폴더 경로 설정 (htmls 폴더)
HTML_FOLDER = 'htmls'

@app.route('/')
def index():
    """
    메인 페이지 접속 시 htmls/index.html 파일을 반환합니다.
    """
    return send_from_directory(HTML_FOLDER, 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    """
    추가적인 정적 파일(이미지, CSS 등)이 있을 경우를 대비한 경로 설정입니다.
    """
    return send_from_directory(HTML_FOLDER, path)

if __name__ == '__main__':
    # 서버 실행 (로컬 환경에서 테스트 가능)
    # 호스트를 0.0.0.0으로 설정하면 같은 네트워크의 다른 기기에서도 접속할 수 있습니다.
    print("나만의 룰렛 웹사이트 서버가 시작되었습니다!")
    print("브라우저에서 http://127.0.0.1:5000 접속하여 확인하세요.")
    app.run(host='0.0.0.0', port=5000, debug=True)
