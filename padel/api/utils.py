import json
import urllib
from subprocess import Popen, PIPE, STDOUT


def get_padel_params(file):
    """
    shows PaDEL available parameters

    Returns:
    --------
    JSON
    """
    with open(file) as f:
        params = json.load(f)
    return params


base_cmd = ['java',
            '-Djava.awt.headless=true',
            '-jar',
            'PaDEL-Descriptor.jar']


def build_cmd_from_uri(args, cmd=base_cmd):
    """
    Builds PaDEL launch commant from postet uri

    Returns:
    --------
    List with commands
    """
    params_l = ["-" + k + " " + v for k, v in args.items()]
    final_cmd = cmd + params_l
    return final_cmd


def build_cmd_from_json(json, uid, cmd=base_cmd):
    """
    Builds PaDEL launch commant from postet uri

    Returns:
    --------
    List with commands
    """
    # build list of param, value from json
    params_l = []
    for item in json.items():
        params_l.extend(item)

    workdir = json['-dir']  # get work dir from POST json
    # build the results file string:
    absolute_file_name = workdir + 'padel_results_{}'.format(uid)
    # build list with param name, value
    filename_param = ['-file', absolute_file_name]
    # concat all parameter lists:
    final_cmd = cmd + params_l + filename_param
    return final_cmd


def launch_padel(cmd, uid):
    """
    Make system call to PaDEL-Descriptor.jar

     Returns:
    --------
    dict({'success': bool,
          'filename': result filename})
    """
    proc = Popen(cmd,
                 stdout=PIPE,
                 stdin=PIPE,
                 stderr=PIPE,
                 universal_newlines=True)

    stdout, stderr = proc.communicate()
    result = dict()
    if stderr:
        result['success'] = False
    else:
        result['success'] = True
        result['filename'] = 'padel_results_{}.csv'.format(uid)

    return result
