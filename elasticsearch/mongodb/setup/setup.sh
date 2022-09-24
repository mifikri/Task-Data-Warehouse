#!/bin/bash

sleep 10 | echo "Sleeping"

# /bin/mongosh mongodb://mongo1:27017 replicaSet.js
echo "Starting replica set initialization"
until /bin/mongosh --host mongo1 --eval "print(\"waited for connection\")"
do
   sleep 2
done
echo "Connection finished"
echo "Creating replica set"

MONGO1IP=$(getent hosts mongo1 | awk '{ print $1 }')

# read -r -d '' CMD <<EOF
# rs.initiate()
# EOF

read -r -d '' CMD <<EOF
rs.initiate(
  {
    _id : 'rp0',
    members: [
      { _id : 0, host : '${MONGO1IP}:27017' }
    ]
  }
)
EOF

read -r -d '' CMD2 <<EOF
rs.conf()
EOF
read -r -d '' CMD3 <<EOF
rs.status()
EOF

echo $MONGO1IP $MONGO2IP $MONGO3IP

echo $CMD | /bin/mongosh --host mongo1
echo $CMD2 | /bin/mongosh --host mongo1
echo $CMD3 | /bin/mongosh --host mongo1
echo "replica set created"
