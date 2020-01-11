import json, requests

url = 'http://127.0.0.1:19150/test'
data = {
    "filename": "1.ppt"
}
headers = {
    'Content-Type': 'application/json'
}
req = requests.post(url, json.dumps(data), headers=headers)
# result = json.loads(req.text)
result = req.headers
with open("123.zip", 'wb') as f:
    f.write(req.content)
