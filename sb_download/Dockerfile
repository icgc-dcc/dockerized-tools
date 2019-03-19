FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python3-pip python3-dev
RUN pip3 install sevenbridges-python

COPY main.py /app/download
WORKDIR /app
