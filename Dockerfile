FROM python:3.9  # Use Python 3.9 as the base image

WORKDIR /app  # Set the working directory to /app inside the container

COPY . /app  # Copy all files from the current directory to /app in the container

RUN pip install -r requirements.txt  # Install the required Python packages from the requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]  # Run the Django development server on port 8000
