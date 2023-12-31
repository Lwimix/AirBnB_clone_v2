#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import hashlib
import models
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        __table_args__ = {'extend_existing': True}
        id = Column(String(60), primary_key=True, nullable=False)
        email = Column(String(128), nullable=False)
        _password = Column('password', String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user",
                              cascade="all, delete-orphan")
        reviews = relationship("Review",
                               backref="user",
                               cascade="all, delete-orphan")
    else:
        email = ""
        _password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        """hashing password values"""
        self._password = pwd
