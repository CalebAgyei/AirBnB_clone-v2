#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import * 
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Manages amenities for Hbnb"""
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    # Create many-to-many relationship between Amenity and Place
    id = Column(Integer, primary_key=True)
    place_amenities = relationship("Place", secondary=place_amenity,
            back_populates="amenities")
