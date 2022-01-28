#!/bin/python3
import json
import base64
import sys


with open(sys.argv[1]) as jsonfile:
    data = json.load(jsonfile)
    datastr = json.dumps(data)
    encoded = base64.b64encode(datastr.encode('utf-8'))
    print(encoded.decode())
