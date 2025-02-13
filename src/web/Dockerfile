# Use an official Python image as a base
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the web files
COPY ./src/web /app

# Install clipboard utility
RUN apt-get update && apt-get install -y xclip xsel python3-tk && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Streamlit web app port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "web_service.py", "--server.port=8501", "--server.address=0.0.0.0"]
