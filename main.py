import os
import logging
import json

from flask import Flask
from flask import request
from flask.ext.api import status

from bridge.r_bridge import rpy2_version
from bridge.r_bridge import r_version_on_build
from bridge.r_bridge import calculate_log

from db.CloudantClient import connect
from db.CloudantClient import open_db
from db.CloudantClient import create_document

logging.basicConfig(level=logging.INFO)

def init_app():
    app = Flask(__name__)
    port = os.getenv('VCAP_APP_PORT', 5000)
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=int(port))

    return app

app = init_app()

cloudant_client = connect("demo_user", "password", "http://localhost:7080")
config_db = open_db(cloudant_client, "config_db")

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

@app.route('/model/log/<int:base>/<int:value>')
def get_calculated_log(base, value):
    return json.dumps({
        'logarithm': calculate_log(base, value)
        }, indent=4)


@app.route('/config'):
def create_config(methods = ["POST"]):
    request_body = request.get_json()
    create_document(config_db, request_body)

    return status.HTTP_201_CREATED
