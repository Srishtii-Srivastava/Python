# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:58:42 2020

@author: Srishti Srivastava
"""

from models.user import UserModel

def authenticate(username,password):
    user = UserModel.find_by_username(username)
    if user and password == user.password :
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)