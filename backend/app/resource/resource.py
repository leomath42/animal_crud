#!/usr/bin/env python3
from flask import Blueprint

animal = Blueprint('animal', __name__, url_prefix='/animal')


@animal.route("/")
def get_all_paged():
    pass


@animal.route("/")
def get():
    pass


@animal.route("/")
def post():
    pass


@animal.route("/")
def put():
    pass


@animal.route("/")
def delete():
    pass
