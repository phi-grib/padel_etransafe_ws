# PaDLE web service for eTransafe

This repo contains the (work in progress) proof of concenpt for module intercomunication. 

The first prototype of model intercomunication will consist of flame and PaDEL talking to each other. When flame recieves a petition of external molecular descriptors, it will make a request to the PaDEL container which will pick up the molecules and calculate the requested descriptors.

## Workflow Details:

+ The two containers have a running web service, are connected to each other (ports are visible), and share the same data volume
+ Flame recieves a .sdf file from user
+ Flame puts the file in the shared volume with a session id
+ User asks for service that requires external descriptor not available in flame
+ Flame then sends a HTTP request to the port where PaDEL is listening with the parameter payload e.g.:
```python
payload = {
            'filename':'mols_id.sdf',
            '3d':'true',
            'outfile':'results_id.json'
          }
          
request.post('localhost:xxxx/padel/calc', data=payload)
``` 
or 

```python
uri = 'localhost:xxxx/padel/calc?filename=mols_id.sdf&3d=true&outfile=results_id.json'

request.post(uri)
```
+ PaDEL returns the status of the calculation and the location of the results file via JSON 
+ Flame uses the new descriptors that are in the shared volume.
