#!/usr/bin/python3
import unittest
import os
import json
from models import storage
from models.base_model import BaseModel


class TestStorageOperations(unittest.TestCase):
    """Test cases for storage operations"""

    def setUp(self):
        """Set up test environment"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_new_method(self):
        """Test new() method adds object to storage"""
        model = BaseModel()
        key = f"BaseModel.{model.id}"
        self.assertIn(key, storage.all())

    def test_save_method(self):
        """Test save() method persists objects to file"""
        model = BaseModel()
        model.name = "Test Save"
        model.save()

        with open("file.json", "r") as f:
            data = json.load(f)
            key = f"BaseModel.{model.id}"
            self.assertIn(key, data)
            self.assertEqual(data[key]["name"], "Test Save")

    def test_reload_method(self):
        """Test reload() method loads objects from file"""
        model = BaseModel()
        model.name = "Test Reload"
        model.save()

        storage._FileStorage__objects = {}
        storage.reload()

        key = f"BaseModel.{model.id}"
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key].name, "Test Reload")


if __name__ == '__main__':
    unittest.main()
