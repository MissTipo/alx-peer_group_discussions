#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    # cities = relationship('City')
    cities = relationship('City', backref='state')
   # user = relationship("User", back_populates="addresses")


    @property
    def cities(self):

        '''returns the list of City instances with state_id
            equals the current State.id
            FileStorage relationship between State and City
        '''
        from models import storage
        related_cities = []

        cities = storage.all(City).items() # gets the entire storage- a dictionary
        for city in cities.values(): # cities.value returns list of the city objects
            if city.state_id == self.id: # if the object.state_id == self.id
                related_cities.append(city) # append to the cities list
        return related_cities
