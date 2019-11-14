#!/usr/bin/python3
"""test para amenity"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):
    """clase para amenity test"""

    @classmethod
    def Config(cls):
        cls.amenity = Amenity()
        cls.amenity.name = "Nodejs"

    @classmethod
    def Cleardelete(cls):
        del cls.amenity

    def ClearDelete(self):
        """ClearDelete"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def Amenity_style(self):
        """pep8"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/amenity.py'])
        self.assertEqual(pep.total_errors, 0, "fix pep8")

    def Amenity_docstring(self):
        """docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def Amenity_attrib(self):
        """attibutes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def Amenity_subclass(self):
        """subclass"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def Amenity_test_attrib(self):
        """test attrib"""
        self.assertEqual(type(self.amenity.name), str)

    def Amenity_save(self):
        """save"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def Amenity_dict(self):
        """dictionary"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
