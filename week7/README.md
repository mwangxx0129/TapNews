# week7

Rule:
+ function 
- explanation
```command line```

# --------------------- common newspipline ---------------------------
# Start    
    - cp -r week7-codelab2/ week7
```
mkdir common
mv backend_server/utils/* common/
mv backend_server/requirements.txt ./
rmdir backend_server/utils/
```

# FAQ
I failed to install newspaper package. It shows errors like 'could not build the egg.'

This is because an error when installing nltk dependency. Try following commands:

```
sudo apt-get install python-dev;

sudo apt-get install libxml2-dev libxslt-dev;

sudo apt-get install libjpeg-dev zlib1g-dev libpng12-dev;

sudo pip install --upgrade setuptools;

sudo pip install newspaper
```

#------------------------01:12------------------------

- scrapers 
- ? cnn_news match with cnn_news_scraper.py
- ua: user agency
- ? pertend dif ua

02:11 xpath -> newspaper



