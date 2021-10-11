#! /usr/bin/python3

import requests
from passwords import *



print(requests.get('http://172.17.0.4/basic-auth/u/p', auth=auth(),timeout=1).text)
