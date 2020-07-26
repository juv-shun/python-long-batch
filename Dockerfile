FROM python:3.7-alpine

LABEL maintainer Shun Fukusumi <shun.fukusumi@gmail.com>

WORKDIR /app

RUN apk update && apk add tzdata
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata && \
    rm -rf /var/cache/apk/*

RUN pip install -U setuptools pip && pip install pipenv

COPY Pipfile ./
COPY Pipfile.lock ./
RUN pipenv install --system

COPY src ./src
CMD ["python", "-u", "src/main.py"]
