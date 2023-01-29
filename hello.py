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
    return json.dumps(result)

@app.route('/pythonver')
def python_ver_show():
    return json.dumps({"python_version": sys.version})

if __name__ == '__main__':
    app.run(debug=True)

