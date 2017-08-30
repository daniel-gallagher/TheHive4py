#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import argparse
import requests
import sys
import json
from thehive4py.api import TheHiveApi

api = TheHiveApi('http://127.0.0.1:9000', 'username', 'password', {'http': '', 'https': ''})

def delete_case(caseId):
    response = api.delete_case(caseId)
    if response.status_code == 204:
        print('Deleting case {}'.format(caseId))
    else:
        print('Response: {} - {}'.format(response.status_code, response.text))


def search(string):
    query = '{"_field": "tags", "_value": "%s"}' % (string)

    response = api.find_cases(query=json.loads(query))

    if response.status_code == 200:
        case = response.json()
        for i in case:
            delete_case(i['id'])

    else:
        print('Response: {} - {}'.format(response.status_code, response.text))
        sys.exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search event tags to delete cases from TheHive')
    parser.add_argument('-s', '--search', help='Tag to search')

    args = parser.parse_args()

    if args.search is not None:
        search(args.search)
    else:
        print('No search query was provided!')
        exit(1)
