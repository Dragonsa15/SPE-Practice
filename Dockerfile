FROM python:3.9-slim AS build
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
WORKDIR /app
COPY requirements.txt /app
# RUN ls -a
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python3", "./app.py"]
