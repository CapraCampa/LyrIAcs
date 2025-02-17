# LyrIAcs

## Summary
LyrIAcs is a web-based songwriting assistant that leverages machine learning and large language models (LLMs) to help users compose song lyrics. The application allows users to input an initial set of lyrics, after which it provides genre and emotion predictions to guide the songwriting process. Users can then generate new stanzas using an LLM, edit them as needed, and build a complete song.

The system is built using:

- Streamlit for the interactive web interface.
- FastAPI for handling backend requests.
- Machine learning models for genre and emotion classification.
- Llama API for lyric generation.
- Render for cloud deployment.
  
LyrIAcs provides a seamless and intuitive experience, making it easier for musicians, poets, and creatives to explore new lyrical ideas and enhance their songwriting process.


## Execution

LyrIAcs can be currently accesed at https://lyriacs-web.onrender.com.

It is also possible to clone this repository and execute it locally by executing the `lysriasc.sh` bash script:
```
./lyriacs.sh <llama api key>
```
`<llama api key>` must be a valid Groq API key to be able to connect to Llama model.
