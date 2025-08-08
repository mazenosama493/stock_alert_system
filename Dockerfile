# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and to buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set work directory inside container
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Expose the port your app runs on (e.g., 8000)
EXPOSE 8000

# Default command to run your Django app with Gunicorn
CMD ["gunicorn", "stock_alert_system.wsgi:application", "--bind", "0.0.0.0:8000"]
