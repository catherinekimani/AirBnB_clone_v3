#!/usr/bin/python3
""" Returns a Json Response """

from flask import jsonify, Blueprint
from api.v1.views import app_views
from models import storage


@app_views.route('/status', strict_slashes=False)
def returnstuff():
    return jsonify(status='OK')


@app_views.route('/stats', strict_slashes=False)
def stuff():
    stats_obj = {
        'states': State, 'users': User,
        'amenities': Amenity, 'cities': City,
        'places': Place, 'reviews': Review
    }
    for key in stats_obj:
        stats_obj[key] = storage.count(stats_obj[key])
    return jsonify(stats_obj)
