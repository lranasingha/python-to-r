import json
from flask import Flask
from r_bridge import rpy2_version
from r_bridge import r_version_on_build
from r_bridge import calculate_log

app = Flask(__name__)

@app.route('/')
def get_app_route():
    return 'OK'

@app.route('/health')
def get_health_check():
    return json.dumps({
        'health':'OK',
        'rpy2_version': rpy2_version(),
        'r_version_built_on': r_version_on_build()
    }, indent=4)

@app.route('/log/<int:base>/<int:value>')
def get_calculated_log(base, value):
    return json.dumps({
        'logarithm': calculate_log(base, value)[0]
        }, indent=4)
