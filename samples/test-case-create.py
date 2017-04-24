#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import requests
import sys
import json
import time
from thehive4py.api import TheHiveApi
from thehive4py.models import Case, CaseTask

api = TheHiveApi('http://127.0.0.1:9000', 'username', 'password', {'http': '', 'https': ''})


# Prepare the sample case
tasks = [
    CaseTask(title='Tracking'),
    CaseTask(title='Communication'),
    CaseTask(title='Investigation', status='Waiting', flag=True)
]
# tasks = []
case = Case(title='From TheHive4Py', tlp=3, flag=True, tags=['TheHive4Py', 'sample'], description='N/A', tasks=tasks)

# Create the case
print('Create Case')
print('-----------------------------')
id = None
response = api.create_case(case)
if response.status_code == 201:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')
    id = response.json()['id']
else:
    print('ko: {}/{}'.format(response.status_code, response.text))
    sys.exit(0)

# Get all the details of the created case
print('Get created case {}'.format(id))
print('-----------------------------')
response = api.get_case(id)
if response.status_code == requests.codes.ok:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')
else:
    print('ko: {}/{}'.format(response.status_code, response.text))
