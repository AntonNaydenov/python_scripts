#Python script for get values
import json
import redis
import sys
val='e96ec958-fb68-11eb-80c3-30e1715c5317'
val = sys.argv[1]
print(val)
r=redis.Redis(host='redis')
print (r.get(val).decode('utf-8'))
