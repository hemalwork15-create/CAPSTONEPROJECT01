# Use Python 3.11 slim image
FROM python:3.11-slim

WORKDIR /app

# Copy requirements first (caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY ./app ./app

# Create uploads folder
RUN mkdir -p /app/uploads

EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
