FROM python:3.8.5-alpine3.12

COPY requirements.txt /alpine-wheels/index/requirements.txt

RUN /usr/local/bin/pip install --no-cache-dir --requirement /alpine-wheels/index/requirements.txt
