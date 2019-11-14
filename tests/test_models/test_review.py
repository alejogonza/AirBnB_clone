#!/usr/bin/python3
"""test para review"""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel
import pep8


class TestReview(unittest.TestCase):
    """clase para place class"""

    @classmethod
    def Config(cls):
        cls.rev = Review()
        cls.rev.place_id = "6969-nini"
        cls.rev.user_id = "9696-nini"
        cls.rev.text = "Nani no xd"

    @classmethod
    def Cleardelete(cls):
        del cls.rev

    def ClearDelete(self):
        """ClearDelete"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def Review_style(self):
        """pep8"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/review.py'])
        self.assertEqual(pep.total_errors, 0, "fix pep8")

    def Review_docsting(self):
        """docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def Review_attributes(self):
        """attributes"""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def Review_subclass(self):
        """subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def Review_test_attrib(self):
        """test attrib"""
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    def Review_save(self):
        """save"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def Review_dict(self):
        """dictionary"""
        self.assertEqual('to_dict' in dir(self.rev), True)


if __name__ == "__main__":
    unittest.main()
