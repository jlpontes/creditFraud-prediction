# Stage 1: Define the base image
# We start from an official Python image. '3.9-slim' is a lightweight version, perfect for production.
FROM python:3.9-slim

# Stage 2: Set the working directory inside the container
# This is where our application files will live.
WORKDIR /app

# Stage 3: Copy and install dependencies
# First, copy only the requirements file to leverage Docker's layer caching.
# If requirements.txt doesn't change, Docker won't re-install libraries on subsequent builds.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 4: Copy the rest of the application files
# Copy the main application code and the trained model into the container.
COPY . .

# Stage 5: Expose the port the app runs on
# This informs Docker that the container listens on port 8000.
EXPOSE 8000

# Stage 6: Define the command to run the application
# This is the command that will be executed when the container starts.
# We use 0.0.0.0 to make the API accessible from outside the container.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
