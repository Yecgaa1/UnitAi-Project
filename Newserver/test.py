from flask import Flask, redirect, url_for, request
import json
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        #user = request.form['nm']
        #data = json.loads(request.get_data(as_text=True))
        #print(data)
        print(request.json)
        #print(type(request.headers))
        return {
            "user":'xutongxin'
        }
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))

if __name__ == '__main__':
    app.run()