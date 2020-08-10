import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict


location = Blueprint('locations', 'location')

@location.route('/', methods=['GET'])
def get_locations():
    return jsonify(data={}, status={'code':200, 'message': 'succesful get route'})

@location.route('/', methods=["POST"])
def save_location():
    payload = request.get_json()
    location = models.Location.create(**payload)
    return jsonify(data=model_to_dict(location), status={'code': 200, 'message':'success'})

@location.route('/<id>', methods=["GET"])
def get_one_location(id):
    location = models.Location.get_by_id(id)
    return jsonify(data=model_to_dict(location), status={'code': 200, 'message': 'success'})

@location.route('/<id>', methods=["PUT"])
def update_location(id):
    payload = request.get_json()
    update_query = models.Location.update(**payload).where(models.Location.id == id)
    update_query.execute()
    updated_location = models.Location.get_by_id(id)
    return jsonify(data=updated_location, message="succesfully updated location with id {}".format(id), status={'code': 200, 'message': "Success"})


@location.route('/<id>', methods=['DELETE'])
def delete_location(id):
    delete_query = models.Location.delete().where(models.Location.id == id)
    delete_query.execute()
    return jsonify(data={}, message="Succefully deleted location with id{}".format(id), status={'code': 200, 'message': 'Success'})