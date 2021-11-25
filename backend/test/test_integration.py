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
from mongoengine import connect, disconnect, get_connection
from datetime import date
from bson.objectid import ObjectId


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.app = create_app()
        registre_blueprints(self.app)
        init_database(self.app)

        # SEED DATABASE INICIO
        animal_dict_1 = {
            "id": "619bd05b20c5f552ce95e28a",
            "data_nascimento": "10/10/2021",
            "nome": "Caramelo",
            "peso": 7.0,
            "tipo": "cachorro"
        }

        animal_dict_2 = {
            "id": "6197e0c5902bd4c1e75ba3f6",
            "data_nascimento": "09/10/2021",
            "nome": "Mel",
            "peso": 5,
            "tipo": "gato"
        }
        animal_dict_3 = {
            "id": "6197e0c5902bd4c1e75ba3f7",
            "data_nascimento": "08/10/2021",
            "nome": "cusco",
            "peso": 0.2,
            "tipo": "hamster"
        }
        animal_1 = Animal(**animal_dict_1)
        animal_2 = Animal(**animal_dict_2)
        animal_3 = Animal(**animal_dict_3)
        Animal.objects.insert([animal_1, animal_2, animal_3])
        # SEED DATABASE FIM

    def tearDown(self) -> None:
        from app import database
        con = database.get_connection()
        con.drop_database('test')

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
