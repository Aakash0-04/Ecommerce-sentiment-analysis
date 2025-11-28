# 1. Use official Python image
FROM python:3.11-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy requirements and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy application code and data (model + app)
COPY App ./App
COPY Data ./Data

# 5. Download NLTK data needed by your app
RUN python -m nltk.downloader stopwords && \
    python -m nltk.downloader wordnet

# 6. Expose port 8000 (FastAPI runs here)
EXPOSE 8000

# 7. Command to start the FastAPI app
CMD ["uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "8000"]
