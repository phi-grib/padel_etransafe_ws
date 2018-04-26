FROM openkbs/jre-mvn-py3

WORKDIR /opt

COPY app.py .

RUN wget http://www.yapcwsoft.com/dd/padeldescriptor/PaDEL-Descriptor.zip && \
    unzip PaDEL-Descriptor.zip 

ENTRYPOINT [ "python", "app.py" ]

