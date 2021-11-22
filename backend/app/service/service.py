from app.model.model import Animal, AnimalValidator, Pagination

from app.model.model import Model, ModelValidator
# from abc import ABC, abstractmethod
from flask import jsonify


class Service(object):

    def __init__(self, model: Model, model_validator: ModelValidator,
                 pagination: Pagination):
        pass

    def find_by_id(self, id: int) -> Model:
        pass


class AnimalService(Service):

    def find_by_id(self, id: int) -> Animal:
        return Animal.objects.get(id)

    def save(self, animal: str) -> Animal:
        animal = AnimalValidator().load(animal).save()
        return animal
