#!/usr/bin/python3
"""Create a database storage engine"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


class DBStorage:
    """This class manages storage of hbnb models in database format"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate DBStorage class"""

        # Create a new engine to MySQL
        self.__engine = create_engine(
                "mysql+mysqldb://hbnb_dev@localhost/hbnb_dev_db",
                encoding='latin1', echo=True, pool_pre_ping=True)

        # Set environment variables
        os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
        os.environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
        os.environ['HBNB_MYSQL_HOST'] = 'localhost'
        os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'

        # Retrieve environment variables
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')

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



if __name__ = '__main__':
    pass
