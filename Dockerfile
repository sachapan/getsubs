#Use the official Python image as the base image
#FROM python:3.11-slim
FROM alpine:3.17
RUN apk add --no-cache python3 ffmpeg

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the dependencies
RUN python3 -m ensurepip
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy the script file to the container
COPY getjwsubs.py .

# Set the command to run your Python script
CMD ["python3", "getjwsubs.py"]
