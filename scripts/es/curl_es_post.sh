curl -X POST \
  http://localhost:9200/helloworld/_doc \
  -H 'Content-Type: application/json' \
  -d '{"hello": "world"}'
