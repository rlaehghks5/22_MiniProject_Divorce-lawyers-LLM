# Divorce-lawyers-LLM
이혼전문 변호사 LLM 입니다!

- Tesla V100 32GB 한 대를 사용해서 튜닝하였습니다.
- SOLAR 10.7B에 PEFT LORA를 붙이고, 4bit 양자화를 통해서 학습시켰습니다. 
- 학습 코드는 이 repo를 참고 하였습니다. https://github.com/nlpai-lab/KULLM

- Inference는 24GB 한 대 만으로도 가능합니다!
- LORA MODEL CARD : https://huggingface.co/DoHwan9672/SOLAR10.7B-Divorce-Lawyers-LLM-PEFT

- 데이터셋은 "찾기쉬운 생활법령 정보 ‘이혼' 키워드 | 백문백답, 판례, 솔로몬의 재판 카테고리", "다정 법률 상담소 | 이혼 분쟁 - FAQ", 네이버 지식인 크롤링을 통하여 구축하였습니다. 
- 데이터셋은 학습 및 연구 목적으로만 사용하였습니다. https://huggingface.co/datasets/DoHwan9672/divorce_QA_korean

### create conda env

```
conda env create -f llm.yaml
conda activate llm
```

### Run Fastapi backend


```
cd Divorce-lawyers-LLM
uvicorn main:app --reload
```

### Run Streamlit Frontend

```
streamlit run app.py
```

### Access Streamlit app
http://localhost:8501 

### Example
![Initial](https://github.com/rlaehghks5/Divorce-lawyers-LLM/assets/121927513/8ed7f75f-c507-48c8-a6dc-45fb873ba90b.png)
