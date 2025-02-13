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
py -m uvicorn src.APIs.emotion.api_emotion:app --port 8081 --reload
```

To launch the **web page**:

```
cd .\src\web\
py -m streamlit run web_service.py
```


Pushing images to **DockerHub**:

- Build docker images:
    ```
    docker build -t lyriacs-web -f src/web/Dockerfile .
    docker build -t lyriacs-api-genre -f src/APIs/genre/Dockerfile .
    docker build -t lyriacs-api-emotion -f src/APIs/emotion/Dockerfile .
    ```

- Tag images:
    ```
    docker tag lyriacs-web cvf751/lyriacs-web:latest
    docker tag lyriacs-api-genre cvf751/lyriacs-api-genre:latest
    docker tag lyriacs-api-emotion cvf751/lyriacs-api-emotion:latest
    ```

- Push images:
    ```
    docker push cvf751/lyriacs-web:latest
    docker push cvf751/lyriacs-api-genre:latest
    docker push cvf751/lyriacs-api-emotion:latest
    ```