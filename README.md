# PaDLE web service for eTransafe

This repo contains the (work in progress) proof of concenpt for module intercomunication. 

The first prototype of model intercomunication will consist of flame and PaDEL talking to each other. When flame recieves a petition of external molecular descriptors, it will make a request to the PaDEL container which will pick up the molecules and calculate the requested descriptors.

## Workflow Details:

+ The two containers have a running web service, are connected to each other (ports are visible), and share the same data volume
+ Flame recieves a .sdf file from user
+ Flame puts the file in the shared volume with a session id
+ User asks for service that requires external descriptor not available in flame
+ Flame then sends a HTTP POST to the port where PaDEL is listening with the parameter payload.
+ PaDEL returns the status of the calculation and the location of the results file via JSON 
+ Flame uses the new descriptors that are in the shared volume and finishes the service that user asked for.
+ The setup of the containers, the network and the volume will be done with docker-compose 

## nailgun setup:

This is what you need to do in order to **run this service in your host** (outside the container.)
install nailgun:
```bash
git clone git://github.com/martylamb/nailgun.git
cd nailgun
mvn clean install
cd nailgun-client
gcc ng.c -o ng
cp ng ~/bin
```
----------
The following is done by the flask service when it starts.

start nailgun server:

```bash
java -classpath nailgun-server-0.9.3-SNAPSHOT.jar com.martiansoftware.nailgun.NGServer
``` 

add padel libs to nailgun. 
```bash
ng ng-cp lib/*.jar PaDEL-Descriptor.jar
```
