import marshmallow_mongoengine as ma
from marshmallow import fields
from mongoengine import DateField, Document, FloatField, StringField
import json


class Animal(Document):
    data_nascimento = DateField(required=True)
    nome = StringField(max_length=4, required=True)
    peso = FloatField(required=True)
    tipo = StringField(required=True)


class AnimalValidator(ma.ModelSchema):
    class Meta:
        model = Animal
    data_nascimento = fields.Date('%Y-%m-%dT%H:%M:%S%z', required=True)


class Pagination(object):
    # default values of pagination
    page_number = 0
    page_size = 10

    class Page(object):
        def __init__(self, content, page_number, page_size):
            self.content = content
            self.page_number = page_number
            self.page_size = page_size

        def to_json(self):
            return json.dumps(self.__dict__)

    @classmethod
    def page(cls, cls_document, cls_validator, page_number, page_size):
        count = cls_document.objects.count()
        content = cls_document.objects.skip(page_number).limit(page_size)
        content_validated = cls_validator(many=True).dump(content)
        page = cls.Page(content_validated, page_number, page_size)

        return page

    @classmethod
    def page_from_request(cls, request, cls_document, cls_validator):
        page = request.form.get('page', type=int)
        size = request.form.get('size', type=int)

        page_number = page if page else cls.page_number
        page_size = size if size else cls.page_size

        return cls.page(cls_document, cls_validator, page_number, page_size)
