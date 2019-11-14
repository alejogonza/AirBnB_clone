#!/usr/bin/python3
"""clase para place"""
import unittest
import os
from models.place import Place
from models.base_model import BaseModel
import pep8


class TestPlace(unittest.TestCase):
    """clase para place class"""

    @classmethod
    def Config(cls):
        cls.place = Place()
        cls.place.city_id = "CaCa-666"
        cls.place.user_id = "999-AcAc"
        cls.place.name = "IBIZA"
        cls.place.description = "melo el cuarto"
        cls.place.number_rooms = 666
        cls.place.number_bathrooms = 8
        cls.place.max_guest = 2
        cls.place.price_by_night = 6666666
        cls.place.latitude = 90.0
        cls.place.longitude = 100.0
        cls.place.amenity_ids = ["CoCo-6969"]

    @classmethod
    def Cleardelete(cls):
        del cls.place

    def ClearDelete(self):
        """ClearDelete"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def Place_style(self):
        """pep8"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/place.py'])
        self.assertEqual(pep.total_errors, 0, "fix pep8")

    def Place_docstring(self):
        """docstrings"""
        self.assertIsNotNone(Place.__doc__)

    def Place_attributes(self):
        """attributes"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def Place_subclass(self):
        """Basemodel"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def Place_attrib(self):
        """test attrib"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def Place_save(self):
        """save"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def Place_dict(self):
        """dict"""
        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ == "__main__":
    unittest.main()
