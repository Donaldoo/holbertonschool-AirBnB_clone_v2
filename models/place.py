#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.sql.sqltype import Float, Integer
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import Table
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60), nullable=False, ForeignKey(cities.id))
    user_id = Column(String(60), nullable=False, ForeignKey(users.id))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
=======
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


Table('place_amenity', Base.metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True,
                                 nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
>>>>>>> origin/alt
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
<<<<<<< HEAD
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete", passive_deletes=True)

    @property
    def reviews(self):
        """Getter that returns the list of Review instances"""
        inst = models.storage.all(Review)
        new_list = []
        for rev in inst.values():
            if rev.place_id == (self.id):
                new_list.append(review)
        return new_list
    
    @

place_amenity = Table(
        "place_amenity", Base.metadata,
        Column(
            "place_id",
            String(60),
            ForeignKey("places.id"),
            nullable=False),
        Column(
            "amenity_id",
            String(60),
            ForeignKey("amenities.id"),
            primary_key=True,
            nullable=False))
=======
    latitude = Column(Float)
    longitude = Column(Float)

    reviews = relationship('Review', backref='place', cascade='delete')
    amenities = relationship('Amenity', secondary='place_amenity',
                             back_populates="place_amenities", viewonly=False)

    if getenv('HBNB_TYPE_STORAGE') != 'db':

        @property
        def reviews(self):
            """getter for FileStorage"""
            reviews = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews

        @property
        def amenities(self):
            """getter for FileStorage"""
            amenities = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, obj):
            """setter for FileStorage"""
            if type(obj) == Amenity:
                self.amenities_ids.append(obj.id)
>>>>>>> origin/alt
