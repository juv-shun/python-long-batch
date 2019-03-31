FROM python:3.7-alpine

LABEL maintainer Shun Fukusumi <shun.fukusumi@gmail.com>

WORKDIR /app

ENV TZ=Asia/Tokyo

RUN apk update
RUN pip install -U setuptools pip && pip install pipenv

COPY Pipfile ./
COPY Pipfile.lock ./
RUN pipenv install --system

COPY src ./src
CMD ["python", "-u", "src/main.py"]
