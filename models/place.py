#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm import relationship


# MANY-TO-MANY RELATIONSHIP
# Create an instance of Table to create many-to-many relationship
# Association table
place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
            primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
            primary_key=True, nullable=False)
        )

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float(0.00), nullable=True)
    longitude = Column(Float(0.00), nullable=True)

    # Create a relationship between Place and Cities
    city = relationship("City", back_populates="places")
    
    # Create a relationship between Place and Users
    user = relationship("Users", back_populates="places")  

    # Create a relationship between Place and Reviews
    review = relationship("Review", back_populates="places",
            cascade="all, delete")

    # Create a Many-to-Many relationship
    id = Column(Integer, primary_key=True)
    amenities = relationship('Amenity', secondary=place_amenity,
            back_populates="places", viewonly=False) 
