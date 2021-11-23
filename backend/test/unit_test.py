from http import HTTPStatus
import unittest
import unittest.mock
from unittest.mock import MagicMock, Mock, patch

from flask import Flask, request, jsonify
from app import create_app, registre_blueprints, init_database
from app.model.model import Animal
from mongoengine.errors import DoesNotExist, ValidationError

from werkzeug.test import Client
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

        def dump_side_effect(animal: Animal) -> dict:
            return dict()

        self.animal_service = MagicMock()
        self.animal_service.delete.side_effect = side_effect
        self.animal_service.find_by_id.side_effect = side_effect

        self.animal_service.dump.side_effect = dump_side_effect

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


if __name__ == '__main__':
    unittest.main()
