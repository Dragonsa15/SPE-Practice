FROM python:3.9-slim AS build
ENV PYTHONUNBUFFERED 1
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "./app.py"]
