# Task-Data-Warehouse

## prerequisites
- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [docker-compose](https://docs.docker.com/compose/install/) 

## Run All
```
cd elasticsearch
docker-compose up -d
```

## Ensure your deployment success
```
CURL -X GET http://localhost:9200/_cat/indices?v
CURL -X GET http://localhost:9200/distribution/_search
```

## In case you found error
- https://stackoverflow.com/questions/68674897/mongodb-docker-replica-set-connection-error-host-not-found
