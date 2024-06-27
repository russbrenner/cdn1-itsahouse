# Use the official Python image from the Docker Hub
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Command to run on container start
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]