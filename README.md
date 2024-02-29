# Divorce-lawyers-LLM
이혼판례 판단 LLM

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
![Initial](https://github.com/rlaehghks5/Divorce-lawyers-LLM/assets/121927513/304bd2d7-edb0-4e3c-a6cf-0e6c5c5ff0c5.png)