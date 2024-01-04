# Dockerfile
FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
