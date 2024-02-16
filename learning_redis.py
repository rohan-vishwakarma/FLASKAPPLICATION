import redis
import datetime

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

r.set("name", "rohan")

# current_d = datetime.datetime.now()

dict = {
    "name": "rohan",
    "surname" : "vishwakarma",
    "company" : "JD Softech",
    "age" : '21'
}

b = r.hset("dict", dict )

print(r.get("name"))
