#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
import os
import models
from models.city import City

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='delete')
else:
    class State(BaseModel):
        """ State class """
        name = ''
        @property
        def cities(self):
            """Get cities"""
            cities = models.storage.all(City)
            return [instance for instance in cities.values()
                    if self.id == instance.state_id]
