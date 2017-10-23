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
from bridge.r_bridge import get_event_info

from db.cloudant_interface import connect_cloudant
from db.cloudant_interface import create_document
from db.cloudant_interface import create_cloudant_db
from db.cloudant_interface import disconnect_cloudant

from db.db2_interface import connect_db2
from db.db2_interface import close_db2

logging.basicConfig(level=logging.INFO)

def init_app():
    app = Flask(__name__)
    port = os.getenv('PORT', 5000)
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=int(port))

    return app

app = init_app()

@app.before_first_request
def init_databases():
    is_cloudant_enabled = os.getenv("cloudant_enabled")
    print("cloudant_enabled : ", is_cloudant_enabled)
    if is_cloudant_enabled:
        connect_cloudant()
        create_cloudant_db("config_db")

    is_db2_enabled = os.getenv("db2_enabled")
    print("db2_enabled : ", is_db2_enabled)
    if is_db2_enabled:
        connect_db2("eventsdb")

@atexit.register
def shutdown():
    disconnect_cloudant()
    close_db2()

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
    create_document(request_body)

    return make_response('', 201)

@app.route('/model/events')
def get_events_count():
    evts = get_event_info()
    memory_mbs = evts[1]/(1024*1024)
    return json.dumps({
        "eventsCount": evts[0],
        "memoryUsage": str(memory_mbs)+"MB"
    })
