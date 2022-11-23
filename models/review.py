#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

<<<<<<< HEAD

class Review(BaseModel, Base):
    """ Review class to store review information """

    __tablename__ = "reviews"

    place_id = Column(String(60), nullable=False, ForeignKey('places.id')
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
=======
class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'

    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
>>>>>>> origin/alt
    text = Column(String(1024), nullable=False)
