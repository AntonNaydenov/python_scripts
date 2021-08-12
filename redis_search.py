#Python script for search
import json
import redis
import sys
val='e96ec958-fb68-11eb-80c3-30e1715c5317'
val = sys.argv[1]
print("Search " + val + " in Redis")
r=redis.Redis(host='redis')
f=0
keys = r.keys()
for key in keys:
    v = r.get(key)
    
    if v:
        if val in v.decode('utf-8'):
             f = f+1
             print(key.decode('utf-8') + ': ' + r.get(key).decode('utf-8'))
if f != 0:
    print('Found ' + str(f) + ' records')
else: 
    print('Not Found!')
