# Divorce-lawyers-LLM
이혼판례 판단 LLM

### create conda env

```
conda env create -f llm.yaml
```

### Run Fastapi backend
'''
uvicorn main:app --reload
'''

### Run Streamlit Frontend

'''
streamlit run app.py
'''

### Access Streamlit app
http://localhost:8501 

![Initial] https://github.com/rlaehghks5/Divorce-lawyers-LLM/assets/121927513/d5a7891d-2949-43a1-bdb2-c1c958d32ea7