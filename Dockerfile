# Include Python
FROM python:3.10-slim

# Define your working directory
WORKDIR /

# Add your file
COPY . .

# Install runpod
RUN pip install runpod

# Call your file when your container starts
CMD [ "python", "-u", "/main.py" ]
