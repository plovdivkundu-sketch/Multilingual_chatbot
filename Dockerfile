FROM python:3.10.11

# Install PortAudio, required for PyAudio
RUN apt-get update && apt-get install -y portaudio19-dev

# Set working directory to /app
WORKDIR /app

# Copy all files to /app
COPY . /app

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "10000"]
