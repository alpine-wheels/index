FROM python:3.11.3-alpine3.18

RUN /usr/sbin/adduser -g python -D python

USER python
RUN /usr/local/bin/python -m venv /home/python/venv

COPY --chown=python:python requirements.txt /home/python/alpine-wheels/index/requirements.txt
RUN /home/python/venv/bin/pip install --no-cache-dir --requirement /home/python/alpine-wheels/index/requirements.txt

ENV PATH="/home/python/venv/bin:${PATH}" \
    PYTHONUNBUFFERED="1" \
    TZ="Etc/UTC"

LABEL org.opencontainers.image.authors="William Jackson <william@subtlecoolness.com>" \
      org.opencontainers.image.source="https://github.com/alpine-wheels/index"
