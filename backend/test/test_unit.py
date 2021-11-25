from http import HTTPStatus
import unittest
import unittest.mock
from unittest.mock import MagicMock, Mock, patch

from flask import Flask, request, jsonify
from app import create_app, registre_blueprints, init_database
from app.model.model import Animal
from mongoengine.document import Document
from mongoengine.errors import DoesNotExist, ValidationError

from werkzeug.test import Client
from werkzeug.exceptions import NotFound, UnprocessableEntity, BadRequest
from werkzeug.testapp import test_app
from mongoengine import connect, disconnect
from datetime import date
from bson.objectid import ObjectId
from app.resource.resource import delete
import json


class TestResource(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.app = create_app()
        registre_blueprints(cls.app)

    @classmethod
    def tearDownClass(cls) -> None:
        disconnect()

    def setUp(self) -> None:
        self.id_exist = '619bd05b20c5f552ce95e28a'
        self.id_does_not_exist = '619bd70920c5f552ce95e28b'
        self.id_invalid = 0

        def side_effect(id):
            if id == self.id_exist:
                return Animal()
            elif id == self.id_does_not_exist:
                raise DoesNotExist()

        self.animal_dict_valid = {
            "id": self.id_exist,
            "data_nascimento": "10/10/2021",
            "nome": "dog",
            "peso": 60,
            "tipo": "cachorro"
        }

        self.animal_dict_valid_doest_not_exist = {
            "id": self.id_does_not_exist,
            "data_nascimento": "10/10/2021",
            "nome": "dog",
            "peso": 60,
            "tipo": "cachorro"
        }

        self.animal_dict_invalid = {
            "id": "619bd05b20c5f552ce95e28a",
            "data_nascimento": "invalido",
            "nome": "dog",
            "peso": 60,
            "tipo": "cachorro"
        }

        self.animal_valid = Animal(**self.animal_dict_valid)
        self.animal_invalid = Animal(**self.animal_dict_invalid)
        self.animal_valid_doest_not_exist = Animal(
            **self.animal_dict_valid_doest_not_exist)

        def dump_side_effect(animal: Animal):

            if animal == self.animal_valid:
                return self.animal_dict_valid

            elif animal == self.animal_dict_valid_doest_not_exist:
                return self.animal_valid_doest_not_exist

            elif animal == self.animal_invalid:
                raise ValidationError()

        def load_side_effect(animal: str):

            if animal == self.animal_dict_valid:
                return self.animal_valid

            elif animal == self.animal_dict_valid_doest_not_exist:
                return self.animal_valid_doest_not_exist

            elif animal == self.animal_dict_invalid:
                raise ValidationError()

        def save_side_effect(animal: Animal) -> Animal:
            animal.id = str(ObjectId())

            return animal

        def update_side_effect(id: int, animal: Animal) -> Animal:
            if id == self.id_exist:
                return animal
            elif id == self.id_does_not_exist:
                raise DoesNotExist()

        self.animal_service = MagicMock()
        self.animal_service.delete.side_effect = side_effect
        self.animal_service.find_by_id.side_effect = side_effect

        self.animal_service.save.side_effect = save_side_effect

        self.animal_service.update.side_effect = update_side_effect

        self.animal_service.dump.side_effect = dump_side_effect
        self.animal_service.load.side_effect = load_side_effect

        self.app = self.build_app(self.animal_service)

    def build_app(self, animal_service: MagicMock) -> Flask:
        import app.resource.resource as resource
        resource.animal_service = animal_service

        app = create_app()
        app.register_blueprint(resource.animal)

        return app

    def test_get_animal_when_id_exist(self) -> None:

        with self.app.test_client() as c:

            response = c.get('/animal/{0}'.format(self.id_exist))
            data = response.data
            self.animal_service.find_by_id.assert_called_once()
            self.assertEqual(response.status_code, HTTPStatus.OK)
            self.assertIsNotNone(data)

    def test_get_animal_when_id_not_exist(self) -> None:

        with self.app.test_client() as c:

            response = c.get('/animal/{0}'.format(self.id_does_not_exist))
            data = response.data
            self.animal_service.find_by_id.assert_called_once()
            self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
            self.assertIsNotNone(data)

    def test_delete_animal_when_id_exist(self):

        with self.app.test_client() as c:
            response = c.delete('/animal/{0}'.format(self.id_exist))
            self.animal_service.delete.assert_called()
            self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)

    def test_delete_animal_when_id_not_exist(self):

        with self.app.test_client() as c:
            response = c.delete('/animal/{0}'.format(self.id_does_not_exist))
            self.animal_service.delete.assert_called()
            self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_post_animal_when_data_valid(self):

        with self.app.test_client() as c:
            response = c.post('/animal/', json=self.animal_dict_valid)
            self.animal_service.save.assert_called()
            self.animal_service.dump.assert_called()
            self.animal_service.load.assert_called()
            self.assertEqual(response.status_code, HTTPStatus.CREATED)

    # Falha -> ValidationError
    def test_post_animal_when_data_invalid(self):

        with self.app.test_client() as c:
            response = c.post('/animal/', json=self.animal_dict_invalid)
            self.animal_service.save.assert_called()
            self.animal_service.dump.assert_called()
            self.animal_service.load.assert_called()
            self.assertEqual(response.status_code,
                             HTTPStatus.UNPROCESSABLE_ENTITY)

    def test_put_animal_when_data_valid(self):
        with self.app.test_client() as c:
            response = c.put(
                '/animal/{0}'.format(self.id_exist), json=self.animal_dict_valid)
            self.animal_service.update.assert_called()
            self.animal_service.dump.assert_called()
            self.animal_service.load.assert_called()
            self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_put_animal_when_id_not_exist(self):
        with self.app.test_client() as c:

            response = c.put('/animal/{0}'.format(self.id_does_not_exist),
                             json=self.animal_dict_valid_doest_not_exist)

            self.animal_service.update.assert_called()
            self.animal_service.load.assert_called()
            self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    # Falha -> ValidationError
    def test_put_animal_when_data_invalid(self):
        with self.app.test_client() as c:
            response = c.put(
                '/animal/{0}'.format(self.id_exist), json=self.animal_dict_invalid)
            self.animal_service.update.assert_called()
            self.animal_service.dump.assert_called()
            self.animal_service.load.assert_called()
            self.assertEqual(response.status_code,
                             HTTPStatus.UNPROCESSABLE_ENTITY)


class TestService(unittest.TestCase):

    def setUp(self) -> None:
        from app.service.service import AnimalService
        self.model = Mock()
        self.model_validator = Mock()
        self.pagination = Mock()

        self.animal_service = AnimalService(
            model=self.model,
            model_validator=self.model_validator,
            pagination=self.pagination
        )

        self.id_exist = '619bd05b20c5f552ce95e28a'
        self.id_does_not_exist = '619bd70920c5f552ce95e28b'
        self.id_invalid = 0

        self.animal_dict_valid = {
            "id": self.id_exist,
            "data_nascimento": "10/10/2021",
            "nome": "dog",
            "peso": 60,
            "tipo": "cachorro"
        }

        self.animal_valid = Animal(**self.animal_dict_valid)

        def get_side_effect(id: str) -> Animal:
            if id == self.id_exist:
                return Animal(**self.animal_dict_valid)
            elif not ObjectId.is_valid(id):
                raise ValidationError()
            elif id != self.id_exist:
                raise DoesNotExist()

        def update_side_effect(upsert=False, multi=True, write_concern=None, read_concern=None, full_result=False, **update) -> Animal:
            return Mock()

        def objects_side_effect(id: int):
            if id == self.id_does_not_exist:
                raise DoesNotExist()
            elif not ObjectId.is_valid(id):
                raise ValidationError()
            else:
                m = Mock()
                m.update.side_effect = update_side_effect
                return m

        def load_side_effect(animalJson: dict) -> Animal:
            if animalJson == self.animal_dict_valid:
                return self.animal_valid
            else:
                raise ValidationError()

        def dump_side_effect(animal: Animal) -> str:
            if animal == self.animal_valid:
                return self.animal_dict_valid
            else:
                raise ValidationError()

        def delete_side_effect(id: int) -> None:
            if id == self.id_exist:
                return None
            else:
                raise DoesNotExist()

        self.model.objects.get.side_effect = get_side_effect
        self.model.objects.side_effect = objects_side_effect
        self.model.objects.update.side_effect = update_side_effect

        self.model.objects.delete.side_effect = delete_side_effect

        def model_validator_side_effect():
            m = Mock()
            m.dump.side_effect = dump_side_effect
            m.load.side_effect = load_side_effect
            return m

        self.model_validator.side_effect = model_validator_side_effect
        self.model_validator.side_effect = model_validator_side_effect

    def test_find_by_id_when_valid(self):
        animal = self.animal_service.find_by_id(self.id_exist)
        self.assertIsNotNone(animal)
        self.assertTrue(isinstance(animal, Document))
        self.assertTrue(isinstance(animal, Animal))

    # falha
    def test_find_by_id_when_not_exist(self):

        with self.assertRaises(NotFound):
            self.animal_service.find_by_id(self.id_does_not_exist)

    # falha
    def test_find_by_id_when_invalid(self):

        with self.assertRaises(BadRequest):
            self.animal_service.find_by_id(self.id_invalid)

    @patch('app.model.model.Animal')
    def test_save_animal_when_valid_data(self, animal: MagicMock):
        animal.save.return_value = Animal()

        animal = self.animal_service.save(animal)
        self.assertIsNotNone(animal)
        self.assertTrue(isinstance(animal, Animal))

    # falha
    def test_save_animal_when_invalid_data(self):

        with self.assertRaises(TypeError):
            animal = self.animal_service.save(dict())

        with self.assertRaises(TypeError):
            animal = self.animal_service.save(int())

    def test_update_animal_when_valid_data(self):

        animal = self.animal_service.update(self.id_exist, self.animal_valid)
        self.assertIsNotNone(animal)
        self.assertTrue(isinstance(animal, Animal))

    # falha
    def test_update_animal_when_invalid_data(self):

        with self.assertRaises(TypeError):
            animal = self.animal_service.update(
                self.id_exist, dict())

        with self.assertRaises(TypeError):
            animal = self.animal_service.update(
                self.id_exist, int())

    # Falha
    def test_update_animal_when_id_invalid(self):

        with self.assertRaises(BadRequest):
            self.animal_service.update(
                self.id_invalid, self.animal_valid)

    # Falha
    def test_update_animal_id_when_not_exist(self):

        with self.assertRaises(NotFound):
            self.animal_service.update(
                self.id_does_not_exist, self.animal_valid)

    def test_delete_when_id_exist(self):
        def delete_side_effect(id: int) -> None:
            if id == self.id_exist:
                return None
            else:
                raise DoesNotExist()

        model = Mock()
        model.objects.get.delete.side_effect = delete_side_effect

        self.animal_service.model = model

        try:
            aux = self.animal_service.delete(self.id_exist)
            self.assertIsNone(aux)
        except:
            self.fail('animal_service raised an unexpected Exception !')

    # Falha
    def test_delete_when_id_not_exist(self):

        with self.assertRaises(NotFound):
            self.animal_service.delete(self.id_does_not_exist)

    # Falha
    def test_delete_when_id_invalid(self):
        with self.assertRaises(BadRequest):
            self.animal_service.delete(self.id_invalid)

    def test_load_when_valid(self):
        animal = self.animal_service.load(self.animal_dict_valid)
        self.assertIsNotNone(animal)
        self.assertTrue(isinstance(animal, Animal))

    def test_load_when_invalid(self):
        with self.assertRaises(ValidationError):
            # passa qualquer coisa que não seja valida para testar
            self.animal_service.load(dict())

    def test_dump_when_valid(self):
        animal_json = self.animal_service.dump(self.animal_valid)
        self.assertIsNotNone(animal_json)
        self.assertEqual(type(animal_json), dict)

    def test_dump_when_invalid(self):
        with self.assertRaises(ValidationError):
            # passa qualquer coisa que não seja valida para testar
            self.animal_service.dump(dict())


if __name__ == '__main__':
    unittest.main()
