FROM openkbs/jre-mvn-py3

WORKDIR /opt/app

RUN wget http://www.yapcwsoft.com/dd/padeldescriptor/PaDEL-Descriptor.zip && \
    unzip PaDEL-Descriptor.zip 

COPY app /opt/app/

EXPOSE 5000
ENTRYPOINT [ "python", "app.py" ]


