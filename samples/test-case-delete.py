#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import argparse
import json
import requests


def delete_case(caseId):
    """
        :param caseId: Case identifier
    """

    req = url + "/api/case/{}".format(caseId)

    try:
        response = requests.delete(req, auth=auth, verify=False)
    except requests.exceptions.RequestException as e:
        sys.exit("Error: {}".format(e))

    if response.status_code == 201:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
        print('')
        id = response.json()['id']
    else:
        print('Response: {} - {}'.format(response.status_code, response.text))


def list_delete(filename):
    with open(filename, 'r') as f:
        list = f.read().splitlines()
    for caseId in list:
        delete_case(caseId)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Delete events from TheHive')
    parser.add_argument('-f', '--filename', type=str,
                        help='File containing list of even IDs to delete')
    parser.add_argument('-e', '--event', help='Single event ID to delete')

    args = parser.parse_args()
    url = 'http://127.0.0.1:9000'
    username = 'username'
    password = 'password'
    auth = requests.auth.HTTPBasicAuth(username=username,
                                       password=password)

    if args.filename is not None:
        list_delete(args.filename)
    else:
        delete_case(args.event)
