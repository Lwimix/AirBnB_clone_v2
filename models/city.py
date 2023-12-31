#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class City(BaseModel, Base):
    """the city representation"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        __table_args__ = {'extend_existing': True}
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'),
                          nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete-orphan")
        id = Column(String(60), primary_key=True)
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """to initialize the city"""
        super().__init__(*args, **kwargs)
