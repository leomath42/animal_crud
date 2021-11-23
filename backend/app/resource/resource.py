#!/usr/bin/env python3
from http import HTTPStatus

from app.model.model import Animal, AnimalValidator, Pagination
from flask import Blueprint, jsonify, make_response, request
from flask_mongoengine.wtf import model_form
from marshmallow import ValidationError
from mongoengine import DoesNotExist
from werkzeug.exceptions import HTTPException
import json

from app.containers import Container
from dependency_injector.wiring import Provide, inject
from app.service.service import AnimalService

# from flask_paginate import Pagination, get_page_parameter
#from flask_mongoengine.pagination import Pagination
animal = Blueprint('animal', __name__, url_prefix='/animal')

animalForm = model_form(Animal)

animal_service = AnimalService(Animal, AnimalValidator, Pagination)


@animal.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@animal.route("/")
def get_all_paged():
    #x = Pagination.page(Animal, AnimalValidator, 0, 2)
    x = Pagination.page_from_request(request, Animal, AnimalValidator)
    body = x.to_json()
    response = make_response(body, HTTPStatus.OK)
    response.headers['Content-Type'] = "application/json"
    return response


@animal.route("/<string:_id>", methods=["GET"])
def get(_id):

    try:
        animal = animal_service.find_by_id(id=_id)
        animal = animal_service.dump(animal)
        body = jsonify(animal)

        response = make_response(body, HTTPStatus.OK)
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
    json = request.get_json()
    animal = animal_service.load(json)
    animal = animal_service.save(animal)
    animal = animal_service.dump(animal)
    body = jsonify(animal)

    response = make_response(body, HTTPStatus.CREATED)
    response.headers['Content-Type'] = "application/json"
    return response


@animal.route("/<string:_id>", methods=["PUT"])
def put(_id):
    try:

        json = request.get_json()
        animal = animal_service.load(json)
        animal = animal_service.update(_id, animal)
        animal = animal_service.dump(animal)

        body = jsonify(animal)
        response = make_response(body, HTTPStatus.OK)
        response.headers['Content-Type'] = "application/json"
        return response

    except DoesNotExist:
        response = make_response(
            "Doesn't exist object with id '{0}'".format(_id),
            HTTPStatus.NOT_FOUND
        )
        return response


@animal.route("/<string:_id>", methods=["DELETE"])
def delete(_id):
    try:
        # raise DoesNotExist when _id not found
        animal_service.delete(_id)

        body = jsonify(None)
        response = make_response(body, HTTPStatus.NO_CONTENT)
        response.headers['Content-Type'] = "application/json"
        return response
    except DoesNotExist:
        response = make_response(
            "Doesn't exist object with id '{0}'".format(_id),
            HTTPStatus.NOT_FOUND
        )
        return response
