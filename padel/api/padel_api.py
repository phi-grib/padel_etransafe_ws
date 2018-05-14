
import sys
import os
import uuid
import time
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import abort
from flask import request

import utils
import launch_nailgun

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
    cmd = utils.build_cmd_from_json(req_json, uid)  # build cmd

    try:
        result = utils.launch_padel(cmd, uid)
    except:
        abort(500)
    return jsonify(result)

if __name__ == '__main__':
    launch_nailgun.start_nailgun()
    time.sleep(5)
    launch_nailgun.add_cp_nailgun()
    app.run(debug=False, host='0.0.0.0')
