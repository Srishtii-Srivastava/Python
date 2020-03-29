from flask_restful import Resource

from models.store import StoreModel

class Store(Resource):

    def get(self,name):
        store = StoreModel.get_store_by_name(name)
        if store :
            return store.json()
        return {'message' : 'Store not found'},404
        
    def post(self,name):
        if StoreModel.get_store_by_name(name):
            return {'message' : f'Store {name} already exists!'},400
        else :
            store = StoreModel(name)
            store.save_to_db()
        return {'message' : 'Store added successfully.'},201

    def delete(self,name):
        store = StoreModel.get_store_by_name(name)
        if store:
            store.delete_from_db()
        return {'message' : 'Store deleted successfully.'}

class StoreList(Resource):
    def get(self):
        return {'stores' : [store.json() for store in  StoreModel.query.all()]}