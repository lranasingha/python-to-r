import os
import logging
import json


from flask import Flask
from flask import request
from flask import make_response
import atexit

from bridge.r_bridge import rpy2_version
from bridge.r_bridge import r_version_on_build
from bridge.r_bridge import calculate_log

from db.cloudant_interface import *
from db.db2_interface import connect_db2

logging.basicConfig(level=logging.INFO)

def init_app():
    app = Flask(__name__)
    port = os.getenv('VCAP_APP_PORT', 5000)
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=int(port))

    return app

app = init_app()


cloudant_client = connect_cloudant("admin", "pass", "http://localhost:7080")
config_db = create_cloudant_db(cloudant_client, "config_db")

db_client = connect_db2("eventsdb")


@atexit.register
def shutdown():
    cloudant_client.disconnect()

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


@app.route('/config', methods = ["POST"])
def create_config():
    request_body = request.get_json()

    create_document(config_db, request_body)

    return make_response('', 201)
