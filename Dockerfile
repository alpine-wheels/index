FROM python:3.9.6-alpine3.14

COPY requirements.txt /alpine-wheels/index/requirements.txt

RUN /usr/local/bin/pip install --no-cache-dir --requirement /alpine-wheels/index/requirements.txt
