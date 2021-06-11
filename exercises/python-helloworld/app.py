from flask import Flask, Response, request
import logging

app = Flask(__name__)
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format= '%(asctime)s, %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S'
)

@app.route("/")
def hello():
    return "Hello developer!"

@app.route("/status")
def status():
    app.logger.info(f'{request.path} endpoint was reached')
    return Response('{"result": "OK - healthy"}', status=200, mimetype='application/json')

@app.route("/metrics")
def metrics():
    app.logger.info(f'{request.path} endpoint was reached')
    return Response('{"data": {"UserCount": 140, "UserCountActive": 23}}', status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
