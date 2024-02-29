import streamlit as st
import requests

def generate_text(input_text):
    response = requests.post("http://localhost:8000/generate_text/", json={"text": input_text})
    generated_text = response.json()["generated_text"]
    return generated_text

st.title("Hello! 이혼전문LLM 이혼GPT입니다.")
st.title("반가워요!")
st.title("")

# Text input box for user input
input_text = st.text_area("저에게 문의할 내용을 입력해주세요:", "")

if st.button("답변 생성"):
    if input_text:
        generated_text = generate_text(input_text)
        st.write("답변:")
        st.write(generated_text)
    else:
        st.write("Please enter some text to generate.")
        
# 이혼소송을 하려고 하는데, 
# 사실 남편과 다른 부분은 크게 이견이 없는데 이혼소송 재산분할만 이견이 심합니다. 
# 재산이 거의다 남편 명의인데 남편은 결혼할 때 본인이 가지고 온 재산에다 본인이 돈을 거의 벌었으므로
# 재산분할할게 거의 없다는 입장인거 같습니다. 
# 이혼소송 재산분할 다툼에서 어떻게 해야 이득을 볼 수 있을까요?