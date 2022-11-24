#!/usr/bin/python3
"""Unittest for base_model"""
import unittest
from models.place import Place
from datetime import datetime


class Test_User(unittest.TestCase):
    """Class to Test User"""
    base1 = Place()

    def test_uuid(self):
        """Test id attribute and type of id"""
        self.assertTrue(hasattr(self.base1, "id"))
        self.assertEqual(type(self.base1.id), str)

    def test_created_at(self):
        """Test created_at and type of created_at"""
        self.assertTrue(hasattr(self.base1, "created_at"))
        self.assertEqual(type(self.base1.created_at), datetime)

    def test_updated_at(self):
        """Test updated_at and type of updated_at"""
        self.assertTrue(hasattr(self.base1, "updated_at"))
        self.assertEqual(type(self.base1.updated_at), datetime)

    def test_str(self):
        """Test the __str__ method from BaseModel"""
        name = "[{}] ({}) {}".format(
            self.base1.__class__.__name__,
            self.base1.id,
            self.base1.__dict__)
        self.assertEqual(self.base1.__str__(), name)

    def test_save(self):
        """Test save method, compare created_at with updated_at"""
        prev_update = self.base1.updated_at
        self.base1.save()
        self.assertNotEqual(prev_update, self.base1.updated_at)

    def test_to_dict_created_at(self):
        """Test the to_dict method in BaseModel"""
        created_time = self.base1.created_at
        our_dict = self.base1.to_dict()
        self.assertNotEqual(our_dict["created_at"], created_time)

    def test_to_dict_updated_at(self):
        """Test the to_dict method in BaseModel"""
        updated_time = self.base1.updated_at
        our_dict = self.base1.to_dict()
        self.assertNotEqual(our_dict["updated_at"], updated_time)

    def test__to_dict_class(self):
        """Test for class in dict"""
        our_dict = self.base1.to_dict()
        self.assertTrue("__class__" in our_dict.keys())


if __name__ == "__main__":
    unittest.main()
