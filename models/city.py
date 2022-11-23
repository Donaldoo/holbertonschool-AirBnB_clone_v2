#!/usr/bin/python3
""" City Module for HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel
=======
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
>>>>>>> origin/alt
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
<<<<<<< HEAD
    state_id = ""
    name = ""
    places = relationship("Place", backref="cities", cascade="all, delete", passive_deletes=True)
=======
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', backref='cities', cascade='delete')
>>>>>>> origin/alt
