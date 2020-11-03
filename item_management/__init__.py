import shelve

from flask import Flask, current_app, g
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)

api = Api(app)

def get_db():
    if 'db' not in g:
        g.db = shelve.open("item.db")
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close() 

class ItemList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        items = []

        for key in keys:
            items.append(shelf[key])
        
        return {'message': 'Success', 'data':items}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('brand')
        parser.add_argument('item_type')
        parser.add_argument('expire_date', required=True)
        parser.add_argument('desire')
        parser.add_argument('sales')

        args = parser.parse_args()

        shelf = get_db()
        shelf[args['identifier']] = args

        return {'message': 'Item added', 'data': args}, 201

class Item(Resource):
    def get(self,identifier:str):
        shelf = get_db()

        if not (identifier in shelf):
            return {'message': 'Item not found', 'data': {}}, 404

        return {'message':'Item found', 'data': shelf[identifier]}, 200

    def delete(self, identifier):
        shelf = get_db()

        if not(identifier in shelf):
            return {'message': 'Item not found', 'data': {}}, 404

        del shelf[identifier]
        return '', 204

        
api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:identifier>')
