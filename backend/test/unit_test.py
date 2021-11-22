from http import HTTPStatus
import unittest
import unittest.mock
from unittest.mock import patch
from app.resource.resource import animal
from flask import Flask, request, jsonify
from app import create_app, registre_blueprints, init_database
from app.model.model import Animal
from mongoengine.errors import DoesNotExist

from werkzeug.test import Client
from werkzeug.testapp import test_app
from mongoengine import connect, disconnect
from datetime import date
from bson.objectid import ObjectId


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.app = create_app()
        registre_blueprints(cls.app)

    @classmethod
    def tearDownClass(cls) -> None:
        disconnect()

    def when_id_side_effect(self):
        existing_id = ObjectId('619bd05b20c5f552ce95e28a')
        not_valid_id = 0
        does_not_exist_id = ObjectId('619bd70920c5f552ce95e28b')

        def side_effect(id):
            if type(ObjectId(id)) != ObjectId:
                raise Exception()
            elif ObjectId(id) == existing_id:
                return Animal()
            elif ObjectId(id) != existing_id:
                raise DoesNotExist('')
            else:
                raise Exception()

        return side_effect

    @patch('app.service.service.AnimalService')
    def test_get_animal_when_id_does_exist(self, animal_service_mock) -> None:
        existing_id = '619bd05b20c5f552ce95e28a'

        animal_service_mock.find_by_id.side_effect = self.when_id_side_effect()

        with self.__class__.app.test_client() as c, self.__class__.app.container.animal_service.override(animal_service_mock):

            response = c.get('/animal/{0}'.format(existing_id))
            data = response.data
            self.assertEqual(response.status_code, HTTPStatus.OK)
            self.assertIsNotNone(data)

    @patch('app.service.service.AnimalService')
    def test_get_animal_when_id_does_not_exist(self, animal_service_mock) -> None:
        does_not_exist_id = '619bd70920c5f552ce95e28b'

        animal_service_mock.find_by_id.side_effect = self.when_id_side_effect()

        with self.__class__.app.test_client() as c, self.__class__.app.container.animal_service.override(animal_service_mock):

            response = c.get('/animal/{0}'.format(does_not_exist_id))
            data = response.data
            self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
            self.assertIsNotNone(data)

    @patch('app.service.service.AnimalService')
    def test_get_animal_when_invalid_id(self, animal_service_mock) -> None:
        not_valid_id = 0

        animal_service_mock.find_by_id.side_effect = self.when_id_side_effect()

        with self.__class__.app.test_client() as c, self.__class__.app.container.animal_service.override(animal_service_mock):

            response = c.get('/animal/{0}'.format(not_valid_id))
            data = response.data
            self.assertEqual(response.status_code,
                             HTTPStatus.INTERNAL_SERVER_ERROR)
            self.assertIsNotNone(data)


if __name__ == '__main__':
    unittest.main()
