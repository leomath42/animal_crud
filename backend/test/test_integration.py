from http import HTTPStatus
import unittest
import unittest.mock
from unittest.mock import patch
from app import create_app, registre_blueprints, init_database
from app.model.model import Animal

from datetime import date
from bson.objectid import ObjectId


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.app = create_app()
        registre_blueprints(self.app)

        # Derruba o banco de dados de testes, caso ainda exista alguma conexão após um erro inesperado.
        self.drop_database()

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

        self.animal_update_dict_test = animal_dict_1

    def tearDown(self) -> None:
        self.drop_database()

    def drop_database(self):
        try:
            from app import database
            con = database.get_connection()
            con.drop_database('test')
        except:
            pass

    def test_get_animal_when_id_exist(self) -> None:

        with self.app.test_client() as c:
            response = c.get('/animal/6197e0c5902bd4c1e75ba3f6')
            data = response.data
            self.assertEqual(response.status_code, HTTPStatus.OK)
            self.assertIsNotNone(data)

    def test_get_animal_when_id_does_not_exist(self) -> None:

        with self.app.test_client() as c:
            response = c.get('/animal/6197e0c5902bd4c1e75ba3f0')
            data = response.data
            self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
            self.assertIsNotNone(data)

    def test_delete_animal_when_invalid_id(self):
        with self.app.test_client() as c:
            response = c.delete('/animal/0')
            data = response.data
            self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_animal_when_valid_data(self):

        with self.app.test_client() as c:
            size_collection_before_insert = len(Animal.objects)
            animal = {"nome": 'test', "peso": 5, "tipo": 'test',
                      "data_nascimento": '2021-11-19T00:00:00'}
            response = c.post('/animal/', json=animal)
            data = response.json

            self.assertEqual(response.status_code, HTTPStatus.CREATED)
            self.assertEqual(size_collection_before_insert +
                             1, len(Animal.objects))
            self.assertIsNotNone(data['id'])

    def test_post_animal_when_invalid_data(self):

        with self.app.test_client() as c:
            size_collection_before_insert = len(Animal.objects)
            animal = {"nome": 'test', "peso": 5, "tipo": 'test',
                      "data_nascimento": 'AAAAAAA'}
            response = c.post('/animal/', json=animal)
            data = response.json

            self.assertEqual(response.status_code,
                             HTTPStatus.UNPROCESSABLE_ENTITY)
            # self.assertEqual(size_collection_before_insert + 1, 4)
            # self.assertIsNotNone(data['id'])

    def test_put_animal_when_valid_data(self):

        with self.app.test_client() as c:
            size_collection_before_insert = len(Animal.objects)
            animal = self.animal_update_dict_test
            animal["nome"] = "TURURUUU"

            response = c.put('/animal/{0}'.format(animal['id']), json=animal)
            data = response.json

            self.assertEqual(response.status_code,
                             HTTPStatus.OK)
            self.assertEqual(size_collection_before_insert,
                             len(Animal.objects))
            self.assertIsNotNone(data['id'])
            self.assertEqual(data['nome'], animal['nome'])

    def test_put_animal_when_invalid_data(self):

        with self.app.test_client() as c:
            size_collection_before_insert = len(Animal.objects)
            animal = {"nome": 'test', "peso": 5, "tipo": 'test',
                      "data_nascimento": 'AAAAAAA'}

            animal['id'] = self.animal_update_dict_test['id']

            response = c.put('/animal/{0}'.format(animal['id']), json=animal)
            data = response.json

            self.assertEqual(response.status_code,
                             HTTPStatus.UNPROCESSABLE_ENTITY)

    def test_put_animal_when_invalid_id(self):

        with self.app.test_client() as c:
            size_collection_before_insert = len(Animal.objects)
            animal = {"nome": 'test', "peso": 5, "tipo": 'test',
                      "data_nascimento": 'AAAAAAA'}

            animal['id'] = self.animal_update_dict_test['id']

            response = c.put('/animal/{0}'.format(0), json=animal)
            data = response.json

            self.assertEqual(response.status_code,
                             HTTPStatus.BAD_REQUEST)

    def test_put_animal_when_id_does_not_exist(self):
        with self.app.test_client() as c:
            response = c.put('/animal/619bd05b20c5f552ce95e280',
                             json=self.animal_update_dict_test)
            data = response.data
            self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_delete_animal_when_id_exist(self):
        with self.app.test_client() as c:
            size_collection_before_insert = len(Animal.objects)

            response = c.delete('/animal/619bd05b20c5f552ce95e28a')
            data = response.data
            self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
            self.assertEqual(size_collection_before_insert -
                             1, len(Animal.objects))

    def test_delete_animal_when_id_does_not_exist(self):
        with self.app.test_client() as c:
            response = c.delete('/animal/619bd05b20c5f552ce95e280')
            data = response.data
            self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_delete_animal_when_invalid_id(self):
        with self.app.test_client() as c:
            response = c.delete('/animal/0')
            data = response.data
            self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)


if __name__ == '__main__':
    unittest.main()
