FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python3-pip python3-dev
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
RUN cd /usr/local/bin
RUN ln -s /usr/bin/python3 python
RUN pip3 install --upgrade pip
RUN apt-get install -y software-properties-common wget

RUN wget https://cgc.sbgenomics.com/downloads/cli/cgc-uploader.tgz -O cgc-uploader.tgz
RUN tar -xvzf cgc-uploader.tgz

# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

RUN mkdir /app
#COPY . /app

ENV PATH="/app:/app/cgc-uploader/bin:${PATH}"

RUN mv cgc-uploader /app
RUN mv /app/cgc-uploader/bin/cgc-uploader.sh /app/cgc-uploader/bin/cgc-upload

RUN pip3 install sevenbridges-python
COPY sb_download/main.py /app/download
COPY sb_download/main.py /app/upload

WORKDIR /app

