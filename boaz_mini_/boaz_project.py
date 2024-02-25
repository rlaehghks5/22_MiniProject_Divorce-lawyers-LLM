#패키지 불러오기
import streamlit as st
import requests  # API 호출을 위해 requests 라이브러리를 사용

# 기능 구현 함수: 자체 LLM 모델 API를 호출하여 질문에 대한 답변 생성
# prompt -> 사용자로부터 입력받은 텍스트
def ask_my_model(prompt):
    
    # FastAPI 서버의 엔드포인트로 변경 
    # 여기서는 로컬에서 실행 중인 서버의 주소를 사용
    response = requests.post("http://localhost:8000/generate/", json={"text": prompt})
    if response.status_code == 200:  # 정상적인 응답 확인
        return response.json()['response']  # JSON 응답에서 결과 추출
    else:
        return "모델 호출 중 오류 발생: " + response.text

# 메인 함수: 스트림릿 UI 구성 및 로직 처리
def apple2():
    st.set_page_config(page_title="이혼 승소 판단 시스템")
    st.header("📃 이혼 승소 판단 시스템")
    st.markdown('---')

    # 사용자 입력 받기
    user_input = st.text_area("본인의 상황을 입력하세요")

    # '판단하기' 버튼 처리
    if st.button("판단하기"):
        if user_input:  # 사용자 입력이 있을 경우에만 처리
            prompt = f"사례 분석: {user_input}\n\n 이혼 승소 여부와 근거는?"
            response = (prompt)
            st.write("결과:")
            st.info(response)
        else:
            st.warning("사례를 입력해주세요.")

if __name__ == "__apple2__":
    apple2()
