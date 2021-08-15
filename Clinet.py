from flask.wrappers import Response
import requests

import psutil
from werkzeug.wrappers import response

Base="http://127.0.0.1:5000/"
res=psutil.cpu_percent()

response= requests.put(Base+"cpu/1",{"cpuperc":res})
print(response.json())
input()
response= requests.get(Base+"cpu/1")
print(response.json())