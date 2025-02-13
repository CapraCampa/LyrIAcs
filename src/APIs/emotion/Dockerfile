# Use an official Python image as a base
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the API files
COPY ./src/APIs/emotion /app/api
COPY ./artifacts/emotion /app/artifacts/emotion

# Install dependencies
RUN pip install --no-cache-dir -r api/requirements.txt

# Expose the API port
EXPOSE 8000

# Run the API using Uvicorn
CMD ["uvicorn", "api.api_emotion:app", "--host", "0.0.0.0", "--port", "8000"]