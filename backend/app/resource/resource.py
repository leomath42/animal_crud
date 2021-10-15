#!/usr/bin/env python3
from http import HTTPStatus

from app.model.model import Animal, AnimalValidator, Pagination
from flask import Blueprint, jsonify, make_response, request, render_template, render_template_string
from flask_mongoengine.wtf import model_form
from mongoengine import DoesNotExist
from flask_cors import cross_origin

# from flask_paginate import Pagination, get_page_parameter
#from flask_mongoengine.pagination import Pagination
animal = Blueprint('animal', __name__, url_prefix='/animal')

animalForm = model_form(Animal)


@animal.route("/")
def get_all_paged():
    #x = Pagination.page(Animal, AnimalValidator, 0, 2)
    x = Pagination.page_from_request(request, Animal, AnimalValidator)
    body = x.to_json()
    response = make_response(body, 200)
    response.headers['Content-Type'] = "application/json"
    return response


@animal.route("/<string:_id>", methods=["GET"])
def get(_id):
    try:
        animal = Animal.objects.get(id=_id)  # , many=True)
        body = jsonify(AnimalValidator().dump(animal))
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
    json = request.get_json()
    print("################")
    animal = AnimalValidator().load(json).save()
    print("################")
    body = jsonify(AnimalValidator().dump(animal))
    response = make_response(body, HTTPStatus.CREATED)
    response.headers['Content-Type'] = "application/json"
    return response


@animal.route("/<string:_id>", methods=["PUT"])
def put(_id):
    try:
        json = request.get_json()
        animal_aux = AnimalValidator().load(json)
        Animal.objects(id=_id).update(**animal_aux.to_mongo())
        animal = Animal.objects.get(id=_id)
        # animal = Animal.objects(id=_id)
        # animal = AnimalValidator().update(animal, json)
        body = jsonify(AnimalValidator().dump(animal))
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
        animal = Animal.objects.get(id=_id).delete()

        body = str(animal)  # animal.to_json()
        response = make_response(body, HTTPStatus.NO_CONTENT)
        response.headers['Content-Type'] = "application/json"
        return response
    except DoesNotExist:
        response = make_response(
            "Doesn't exist object with id '{0}'".format(_id),
            HTTPStatus.NOT_FOUND
        )
        return response
