#!/usr/bin/python3
"""test para user"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel
import pep8


class TestUser(unittest.TestCase):
    """clase para User class"""

    @classmethod
    def Config(cls):
        cls.user = User()
        cls.user.first_name = "bruse"
        cls.user.last_name = "banner"
        cls.user.email = "hulk@gmamil.com"
        cls.user.password = "green"

    @classmethod
    def Cleardelete(cls):
        del cls.user

    def ClearDelete(self):
        """ClearDelete"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def User_style(self):
        """pep8"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/user.py'])
        self.assertEqual(pep.total_errors, 0, "fix pep8")

    def User_docstring(self):
        """docstrings"""
        self.assertIsNotNone(User.__doc__)

    def User_attributes(self):
        """attributes"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def User_subclass(self):
        """subclass of Basemodel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def User_attribute(self):
        """attribute"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def User_save(self):
        """save"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def User_dictionary(self):
        """dictionary"""
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
