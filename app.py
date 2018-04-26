from flask import Flask
from flask import jsonify
from flask import make_response
from flask import abort
from flask import request
from subprocess import Popen, PIPE, STDOUT
import urllib


app = Flask(__name__)


# TODO: 
# - get PaDEL parameters from padel_help.json
# - habdle the REST uri in calc_descriptors()
# - return JSON with results ( path of the results file)
# and status of the executions

params = [
    {
        'name': 'maxruntime',
        'description': 'Maximum running time per molecule (in milliseconds). Use -1 for unlimited.'
    },
    {
        'name': 'su',
        'description': 'sa'
    },
]


@app.route('/padel/get_params', methods=['GET'])
def get_params():
    '''
    Returns query parameters for PaDEL-Descriptor.jar
    '''
    return jsonify({'params': params})


def build_cmd(uri):

    cmd = 'java -Djava.awt.headless=true -jar PaDEL/PaDEL-Descriptor.jar'.split(' ')
    # get query fragment
    query = urllib.parse.urlparse(uri).query
    # parse string of params to list of tuples
    params = urllib.parse.parse_qsl(query)
    params_l = ["-" + k + " " + v for k, v in params]
    final_cmd = cmd + params_l
    return final_cmd


@app.route('/padel', methods=['POST'])
def calc_descriptors():
    '''
    parse query and returns path of file with calculated descriptors
    '''
    uri = request.url  # request POST url
    cmd = build_cmd(uri)

    # Make system call to PaDEL-Descriptor.jar
    proc = Popen(cmd, stdout=PIPE,
                 stdin=PIPE,
                 stderr=PIPE,
                 universal_newlines=True)

    stdout, stderr = proc.communicate()
    print("<<<< OUTPUT from system call! >>>>{}".format(stdout))
    print("<<<<< ERROR from system call! >>>> {}".format(stderr))
    return stdout


if __name__ == '__main__':
    app.run(debug=True)
