#!/usr/bin/python3

from flask import Flask
from models import storage
from api.v1.views import app_views
# from flask_cors import CORS
from flask import jsonify
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def downtear(self):
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    return jsonify("error': 'Not found"), 404


if __name__ == "__main__":
    if getenv('HBNB_API_HOST'):
        host = getenv('HBNB_API_HOST')
    else:
        host = '0.0.0.0'
    if getenv('HBNB_API_PORT'):
        port = getenv('HBNB_API_PORT')
    else:
        port = 5000
    app.run(host=host, port=port, threaded=True)
