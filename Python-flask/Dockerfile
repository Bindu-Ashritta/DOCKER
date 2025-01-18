# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies (if any)
RUN apt-get update && apt-get install -y python3-venv

# Create a virtual environment
RUN python3 -m venv /app/venv

# Install Flask and other dependencies inside the virtual environment
RUN /app/venv/bin/pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define the command to run your application
CMD ["/app/venv/bin/python", "app.py"]

