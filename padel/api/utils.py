import json
import urllib
from subprocess import Popen, PIPE, STDOUT

base_cmd = ['java',
            '-Djava.awt.headless=true',
            '-jar',
            'PaDEL-Descriptor.jar']


def build_cmd_from_uri(args, cmd=base_cmd):
    """
    Builds PaDEL launch commant from postet uri
    """
    params_l = ["-" + k + " " + v for k, v in args.items()]
    final_cmd = cmd + params_l
    return final_cmd


def build_cmd_from_json(json, cmd=base_cmd):
    """
    Builds PaDEL launch commant from postet uri
    """
    # get query fragment
    # parse string of params to list of tuples
    # params = urllib.parse.parse_qsl(query)
    params_l = ["-" + k + " " + v for k, v in json.items()]
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


