# memcache-python3-example
Example of using memcache in python to pass data between two seperate scripts

## Debian
Install package
```
sudo apt-get install python3-memcached
sudo apt-get install memcached
```

## OSX
Install package
```
brew install memcached
```

## Demo
Run memcached in background
```
memcached &
```

Set value
```
python3 set.py
```
Get value
```
python3 get.py
```
Should see:
```
Hello
```
