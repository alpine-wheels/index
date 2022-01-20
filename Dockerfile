FROM python:3.10.2-alpine3.15

COPY requirements.txt /alpine-wheels/index/requirements.txt

RUN /usr/local/bin/pip install --no-cache-dir --requirement /alpine-wheels/index/requirements.txt
