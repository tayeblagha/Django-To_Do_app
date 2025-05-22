# Use the official Python runtime image
FROM python:3.9-slim

# Create the app directory
RUN mkdir /app

# Set the working directory inside the container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Upgrade pip
RUN pip install --upgrade pip

# Copy the Django project and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project to the container
COPY . /app/

# Expose the Django port
EXPOSE 8000

# Run migration first
# ENTRYPOINT ["python", "manage.py", "migrate"]

# Then start the Django development server
CMD python manage.py makemigrations &&  python manage.py migrate && python manage.py runserver 0.0.0.0:8000
