import streamlit as st
import streamlit.components.v1 as components
import os

# 페이지 설정 (타이틀 및 아이콘)
st.set_page_config(page_title="나만의 룰렛 사이트", page_icon="🎡", layout="wide")

def main():
    # HTML 파일이 저장된 경로 설정
    # 현재 실행 파일(app.py) 위치를 기준으로 htmls/index.html 경로를 찾습니다.
    current_dir = os.path.dirname(__file__)
    html_path = os.path.join(current_dir, "htmls", "index.html")

    try:
        # index.html 파일 읽기
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Streamlit 화면에 HTML 구성 요소 삽입
        # 높이(height)는 룰렛 판이 충분히 보이도록 800px 정도로 설정했습니다.
        components.html(html_content, height=900, scrolling=True)

    except FileNotFoundError:
        st.error(f"오류: '{html_path}' 파일을 찾을 수 없습니다. 폴더 구조를 확인해 주세요.")
        st.info("구조 예시: app.py 파일이 있는 곳에 'htmls' 폴더가 있고 그 안에 'index.html'이 있어야 합니다.")

if __name__ == "__main__":
    main()
