#!/bin/bash

# API GENRE
echo "Setting up virtual environment for genre predictive model..."

# Navigate to the service directory
cd src/APIs/genre/ || { echo "Failed to enter genre predictive model"; exit 1; }

# Create a virtual environment (if it doesn't exist)
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created for genre predictive model"
fi

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install --no-cache-dir -r requirements.txt
echo "Dependencies installed for genre predictive model"

# Move back to the parent directory
cd ../../..

# Run the execution file in the background
python3 -m uvicorn src.APIs.genre.api_genre:app --port 8080 --reload &
echo "Running genre predictive model API"



# Deactivate virtual environment
deactivate



# API EMOTION
echo "Setting up virtual environment for emotion predictive model..."

# Navigate to the service directory
cd src/APIs/emotion/ || { echo "Failed to enter emotion predictive model"; exit 1; }

# Create a virtual environment (if it doesn't exist)
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created for emotion predictive model"
fi

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install --no-cache-dir -r requirements.txt
echo "Dependencies installed for emotion predictive model"

# Move back to the parent directory
cd ../../..

# Run the execution file in the background
python3 -m uvicorn src.APIs.emotion.api_emotion:app --port 8081 --reload &
echo "Running emotion predictive model API"

# Deactivate virtual environment
deactivate



# WEB SERVICE
echo "Setting up virtual environment for web service..."

# Navigate to the service directory
cd src/web/ || { echo "Failed to enter web service"; exit 1; }

# Create a virtual environment (if it doesn't exist)
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created for web service"
fi

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install --no-cache-dir -r requirements.txt
echo "Dependencies installed for web service"

# Run the execution file in the background
python3 -m streamlit run web_service.py
echo "🚀 Running web service at http://localhost:8501"

# Move back to the parent directory
cd ../..

# Deactivate virtual environment
deactivate
