#!/usr/bin/python3
""" Test BaseModel module """

import unittest
import os
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test BaseModel"""

    def setUp(self):
        self.testbasemodel = BaseModel()

    def test_doc(self):
        self.assertIsNotNone(BaseModel.__doc__)

    def test_save_BaseModel(self):
        """test save_BaseModel"""

        base = BaseModel()
        base.save()
        self.assertEqual(base.created_at, base.updated_at)

    def test_kwarg(self):
        basemodel = BaseModel(name="base")
        self.assertEqual(type(basemodel).__name__, "BaseModel")
        self.assertFalse(hasattr(basemodel, "id"))
        self.assertFalse(hasattr(basemodel, "created_at"))
        self.assertTrue(hasattr(basemodel, "name"))
        self.assertFalse(hasattr(basemodel, "updated_at"))
        self.assertTrue(hasattr(basemodel, "__class__"))

if __name__ == "__main__":
    unittest.main()
