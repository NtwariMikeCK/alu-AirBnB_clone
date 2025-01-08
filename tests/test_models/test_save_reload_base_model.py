#!/usr/bin/python3
import unittest
from models import storage
from models.base_model import BaseModel


class TestBaseModelSaveReload(unittest.TestCase):
    def test_save_reload(self):
        # Load existing objects from file.json
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)
        # Create a new BaseModel object
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        # Verify the object was saved
        key = f"BaseModel.{my_model.id}"
        self.assertIn(key, storage.all())
        # Verify object attributes
        saved_obj = storage.all()[key]
        self.assertEqual(saved_obj.name, "My_First_Model")
        self.assertEqual(saved_obj.my_number, 89)


if __name__ == '__main__':
    unittest.main()
