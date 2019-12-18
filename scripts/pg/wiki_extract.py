# Script to pull part of the intro of a wikipedia article
# passed in on the command line

import json
import requests
import sys

wikipedia_extract_url = 'https://en.wikipedia.org/w/api.php'
params = {
    'action': 'query',
    'format': 'json',
    'prop': 'extracts',
    'exchars': 1200, # Max at time of writing
    'exlimit': 1,
    'exintro': 1,
    'explaintext': 1
}

# Make request with the first arg and parse json from response body
params['titles'] = sys.argv[1]
resp = requests.get(wikipedia_extract_url, params=params)
resp_body_json = json.loads(resp.text)

# Get the extract from the first page of the query
print(resp_body_json)
extract = list(resp_body_json['query']['pages'].values())[0]['extract'];
print(extract)

