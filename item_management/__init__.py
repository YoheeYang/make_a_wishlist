import sqlite3
import click
from flask import Flask, current_app, g
from flask.cli import with_appcontext
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close() 

class ItemList(Resource):
    def get(self):

        return {}

class Item(Resource):
    def get(self,identifier):
        
        return {}