#!/usr/bin/python3
"""test para BaseModel"""
import unittest
import os
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """clase basemodel"""

    @classmethod
    def Config(cls):
        cls.base = BaseModel()
        cls.base.name = "Alejo"
        cls.base.num = 10

    @classmethod
    def Cleardelete(cls):
        del cls.base

    def ClearDelete(self):
        """"ClearDelete"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def BaseModel_pep8(self):
        """pep8"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/base_model.py'])
        self.assertEqual(pep.total_errors, 0, "fix pep8")

    def BaseModel_docstring(self):
        """docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def BaseModel_test(self):
        """Basemodel"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def BaseModel_init(self):
        """type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def BaseModel_save(self):
        """save"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def BaseModel_dict(self):
        """dict"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
