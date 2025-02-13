import os
from groq import Groq
import streamlit as st

def ask_llama(current_chunks, genre, emotion):

    LLM_API_KEY = st.secrets.get("LLM_API_KEY")
    # Client
    client = Groq(
        api_key=LLM_API_KEY
    )

    # Prompt
    chat_completion = client.chat.completions.create(
        messages = [{
            "role": "user",
            "content": f""""You are an advanced AI trained in songwriting. Your task is to generate a new stanza (4 lines) for a song based on the following inputs. Return ONLY the stanza itself, no more text:

                1. **Song so far:**  
                {current_chunks}

                2. **Genre:**  
                {genre}

                3. **Emotion:**  
                {emotion}

                **Guidelines:**  
                - Maintain the same lyrical style and structure as the song so far.  
                - Ensure the new stanza fits seamlessly with the existing lyrics.  
                - Reflect the chosen emotion in the words, tone, and imagery.  
                - Keep the genre’s common themes and vocabulary in mind.  
                - Use poetic and evocative language appropriate for the mood.

                Now generate the stanza. Return ONLY the stanza itself, no more text:""",
        }],
    model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content