# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:00:09 2020

@author: Srishti Srivastava
"""
import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        required=True,
        type=str,
        help="This feild cannot be empty."
    )
    parser.add_argument('password',
    type=str,
    required=True,
    help="This feild is required.")


    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message" : "User already exists!"},400

        user = UserModel(**data)
        user.save_to_db()

        return {"message" : "User created successfully."},201
