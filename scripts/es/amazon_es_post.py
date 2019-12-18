# Posts JSON file to configured es instance.

import boto3
import json
import sys
import yaml

from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

with open('secrets/config.yml') as config_f:
    config = yaml.load(config_f, Loader=yaml.Loader)

host = config['hosts']['es']
region = 'us-east-1'

service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

es = Elasticsearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

idx = sys.argv[1]
filename = sys.argv[2]
with open(filename, 'r') as f:
    document = json.load(f)

es.index(index=idx, doc_type="_doc", body=document)

