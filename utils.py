import json
import urllib
from subprocess import Popen, PIPE, STDOUT


def build_cmd(uri):
    """
    Builds PaDEL launch commant from postet uri
    """
    cmd = ['java',
           '-Djava.awt.headless=true',
           '-jar',
           'PaDEL/PaDEL-Descriptor.jar']

    # get query fragment
    query = urllib.parse.urlparse(uri).query
    # parse string of params to list of tuples
    params = urllib.parse.parse_qsl(query)
    params_l = ["-" + k + " " + v for k, v in params]
    final_cmd = cmd + params_l
    return final_cmd


def get_padel_params(file):
    """
    Returns JSON
    """
    with open(file) as f:
        params = json.load(f)
    return params


def calc_descriptors(cmd):
    # Make system call to PaDEL-Descriptor.jar
    proc = Popen(cmd, stdout=PIPE,
                 stdin=PIPE,
                 stderr=PIPE,
                 universal_newlines=True)
    stdout, stderr = proc.communicate()
    return stdout, stderr
