# Run a search against local es instance and output the response body
# OR the values of a given field ("column").

import json
import requests
import sys

host = 'localhost:9200'

idx = sys.argv[1]
query = sys.argv[2]
req_body = {
    "query": {
        "match": {
            "wiki_extract": {
                "query": query
            }
        }
    }
}
resp = requests.post(f'http://{host}/{idx}/_search', headers={'Content-Type': 'application/json'}, data=json.dumps(req_body))

if len(sys.argv) < 4:
    print(resp.text)
else:
    column = sys.argv[3]
    data = json.loads(resp.text)
    for obj in data['hits']['hits']:
        print(obj['_source'].get(column, None))

