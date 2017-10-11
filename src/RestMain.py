from flask import Flask
app = Flask(__name__)

@app.route('/health')
def healthCheck():
    return 'Health - OK'

@app.route('/')
def appRoute():
    return 'OK'
