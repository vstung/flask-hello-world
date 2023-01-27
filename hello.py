# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
import os
import json
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/env')
def env_show():
    result = []
    for k, v in os.environ.items():
        result.append({k: v})
    result.append({"python_interpreter": sys.executable})
    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True)

