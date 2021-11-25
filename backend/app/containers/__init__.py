from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from app.model.model import Animal, AnimalValidator, Pagination, Model, ModelValidator
from app.service.service import Service, AnimalService


class Container(containers.DeclarativeContainer):
    service = providers.Factory(
        Service,
        model=Model,
        model_validator=ModelValidator,
        pagination=Pagination
    )

    animal_service = providers.Factory(
        AnimalService,
        model=Animal,
        model_validator=AnimalValidator,
        pagination=Pagination
    )
