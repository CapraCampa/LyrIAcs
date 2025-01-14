# LyrIAcs


To launch the APIs:

```
py -3.11 -m uvicorn models.model1.api_model1:app --port 8080 --reload
py -3.11 -m uvicorn models.model2.api_model2:app --port 8081 --reload
```

To launch the web page:

```
cd .\src\web\
py -3.11 -m streamlit run web_service.py
```