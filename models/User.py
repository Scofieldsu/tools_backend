# -*- coding: utf-8 -*-
"""
@Time : 2017/7/17 16:37
@Author : Yu Yuan

"""
from models import db

collections = db.Table('collection',
    db.Column('user_id',db.Integer, db.ForeignKey('user.id')),
    db.Column('service_id',db.Integer, db.ForeignKey('service.id'))
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50),unique=True)
    password_hash = db.Column(db.String(120))
    active = db.Column(db.Boolean, default=1)
    access_token = db.Column(db.String(120))
    services = db.relationship('Service', backref='users')
    messages = db.relationship('Message', backref='users')
    collect = db.relationship('Service', secondary = collections,
                              backref = db.backref('star_users',lazy='dynamic'),
                              lazy = 'dynamic')

    def __init__(self,username,email,password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def enable(self):
        self.active = 1
        db.session.add(self)
        db.session.commit()


    def disable(self):
        self.active = 0
        db.session.add(self)
        db.session.commit()