#!/usr/bin/python3
"""
holds the state class
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        __table_args__ = {'extend_existing': True}
        id = Column(String(60), primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete",
                              backref="states")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """fs getter attribute that returns City instances"""
        values_city = models.storage.all("City").values()
        list_city = []
        for city in values_city:
            if city.state_id == self.id:
                list_city.append(city)
        return list_city
