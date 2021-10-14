#!/usr/bin/env python3
from http import HTTPStatus

from app.model.model import Animal, AnimalValidator
from flask import Blueprint, jsonify, make_response, request
from flask_mongoengine.wtf import model_form
from mongoengine import DoesNotExist

animal = Blueprint('animal', __name__, url_prefix='/animal')

animalForm = model_form(Animal)


@animal.route("/")
def get_all_paged():
    Animal.objects.get_all_paged(10)


@animal.route("/<string:_id>", methods=["GET"])
def get(_id):
    try:
        animal = Animal.objects.get(id=_id)
        body = animal.to_json()
        response = make_response(body, 200)
        response.headers['Content-Type'] = "application/json"
        return response
    except DoesNotExist:
        response = make_response(
            "Doesn't exist object with id '{0}'".format(_id),
            HTTPStatus.NOT_FOUND
        )
        return response


@animal.route("/", methods=["POST"])
def post():
    pass


@animal.route("/")
def put():
    pass


@animal.route("/")
def delete():
    pass
