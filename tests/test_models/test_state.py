#!/usr/bin/python3
"""test para state"""
import unittest
import os
from models.state import State
from models.base_model import BaseModel
import pep8


class TestState(unittest.TestCase):
    """clase para State class"""

    @classmethod
    def Config(cls):
        cls.state = State()
        cls.state.name = "CO"

    @classmethod
    def Cleardelete(cls):
        del cls.state

    def ClearDelete(self):
        """ClearDelete"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def Review_style(self):
        """pep8"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/state.py'])
        self.assertEqual(pep.total_errors, 0, "fix pep8")

    def State_docstrings(self):
        """docstrings"""
        self.assertIsNotNone(State.__doc__)

    def State_attributes(self):
        """attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def State_subclass(self):
        """subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def State_attribute(self):
        """attribute"""
        self.assertEqual(type(self.state.name), str)

    def State_save(self):
        """save"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def State_dict(self):
        """dictionary"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
