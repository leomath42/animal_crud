from app.model.model import Animal, AnimalValidator, Pagination

from app.model.model import Model, ModelValidator
# from abc import ABC, abstractmethod


class Service(object):

    def __init__(self, model: Model, model_validator: ModelValidator,
                 pagination: Pagination):
        pass

    def find_by_id(self, id: int) -> Model:
        pass


class AnimalService(Service):

    def find_by_id(self, id: int) -> Animal:
        return super().find_by_id(id)
