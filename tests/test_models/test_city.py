#!/usr/bin/python3
"""test para city"""
import unittest
import os
from models.city import City
from models.base_model import BaseModel
import pep8


class TestCity(unittest.TestCase):
    """clase city class"""

    @classmethod
    def Config(cls):
        cls.city = City()
        cls.city.name = "BOG"
        cls.city.state_id = "CN"

    @classmethod
    def Cleardelete(cls):
        del cls.city

    def ClearDelete(self):
        """ClearDelete"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def City_style(self):
        """pep8"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/city.py'])
        self.assertEqual(pep.total_errors, 0, "fix pep8")

    def City_docstring(self):
        """docstrings"""
        self.assertIsNotNone(City.__doc__)

    def City_attributes(self):
        """attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def City_subclass(self):
        """subclass"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def City_test_attrib(self):
        """test attrib"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def City_save(self):
        """save"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def City_dict(self):
        """dictionary"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
