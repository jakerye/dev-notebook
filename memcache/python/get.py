#!/usr/bin/python3

import memcache
shared = memcache.Client(['127.0.0.1:11211'], debug=0)    
print(shared.get('Value'))
