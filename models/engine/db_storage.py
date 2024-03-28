#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone"""
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

MYSQL_USER = getenv('HBNB_MYSQL_USER')
MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
MYSQL_DB = getenv('HBNB_MYSQL_DB')


class DBStorage:
    """This class manages storage of hbnb models in a MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}?charset=utf8mb4'.format(
                MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_DB),
            pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """variable"""
        objects = {}
        classes = [User, State, City, Amenity, Place, Review]

        if cls:
            """conditional"""
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session.query(cls)
            for instance in query:
                key = "{}.{}".format(type(instance).__name__, instance.id)
                objects[key] = instance
        else:
            for cls in classes:
                query = self.__session.query(cls)
                for instance in query:
                    key = "{}.{}".format(type(instance).__name__, instance.id)
                    objects[key] = instance
        """return"""
        return objects

    def new(self, obj):
        """new"""
        self.__session.add(obj)

    def save(self):
        """save"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close"""
        self.__session.close()
