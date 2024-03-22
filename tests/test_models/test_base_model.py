#!/bin/usr/python3
"""

"""
import unittest
from models.base_models import BaseModel

class testBaseModel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()

        self.assertisnotnone(my_model.id)
