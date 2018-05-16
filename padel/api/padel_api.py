
import sys
import os
import uuid
import time
import argparse
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import abort
from flask import request

import utils
import launch_nailgun

from functools import partial

# Commands depending on the if launch padel with nailgun or vanila java
BASE_CMD = ['ng',
            'padeldescriptor.PaDELDescriptorApp',
            '-maxruntime', '-1',
            '-retainorder',
            '-threads', '1',
            '-descriptortypes', 'padel_descriptors.xml']

NO_NAILGUN_CMD = ['java', '-jar',
                  'PaDEL-Descriptor.jar',
                  '-maxruntime', '-1',
                  '-retainorder',
                  '-threads', '1',
                  '-log',
                  '-descriptortypes', 'padel_descriptors.xml']


app = Flask(__name__)

# TODO:
# - habdle the REST uri in calc_descriptors()
# - return JSON with results ( path of the results file)
# and status of the executions


@app.route('/padel/api/v0.1/get_params', methods=['GET'])
def get_params():
    """
    Returns query parameters for PaDEL-Descriptor.jar
    """
    params = utils.get_padel_params('padel_help.json')
    return jsonify(params)


@app.route('/padel/api/v0.1/calc/uri', methods=['POST'])
def digest_uri():
    """
    parse uri and returns path of file with calculated descriptors
    """
    uid = uuid.uuid4().hex[:6].upper()  # make a session id

    args = request.args  # request POST url args
    cmd = utils.build_cmd_from_uri(args)

    # return jsonify(cmd)
    result = utils.launch_padel(cmd, uid)
    return jsonify(result)


@app.route('/padel/api/v0.1/calc/json', methods=['POST'])
def digest_json():
    """
    parse json and returns path of file with calculated descriptors
    """

    if not request.json:
        abort(400)

    uid = uuid.uuid4().hex[:6].upper()  # make a session id

    req_json = request.json  # get json from post
    cmd = partial_cmd_json(req_json, uid)  # build cmd with cmd param inherited from init

    try:
        result = utils.launch_padel(cmd, uid)
    except:
        abort(500)
    return jsonify(result)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--nonailgun', action='store_true')
    args = parser.parse_args()

    if not args.nonailgun:

        launch_nailgun.start_nailgun()
        time.sleep(5)
        launch_nailgun.add_cp_nailgun()

        # build partial create_cmd_from_json with with no nailgun cmd  
        partial_cmd_json = partial(utils.build_cmd_from_json, cmd=BASE_CMD)

        app.run(debug=False, host='0.0.0.0')

    else:
        partial_cmd_json = partial(utils.build_cmd_from_json, cmd=NO_NAILGUN_CMD)
        app.run(debug=False, host='0.0.0.0')