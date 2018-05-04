
# Script to make requests to API
import argparse
import requests


def request_with_json():
    uri = "http://127.0.0.1:5000/padel/api/v0.1/calc/json"

    payload = {
        '-filename': 'sgdsgd.sdf'
    }

    req = requests.post(uri, json=payload)
    print(req.text)


def request_with_uri():
    uri = "http://127.0.0.1:5000/padel/api/v0.1/calc/uri"

    payload = {'key1': 'value1', 'key2': 'value2'}
    req = requests.post(uri, params=payload)
    print(req.url)
    print(req.text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--uri', action='store_true')
    group.add_argument('--json', action='store_true')

    args = parser.parse_args()
    if args.uri:
        request_with_uri()

    if args.json:
        request_with_json()
