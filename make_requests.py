
# Script to make requests to API

import requests


uri = "http://127.0.0.1:5000/padel/api/v0.1/calc/json"
payload = {
    '-filename': 'sgdsgd.sdf'
}

req = requests.post(uri, json=payload)
print(req.json())
