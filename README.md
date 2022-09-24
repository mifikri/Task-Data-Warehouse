# Task-Data-Warehouse

## prerequisites
- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [docker-compose](https://docs.docker.com/compose/install/) 


## Setup MySQL server
Run MySQL server
```bash
docker run --name mariadbtest -v -e MYSQL_ROOT_PASSWORD=mypass -p 3306:3306 -d docker.io/library/mariadb:10.0
```

Run migration database using command below
```bash
docker exec -i mariadbtest mysql -u root -pmypass --database=pendidikan < ./pendidikan.sql
docker exec -i mariadbtest mysql -u root -pmypass --database=pekerjaan < ./pekerjaan.sql
```

## Preparation
```bash
virtualenv ~/venv
source ~/venv/bin/activate 
pip install -r preprocess/requirements.txt
```

## Run preprocess
to migrate data from sql to embedded document mongodb
```bash
python preprocess/mongo_handler.py
```

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
