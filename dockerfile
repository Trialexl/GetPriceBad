# Use an official Python runtime as the base image
FROM python:3.11.7

# Create a working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV FLASK_APP app.py

# Run the application
CMD ["gunicorn", "-c", "gunicorn_config.py", "--bind", "0.0.0.0:5000", "app:app"]  