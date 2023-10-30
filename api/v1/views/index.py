#!/usr/bin/python3
""" Returns a Json Response """

from flask import jsonify, Blueprint
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Return Status code """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def object_stats():
    """Retrieves the no of each object by type"""
    objects = {
        "amenities": storage.count('Amenity'),
        "cities": storage.count('City'),
        "places": storage.count('Place'),
        "reviews": storage.count('Review'),
        "states": storage.count('State'),
        "users": storage.count('User'),
    }
    return jsonify(objects)
