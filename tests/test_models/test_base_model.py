#!/usr/bin/python3
"""Unittest for BaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Create a new instance before each test"""
        self.model = BaseModel()
        self.model.name = "Test Model"
        self.model.number = 42

    def test_id_type(self):
        """Test that the id is a string"""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_id_unique(self):
        """Test that each instance has a unique id"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_created_at_type(self):
        """Test that created_at is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        """Test that updated_at is a datetime object"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Test that save() updates updated_at"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test that to_dict() returns a dictionary"""
        model_dict = self.model.to_dict()

        created_at_str = self.model.created_at.isoformat()
        updated_at_str = self.model.updated_at.isoformat()

        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"], created_at_str)
        self.assertEqual(model_dict["updated_at"], updated_at_str)

    def test_to_dict_method(self):
        """Test dictionary conversion"""
        obj_dict = self.model.to_dict()
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["name"], "Test Model")
        self.assertEqual(obj_dict["number"], 42)
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)

    def test_str_representation(self):
        """Test the string representation of the instance"""
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_create_instance_from_dict(self):
        """Test creating an instance from a dictionary"""
        obj_dict = self.model.to_dict()
        new_model = BaseModel(**obj_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)
        self.assertFalse(self.model is new_model)


if __name__ == '__main__':
    unittest.main()
