# Use a lightweight official Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (for faster rebuilds via Docker layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . .

# Expose the Flask port
EXPOSE 5000

# Command to run the Flask app when the container starts
CMD ["python", "app.py"]