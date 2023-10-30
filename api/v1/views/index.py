#!/usr/bin/python3
""" Returns a Json Response """

from flask import jsonify, Blueprint
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    return jsonify({"status": "OK"})
