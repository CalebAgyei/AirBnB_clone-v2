#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
import os


# Retrieve environment variables
HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

# Switch storage type directly using an environment variable
if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage

    # Create an instance of DBStorage and reload
    storage = DBStorage()
    storage.reload()

else:
    from models.engine.file_storage import FileStorage

    # Create an instance of FileStorage and reload
    storage = FileStorage()
    storage = FileStorage()
