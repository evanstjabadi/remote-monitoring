from datetime import datetime


from flask import Blueprint, jsonify, request, send_file
from sqlalchemy.orm import joinedload

from remote.app import db
from remote.models import random
from remote.schemas import random_schema


api = Blueprint("api", "api")


@api.route("/random/", methods=["POST"])
def add_random():
    time_stamb = request.json["time_stamb"]
    value = request.json["value"]
    new_random = random(time_stamb=time_stamb, value=value)
    db.session.add(new_random)
    db.session.commit()
    return random_schema.jsonify(new_random)


@api.route("/random/", methods=["GET"])
def get_randoms():
    randoms = random.query.all()
    result = random_schema.dump(randoms, many=True)
    return jsonify(result)


@api.route("/random/<id>", methods=["GET"])
def get_random(id):
    random = random.query.get(id)
    return random_schema.jsonify(random)


@api.route("/random/<id>", methods=["DELETE"])
def delete_random(id):
    random = random.query.get(id)
    db.session.delete(random)
    db.session.commit()
    return random.jsonify(random)
