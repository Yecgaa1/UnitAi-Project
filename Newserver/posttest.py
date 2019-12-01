import json, requests

url = 'http://127.0.0.1:5000/login'
data = {
    "nm":"xutongxin"
}
headers={
    'Content-Type':'application/json'
}
req = requests.post(url, json.dumps(data),headers=headers)
#result = json.loads(req.text)
result=req.text
print(req)
print(result)

