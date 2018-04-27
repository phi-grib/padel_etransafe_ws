
import urllib
import json

def build_cmd(uri):

    cmd = 'java -Djava.awt.headless=true -jar PaDEL/PaDEL-Descriptor.jar'.split(' ')
    # get query fragment
    query = urllib.parse.urlparse(uri).query
    # parse string of params to list of tuples
    params = urllib.parse.parse_qsl(query)
    params_l = ["-" + k + " " + v for k, v in params]
    final_cmd = cmd + params_l
    return final_cmd

def get_padel_params(file):
    with open(file) as f:
        params = json.load(f)
    return params