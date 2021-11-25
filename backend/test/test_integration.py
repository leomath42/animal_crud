from http import HTTPStatus
import unittest
import unittest.mock
from unittest.mock import patch
from app.resource.resource import animal
from flask import Flask, request, jsonify
from app import create_app, registre_blueprints, init_database
from app.model.model import Animal
from mongoengine.document import Document

from werkzeug.test import Client
from werkzeug.testapp import test_app
from mongoengine import connect, disconnect
from datetime import date
from bson.objectid import ObjectId


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.app = create_app()
        registre_blueprints(self.app)
        init_database(self.app)

        Document.save(
            {
                "id": "6197e0c5902bd4c1e75ba3f6",
                "data_nascimento": "10/10/2021",
                "nome": "dog",
                "peso": 60,
                "tipo": "cachorro"
            }
        )

    def tearDown(self) -> None:
        disconnect()

    def test_get_animal_when_id_does_not_exist(self) -> None:

        with self.app.test_client() as c:
            response = c.get('/animal/6197e0c5902bd4c1e75ba3f6')
            data = response.data
            self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
            self.assertIsNotNone(data)

    def test_get_animal_when_id_exist(self) -> None:

        with self.app.test_client() as c:
            response = c.get('/animal/6197e0c5902bd4c1e75ba3f6')
            data = response.data
            self.assertEqual(response.status_code, HTTPStatus.OK)
            self.assertIsNotNone(data)

    def test_post_animal(self):

        with self.app.test_client() as c:
            animal = {"nome": 'test', "peso": 5, "tipo": 'test',
                      "data_nascimento": '2021-11-19T00:00:00'}
            response = c.post('/animal/', json=animal)
            data = response.json

            self.assertEqual(response.status_code, HTTPStatus.CREATED)
            self.assertIsNotNone(data['id'])


if __name__ == '__main__':
    unittest.main()
