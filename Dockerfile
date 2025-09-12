FROM python:3.10-alpine3.18
LABEL maintainer="orbik.rumlom22@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .