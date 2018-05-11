FROM openkbs/jre-mvn-py3

ENV PADEL_DIR /opt/api

WORKDIR $PADEL_DIR

RUN wget http://www.yapcwsoft.com/dd/padeldescriptor/PaDEL-Descriptor.zip && \
    unzip PaDEL-Descriptor.zip 

COPY api /opt/api/

RUN git clone git://github.com/martylamb/nailgun.git && \
    cd nailgun && \
    mvn clean install && \
    cp nailgun-server/target/nailgun-server-0.9.3-SNAPSHOT.jar ${PADEL_DIR} && \
    cd nailgun-client && \
    gcc ng.c -o ng && \
    cp ng /bin

# CMD java -classpath nailgun-server-0.9.3-SNAPSHOT.jar com.martiansoftware.nailgun.NGServer& &&\ 
#     ng ng-cp ${PADEL_DIR}/lib/*jar ${PADEL_DIR}/PaDEL-Descriptor.jar

EXPOSE 5000

ENTRYPOINT ["/bin/bash", "wrapper.sh"] 