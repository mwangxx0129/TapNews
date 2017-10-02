# setup

## import mongodb
mongodb
```
mongoexport --db <database-name> --collection <collection-name> --out output.json

mongoimport --db <database-name> --collection <collection-name> --file input.json

mongoexport --db tap-news --collection news-test --out output.json

mongoimport --db tap-news --collection news-test --file output.json


db["news-test"].find().count()

tap-news news-test
```