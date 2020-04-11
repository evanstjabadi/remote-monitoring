from datetime import datetime


from flask import Blueprint, jsonify, request, send_file
from sqlalchemy.orm import joinedload

from random.app import db
from random.models import Random
from random.schemas import random_schema


api = Blueprint("api", "api")


@api.route("/random/", methods=["POST"])
def add_random():
    time_stamb = request.json["time_stamb"]
    value = request.json["value"]
    new_random = Random(time_stamb=time_stamb, value=value)
    db.session.add(new_random)
    db.session.commit()
    return random_schema.jsonify(new_random)


@api.route("/random/", methods=["GET"])
def get_randoms():
    randoms = Random.query.all()
    result = random_schema.dump(randoms, many=True)
    return jsonify(result)


@api.route("/random/<id>", methods=["GET"])
def get_random(id):
    random = Random.query.get(id)
    return random_schema.jsonify(random)


@api.route("/random/<id>", methods=["DELETE"])
def delete_random(id):
    random = Random.query.get(id)
    db.session.delete(random)
    db.session.commit()
    return Random.jsonify(random)
