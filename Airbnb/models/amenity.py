#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, ForeignKey, Column, String
from sqlalchemy.orm import relationship
from models.place import Place



class Amenity(BaseModel, Base):
    """Amenity class that inherits from Basemodel and Base"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    #place_amenity = Table('place_amenity', Base.metadata,
     #       Column('place_id', ForeignKey('places.id'), primary_key=True),
      #      Column('amenity_id', ForeignKey('amenities.id'), primary_key=True))
    #place_amenities = relationship('Place', secondary=place_amenity, backref="amenities")
    place_amenities = relationship('Place', secondary=Place.place_amenity, back_populates="amenities")
    #place_amenities = relationship('Place', secondary=Place.place_amenity)

