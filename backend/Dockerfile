# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies needed to compile Python packages (e.g., uvloop)
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies first (leveraging Docker cache)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Copy backend source code
COPY backend /app

# Expose backend port
EXPOSE 8000

# Start FastAPI using uvicorn with hot-reload for dev convenience
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]