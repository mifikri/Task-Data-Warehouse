# Task-Data-Warehouse

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
pip install -r requirements.txt
```

## Run evaltools automation
```bash
python mongo_handler.py
```