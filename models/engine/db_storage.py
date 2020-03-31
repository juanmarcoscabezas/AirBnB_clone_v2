#!/usr/bin/python3
"""
DBStorage module
"""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from models.base_model import BaseModel, Base  # import class model
from models.state import State  # import class State
from models.city import City  # import class City
from models.user import User  # import class User
from models.amenity import Amenity  # import class Amenity
from models.place import Place  # import class Place
from models.review import Review  # import class Review


# TODO Create class DBStorage and empty methods
class DBStorage:
    """
     Class DBStorage
    """

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.\
                 format(getenv('HBNB_MYSQL_USER'),
                        getenv('HBNB_MYSQL_PWD'),
                        getenv('HBNB_MYSQL_HOST'),
                        getenv('HBNB_MYSQL_DB')),
                  pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            """Drop all tables"""
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)
        self.__session = Session(self.__engine)

    def all(self, cls=None):
        results = {}
        if cls is not None:
            name = eval(cls)
            for instance in self.__session.query(name):
                key = "{}.{}".format(cls, instance.id)
                results[key] = instance
            return results
        else:
            #print(Base.metadata.tables.keys())
            return results

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        pass

    def reload(self):
        pass
