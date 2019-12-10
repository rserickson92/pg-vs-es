# Quick and dirty script to pull data from wikipedia and sync with
# existing postgres entries.

import json
import psycopg2
import requests
import sys
import yaml

with open('secrets/config.yml') as config_f:
    config = yaml.load(config_f, Loader=yaml.Loader)

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
country = sys.argv[1]
params['titles'] = country
resp = requests.get(wikipedia_extract_url, params=params)
resp_body_json = json.loads(resp.text)

# Get the extract from the first page of the query
extract = list(resp_body_json['query']['pages'].values())[0]['extract'];

pg_props = {
    'host': config['hosts']['pg'],
    'dbname': 'transactions',
    'user': 'postgres',
    'password': config['passwords']['pg']
}
pg_conn = psycopg2.connect(**pg_props)
pg_cur = pg_conn.cursor()

pg_cur.execute("UPDATE countries SET wiki_extract=%s WHERE name=%s", (extract, country))
pg_conn.commit()

pg_cur.close()
pg_conn.close()

