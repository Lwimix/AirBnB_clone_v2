#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'review'
    __table_args__ = {'extend_existing': True}
    id = Column(String(60), primary_key=True, nullable=False)
    place_id = Column(String(60), ForeignKey("user.id"),
                      nullable=False)
    user_id = Column(String(60), ForeignKey("place.id"), 
                     nullable=False)
    text = Column(String(1024), nullable=False)
