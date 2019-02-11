FROM ubuntu

RUN apt-get update
RUN apt-get upgrade

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python3-all python3-pip

COPY requirments.txt /tmp/requirments.txt

RUN pip3 install -qr /tmp/requirments.txt

COPY ../app /opt/app/

WORKDIR /opt/app

CMD ["python3", "test.py"]