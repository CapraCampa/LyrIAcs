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

To use the **virtual enviroment**:
- **python -m venv venv** (venv is already added to the .gitignore file)
- Go to venv/Scripts and execute activate (**source activate** on Linux/Mac or **source venv/Scripts/activate** on windows)
- **pip install -r requirements.txt**
- if you need any more libraries execute **pip install <package_name_1>** and **pip freeze > requirements.txt**
- **deactivate** to exit
