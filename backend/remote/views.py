from datetime import datetime


from flask import Blueprint, jsonify, request, send_file
from sqlalchemy.orm import joinedload

from remote.app import db
from remote.models import remote
from remote.schemas import remote_schema


api = Blueprint("api", "api")


@api.route("/remote/", methods=["POST"])
def add_remote():
    time_stamb = request.json["time_stamb"]
    value = request.json["value"]
    new_remote = remote(time_stamb=time_stamb, value=value)
    db.session.add(new_remote)
    db.session.commit()
    return remote_schema.jsonify(new_remote)


@api.route("/remote/", methods=["GET"])
def get_remotes():
    remotes = remote.query.all()
    result = remote_schema.dump(remotes, many=True)
    return jsonify(result)


@api.route("/remote/<id>", methods=["GET"])
def get_remote(id):
    remote = remote.query.get(id)
    return remote_schema.jsonify(remote)


@api.route("/remote/<id>", methods=["DELETE"])
def delete_remote(id):
    remote = remote.query.get(id)
    db.session.delete(remote)
    db.session.commit()
    return remote.jsonify(remote)
