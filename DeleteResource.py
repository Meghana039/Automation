import requests
import json
import jsonpath
#APL URL

url =  " https://reqres.in/api/users/2"

#delete resource
response = requests.delete(url)

print(response.status_code)

assert response.status_code==204