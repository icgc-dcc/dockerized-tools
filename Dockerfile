FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python3-pip python3-dev
RUN pip3 install sevenbridges-python

COPY sb_download/main.py /app/download
COPY sb_upload/main.py /app/upload
WORKDIR /app
