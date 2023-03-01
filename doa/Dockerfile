FROM ubuntu:18.04
        
RUN apt update
RUN apt-get install -y python3.10 python3-pip python3-dev build-essential gcc \
    libsnmp-dev snmp-mibs-downloader

RUN pip3 install --upgrade pip

RUN mkdir /app
WORKDIR /app
COPY . /app

WORKDIR /app/snmp_collector
RUN pip3 install -r requirements.txt

WORKDIR /app/pad
CMD python3 __main__.py

WORKDIR /app/doa
CMD python3 __main__.py

WORKDIR /app/exec_pr