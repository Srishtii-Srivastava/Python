import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from flask import request

from models.item import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help='This feild cannot be left blank')
    parser.add_argument('store_id',type=int,required=True,help='Every item needs a store id.')
    
    @jwt_required()
    def get(self,name):
        item = ItemModel.get_item_by_name(name)
        if item :
            return item.json(),200
        return {'message' : 'Item not found'},404
        
    def post(self,name):
        if ItemModel.get_item_by_name(name):
            return {'message' : f"Item '{name}' already exists."},400
        data = Item.parser.parse_args()
        item = ItemModel(name,**data)
        try :
            item.save_to_db()
        except:
            return {'message' : 'Error occurred while inserting item'},500
        return {'message' : 'Item added successfully.'},200

    @jwt_required()
    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.get_item_by_name(name)
        if item is None :
          item = ItemModel(name,**data)
        else :
            item.price = data['price']
            item.store_id = data['store_id']
            
        item.save_to_db()
        
        return item.json(),200

    @jwt_required()
    def delete(self,name):
        item = ItemModel.get_item_by_name(name)
        if item:
            item.delete_from_db()
            return {'message' : f"{name} deleted!"},200
        else:
            return{'message' : f"{name} not found!"},404

class ItemList(Resource):
    def get(self):
        return {'items' : [item.json() for item in ItemModel.query.all()]}