# LyrIAcs


To launch the API (from the root folder):

```
py -3.11 -m uvicorn models.model1.api_model1:app --port 8080 --reload
py -3.11 -m uvicorn models.model2.api_model2:app --port 8081 --reload
```

To launch the web page:

```
py -3.11 -m streamlit run /src/web/web_service.py
```