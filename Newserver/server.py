# code:utf-8
from flask import Flask, redirect, url_for, request
import json

app = Flask(__name__)
Version = "0.0.1b"


@app.route('/login', methods=['POST', 'GET'])
def login():
    print(request.method)
    if request.method == 'POST':
        # user = request.form['nm']
        # data = json.loads(request.get_data(as_text=True))
        # print(data)
        print(request.json)
        rec = request.json
        if rec['acc'] == "ConnectTest":
            return{
                'code': Version
            }
        else:
            print(rec['acc'], rec['pd'])
            # print(type(request.headers))
            return {
                'code': '0'
            }


if __name__ == '__main__':
    app.run(port=19150)
