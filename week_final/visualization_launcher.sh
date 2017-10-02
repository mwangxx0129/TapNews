#!/bin/bash
cd data_visulization/data_visuilzation
# npm install
# npm run build
PORT=3001 npm start&

cd ../data_visulization_server
npm install
PORT=8080 npm start&

echo "=================================================="
read -p "PRESS [ANY KEY] TO TERMINATE PROCESSES." PRESSKEY

fuser -k 3001/tcp
fuser -k 8080/tcp
kill $(jobs -p)


