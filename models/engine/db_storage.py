#!/usr/bin/python3
"""Create a database storage engine"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os


class DBStorage:
    """This class manages storage of hbnb models in database format"""
    __engine = None
    __session = None
    __objects = {}

    def __init__(self):
        """Instantiate DBStorage class"""

        # Retrieve environment variables
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')

        # Create a new engine to MySQL
        self.__engine = create_engine(
                "mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db",
                encoding='latin1', echo=True, pool_pre_ping=True)

        # Set environment variables
        # os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
        # os.environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
        # os.environ['HBNB_MYSQL_HOST'] = 'localhost'
        # os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'

        # Make a connection to the database
        self.__engine.connect()

        # Drop all tables if the environment variable HBNB_ENV is equal to test

    def all(self, cls=None):
        """Create a session to talk to or query current database"""

        # Define Session class to serve as factory for new Session objects
        Session = sessionmaker(bind=self.__engine)

        # Create a new session
        self.__session = Session()

        # Query on current database session the object depending on cls
        self.__session.query(cls)

        #Query all types of objects if cls=None
        if cls is None:
            for i in [User, State, City, Amenity, Place, Review]:
                obj = self.__session.query(i)
                __objects.update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

        return DBStorage.__objects

    def new(self, obj):
        """Add object to current database session"""
        self.__session.add_all(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from current database session obj if not None"""
        if obj is not None:
            self.__session.rollback()
        else:
            pass

    def reload(self):
        """
        Load all classes who inherit from Base and create all tables
        in database
        """
        from models.base_model import Base
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        # Create all tables in database using MetaData.create_all()
        Base.metadata.create_all(self.__engine)

        # Create the current database session by using sessionmaker
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)

        # Create a scoped_session object to make my Session thread-safe
        Session = scoped_session(session_factory)

        # Create session
        self.__session = Session()


if __name__ == '__main__':
    pass
