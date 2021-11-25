from app.model.model import Animal, AnimalValidator, Pagination

from app.model.model import Model, ModelValidator
# from abc import ABC, abstractmethod
from flask import jsonify


class Service(object):
    def __init__(self, model: Model, model_validator: ModelValidator,
                 pagination: Pagination):
        self.model = model
        self.model_validator = model_validator
        self.pagination = pagination


class AnimalService(Service):

    def __init__(self, model: Model, model_validator: ModelValidator, pagination: Pagination):
        super().__init__(model, model_validator, pagination)

    def find_by_id(self, id: int) -> Animal:
        return self.model.objects.get(id=id)

    def save(self, animal: Animal) -> Animal:
        animal = animal.save()
        return animal

    def update(self, id: int, animal: Animal) -> Animal:
        # Animal.objects(id=_id).update(**animal_aux.to_mongo())
        self.model.objects(id).update(**animal.to_mongo())
        animal = self.model.objects.get(id)
        return animal

    def delete(self, id: int) -> Animal:
        self.model.objects.get(id=id).delete()

    def load(self, json: str) -> Animal:
        return self.model_validator().load(json)

    def dump(self, animal: Animal) -> str:
        return self.model_validator().dump(animal)
