# Run a search against local es instance and output the response body
# OR the values of a given field ("column").

import json
import requests
import sys

host = 'localhost:9200'

idx = sys.argv[1]
query = sys.argv[2]
resp = requests.get(f'http://{host}/{idx}/_search', params={'q': query})

if len(sys.argv) < 4:
    print(resp.text)
else:
    column = sys.argv[3]
    data = json.loads(resp.text)
    for obj in data['hits']['hits']:
        print(obj['_source'].get(column, None))

