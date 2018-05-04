FROM python:3

RUN pip install requests

COPY make_requests.py /opt/

WORKDIR /opt/

ENTRYPOINT [ "/bin/bash" ]