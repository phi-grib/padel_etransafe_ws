from flask import Flask
from flask import jsonify
from flask import make_response
from flask import abort
from flask import request


import utils
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
 
    uri = request.url  # request POST url
    cmd = utils.build_cmd(uri)

    stdout, _ = utils.calc_descriptors(cmd)

    return stdout


@app.route('/padel/api/v0.1/calc/json', methods=['POST'])
def digest_json():
    """
    parse json and returns path of file with calculated descriptors
    """

    if not request.json:
        abort(400)

    req_json = request.json

    # params = {
    #     'id': tasks[-1]['id'] + 1,
    #     'title': request.json['title'],
    #     'description': request.json.get('description', ""),
    #     'done': False
    # }
    #
    # return jsonify({'task': task}), 201
    #
    # uri = request.url  # request POST url
    # cmd = utils.build_cmd(uri)
    #
    # stdout, _ = utils.calc_descriptors(cmd)
    print(req_json)
    return jsonify(req_json)


if __name__ == '__main__':
    app.run(debug=True)
