import os
from groq import Groq

def extract_after_double_newline(text):
    parts = text.split("\n\n", 1)
    return parts[1] if len(parts) > 1 else text

def remove_surrounding_quotes(text):
    if text.startswith('"') and text.endswith('"'):
        return text[1:-1]
    return text

def ask_llama(current_chunks, genre, emotion):

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set!")
    
    # Client
    client = Groq(
        api_key=api_key,
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

    stanza = chat_completion.choices[0].message.content
    stanza = extract_after_double_newline(stanza)
    stanza = remove_surrounding_quotes(stanza)
    return stanza