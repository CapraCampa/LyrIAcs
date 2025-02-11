# LyrIAcs

To use the **virtual enviroment**:
- Create the virtual enviroment
    ```
    py -m venv venv
    ```

- Activate it
    ```
    # Windows
    Set-ExecutionPolicy Unrestricted -Scope Process
    venv\Scripts\activate

    # Linux/Mac
    source venv/bin/activate
    ```

- Install requirements
    ```
    pip install -r requirements.txt
    ```

After usage:
- Update dependencies (if needed)
    ```
    pip freeze > requirements.txt
    ```

- Deactivate
     ```
    deactivate
    ```   


To launch the **APIs**:

```
py -m uvicorn src.APIs.genre.api_genre:app --port 8080 --reload
py -m uvicorn models.model2.api_model2:app --port 8081 --reload
```

To launch the **web page**:

```
cd .\src\web\
py -m streamlit run web_service.py
```

To use the **containers**:
```
docker build -t lyriacs-web -f src/web/Dockerfile .
docker build -t lyriacs-api-genre -f src/APIs/genre/Dockerfile .
```

```
docker run -p 8501:8501 lyriacs-web
docker run -p 8000:8000 lyriacs-api-genre
```

