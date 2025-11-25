FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file and install first (faster builds)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application folder
COPY ./app ./app

# Copy uploads folder (optional, if you want existing local files inside container)
COPY ./uploads ./uploads

# Ensure upload directory exists inside container
RUN mkdir -p /app/uploads

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI (correct module path)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
