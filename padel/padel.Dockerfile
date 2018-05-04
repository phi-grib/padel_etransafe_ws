FROM openkbs/jre-mvn-py3

WORKDIR /opt/api

RUN wget http://www.yapcwsoft.com/dd/padeldescriptor/PaDEL-Descriptor.zip && \
    unzip PaDEL-Descriptor.zip 

COPY api /opt/api/

EXPOSE 5000
ENTRYPOINT [ "python", "padel_api.py" ]


