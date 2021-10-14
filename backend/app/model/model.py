import marshmallow_mongoengine as ma
from marshmallow import fields
from mongoengine import DateField, Document, FloatField, StringField


class Animal(Document):
    data_nascimento = DateField(required=True)
    nome = StringField(max_length=4, required=True)
    peso = FloatField(required=True)
    tipo = StringField(required=True)


class AnimalValidator(ma.ModelSchema):
    class Meta:
        model = Animal
    data_nascimento = fields.Date('%Y-%m-%dT%H:%M:%S%z', required=True)
