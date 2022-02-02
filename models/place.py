#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import models
from models.amenity import Amenity
from models.base_model import Base, BaseModel
import os

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class Place(BaseModel, Base):
        """ A place to stay """
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review', backref='place', cascade='delete')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 overlaps="place_amenities", viewonly=False)
else:
    class Place(BaseModel):
        """ A place to stay """
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = ''
        number_bathrooms = ''
        max_guest = ''
        price_by_night = ''
        latitude = ''
        longitude = ''
        amenity_ids = []

        @property
        def reviews(self):
            """Get reviews
            Returns the list of Review instances with place_id equals to the
            current Place.id
            """
            reviews = models.storage.all(Review)
            return [instance for instance in reviews.values()
                    if self.id == instance.place_id]

        @property
        def amenities(self):
            """Getter attribute amenities
            Returns the list of Review instances with place_id equals to the
            current Place.id
            """
            amenities = models.storage.all(Amenity)
            return [instance for instance in amenities.values()
                    if self.id == instance.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            """Setter attribute amenities

            Args:
                value ([Amenity]): amenity to be appended
            """
            if value.__class__.__name__ == Amenity:
                self.amenities.append(value)
