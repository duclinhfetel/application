import requests
import time
while True:
    ret = requests.get("http://localhost/health")
    print(ret.text)
    ret = requests.get("http://localhost/api/v2/info")
    print(ret.text)
    time.sleep(1)