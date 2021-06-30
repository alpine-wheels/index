FROM python:3.10.0b3-alpine3.13

COPY requirements.txt /alpine-wheels/index/requirements.txt

RUN /usr/local/bin/pip install --no-cache-dir --requirement /alpine-wheels/index/requirements.txt
