
# Script to make requests to API
import argparse
import requests


# uri hostid uses padel bcause is the name of the service in docker-compose
def request_with_json():
    uri = "http://padel:5000/padel/api/v0.1/calc/json"

    payload = {
        '-2d': '',
        '-dir': '/opt/data/',
        '-log': ''
    }

    req = requests.post(uri, json=payload)
    print(req.json())


def request_with_uri():
    uri = "http://padel:5000/padel/api/v0.1/calc/uri"

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
