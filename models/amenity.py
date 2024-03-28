#!/usr/bin/python3
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base

Base = declarative_base()

class Amenity(BaseModel, Base):
    """ State Module for HBNB project """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place", secondary="place_amenity", viewonly=True)

