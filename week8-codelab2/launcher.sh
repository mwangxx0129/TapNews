#!/bin/bash

# Run this shell under: /week8-codelab2/

cd news_recommendation_service
python click_log_processor.py&
python recommendation_service.py&

cd ../backend_server
python service.py&

cd ../web-server/client
npm install
npm run build

cd ../server
npm install
npm start&

echo "=================================================="

read -p "PRESS [ANY KEY] TO TERMINATE PROCESSES." PRESSKEY

kill $(jobs -p)