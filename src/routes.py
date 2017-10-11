import json
from flask import Flask
from hello_r import rpy2_version
from hello_r import r_version_on_build


app = Flask(__name__)

@app.route('/')
def get_app_route():
    return 'OK'

@app.route('/health')
def healthCheck():
    return json.dumps({
        'health':'OK',
        'rpy2_version': rpy2_version(),
        'r_version_built_on': r_version_on_build()
    }, indent=4)
