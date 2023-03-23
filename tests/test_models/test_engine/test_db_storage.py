#!/usr/bin/python3
"""Module for testing database storage"""
import unittest
from models.base_model import BaseModel, Base
from models import storage
import os



class test_dbStorage(unnittest.TestCase):
    """ Class to test the database storage method. """

    def setUp(self):
        """ Set up test environment """
        del_list = []

