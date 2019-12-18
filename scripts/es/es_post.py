# Posts JSON file to local es instance.

import json
import requests
import sys

host = 'localhost:9200'

idx = sys.argv[1]
filename = sys.argv[2]
with open(filename, 'r') as f:
    documents = json.load(f)

# Note: this is inefficient, in practice prefer the bulk api
for document in documents:
    headers = {'Content-Type': 'application/json'}
    requests.post(f'http://{host}/{idx}/_doc', data=json.dumps(document),
                                               headers=headers)

