FROM python:3

RUN apt-get update &&\
    apt-get install -y vim &&\
    pip install requests

COPY make_requests.py /opt/
COPY minicaco.sdf /opt/

WORKDIR /opt/

ENTRYPOINT [ "/bin/bash" ]