# week8-codelab2

## Deploy
### pipeline_launcher
Open pipeline when you need 
sudo sh news_pipeline_launcher.sh


### open 4 terminals
```
service redis_6379 start

service mongod start

/week8-codelab2/web-server/server$ npm start

/week8-codelab2/backend_server$ python service.py

/week8-codelab2/news_recommendation_service$ python click_log_processor.py

/week8-codelab2/news_recommendation_service$ python recommendation_service.py
```
### run on backend 
/week8-codelab2/$: launcher.sh

### kill
killall python


## Notes
### mongo
```

mongo

show dbs

use news

show collections

db["test"].find().count()
```

### Code
+ Make sure the db collection is consistent

### Tools
+ pm2

### QA
+ shell order

+ kill all job, still need killall python

+ pm2
