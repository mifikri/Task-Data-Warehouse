# Task-Data-Warehouse

## prerequisites
- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [docker-compose](https://docs.docker.com/compose/install/)
- git

## Run All
Open in your terminal, then clone the repository
```bash
git clone https://github.com/mifikri/Task-Data-Warehouse.git
cd Task-Data-Warehouse/elasticsearch
mkdir -p elasticsearch/data
sudo chown -R 1000:1000 ./elasticsearch #for mac use `brew`
docker-compose up -d
```

## Ensure your deployment success
Open in your terminal, then call HTTP GET to elasticsearch URI
```bash
curl -X GET http://localhost:9200/_cat/indices?v
curl -X GET http://localhost:9200/distribution/_search
```

## Kibana
Open kibana on your browser with url `http://localhost:9200`

## In case you found error
- https://stackoverflow.com/questions/68674897/mongodb-docker-replica-set-connection-error-host-not-found
- https://techoverflow.net/2020/04/18/how-to-fix-elasticsearch-docker-accessdeniedexception-usr-share-elasticsearch-data-nodes/
