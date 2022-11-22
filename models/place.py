#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.sql.sqltype import Float, Integer
from sqlalchemy.orm import relationship, backref


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60), nullable=False, ForeignKey(cities.id))
    user_id = Column(String(60), nullable=False, ForeignKey(users.id))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    review = relationship("Review", backref="place", cascade="all, delete", passive_deletes=True)

    @property
    def reviews(self):
        """Getter that returns the list of Review instances"""
        inst = models.storage.all(Review)
        new_list = []
        for rev in inst.values():
            if rev.place_id == (self.id):
                new_list.append(review)
        return new_list
