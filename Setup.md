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
# If above still not works, try here

1. Remove the repository version
```
sudo apt-get remove python-setup tools
```
2. if necessary, install pip again
```
wget https://bootstrap.pypa.io/get-pip.py;
sudo -H python get-pip.py
```
3. install setuptools via pip
```
sudo -H pip install -U pip setuptools
```
# still failed repeat from FAQ again