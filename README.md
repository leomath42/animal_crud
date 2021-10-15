# Animal CRUD

App feito com Flask, PyMongo e React

#### Antes de executar o flask, primeiro crie uma env :

cd animal_crud

python3 -m venv env

source env/bin/activate

pip3 install -r ./backend/requeriments.txt

#### Depois crie um document mongo:

mkdir -p .data/db

mongod --dbpath .data/db

export FLASK_ENV=dev

export FLASK_APP=./backend/main.py

export FLASK_ENV=DEBUG

flask run

#### para rodar o React:

cd ./frontend

npm install

npm start
