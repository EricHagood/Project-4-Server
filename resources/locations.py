import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict


location = Blueprint('locations', 'location')

@location.route('/', methods=['GET'])
def get_locations():
    return jsonify(data={}, status={'code':200, 'message': 'succesful get route'})