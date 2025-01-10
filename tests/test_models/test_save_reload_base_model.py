#!/usr/bin/python3
import unittest
import os
from models import storage
from models.base_model import BaseModel


class TestBaseModelSaveReload(unittest.TestCase):
    """This is used to test for most of the things"""
    def setUp(self):
        """Set up test environment"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save_reload(self):
        # Load existing objects from file.json
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)
        # Create a new BaseModel object
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

        # Clear storage and reload
        storage._FileStorage__objects = {}
        storage.reload()

        # Verify the object was saved
        key = f"BaseModel.{my_model.id}"
        self.assertIn(key, storage.all())
        # Verify object attributes
        saved_obj = storage.all()[key]
        self.assertEqual(saved_obj.name, "My_First_Model")
        self.assertEqual(saved_obj.my_number, 89)

        # Verify reloaded object
        key = f"BaseModel.{my_model.id}"
        self.assertIn(key, storage.all())
        reloaded_model = storage.all()[key]
        self.assertEqual(reloaded_model.name, "My_First_Model")
        self.assertEqual(reloaded_model.my_number, 89)


if __name__ == '__main__':
    unittest.main()
