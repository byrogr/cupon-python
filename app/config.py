'''
Created on 27 dic. 2019

@author: Roger Rojas <frostbit.sh@gmail.com>
'''


class Config:
    SECRET_KEY = '40LEWT3kLdpWQn5ZaLGDYMfRT7K6QXKu'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@localhost:3306/cupon_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
