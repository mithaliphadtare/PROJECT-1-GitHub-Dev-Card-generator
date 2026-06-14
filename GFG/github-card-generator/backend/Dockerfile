# Use a Python base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app/backend

# Copy the requirements file and install dependencies using uv
COPY requirements.txt .
RUN pip install uv && uv sync

# Create the static/cards directory for generated HTML cards
RUN mkdir -p ../static/cards

# Copy the rest of the application code
COPY . .

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
