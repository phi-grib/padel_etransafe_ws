
# Script to make requests to API
import argparse
import requests
import pathlib

# uri hostid is padel bcause it is the name of the service in docker network
def request_with_json():
    uri = "http://padel:5000/padel/api/v0.1/calc/json"

    payload = {
        '-2d': '',
        '-dir': '/opt/data/',
    }

    req = requests.post(uri, json=payload)
    print(req.text)


def request_with_uri():
    uri = "http://padel:5000/padel/api/v0.1/calc/uri"

    payload = {'-2d': '', '-dir': '/opt/data/'}
    req = requests.post(uri, params=payload)
    print(req.url)
    print(req.text)


def get_params():
    uri = "http://padel:5000/padel/api/v0.1/get_params"
    req = requests.get(uri)
    print(req.text)


def request_single():

    uri = "http://padel:5000/padel/api/v0.1/calc/json"
    path = pathlib.Path('./data')
    dirs = path.glob('file_*/')
    for i, dir_ in enumerate(dirs):

        payload = {
            '-2d': '',
            '-dir': str(dir_.absolute()),
        }

        req = requests.post(uri, json=payload)
        print(req.text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--uri', action='store_true')
    group.add_argument('--json', action='store_true')
    group.add_argument('--params', action='store_true')
    group.add_argument('--single', action='store_true')

    args = parser.parse_args()
    if args.uri:
        request_with_uri()

    elif args.json:
        request_with_json()

    elif args.single:
        request_single()

    elif args.params:
        get_params()
