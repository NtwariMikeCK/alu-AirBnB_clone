#!usr/bin/python3

import unittest
import os
import json
from models.user import User
from models import storage


class TestUserSaveReload(unittest.TestCase):
    """Test cases for saving and reloading User instances."""

    def setUp(self):
        """Set up test environment before each test."""
        self.file_path = "file.json"  # Path to file.json
        self.storage = storage  # Instance of FileStorage
        self.user = User()
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.email = "johndoe@example.com"
        self.user.password = "securepassword"

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)  # Remove file.json to reset state

    def test_save_user(self):
        """Test if User instance is saved correctly in file.json."""
        self.storage.new(self.user)
        self.storage.save()

        # Verify file exists
        self.assertTrue(os.path.exists(self.file_path))

        # Verify content
        with open(self.file_path, "r") as f:
            data = json.load(f)
            key = f"User.{self.user.id}"
            self.assertIn(key, data)  # Check if key exists
            self.assertEqual(data[key]["first_name"], "John")
            self.assertEqual(data[key]["last_name"], "Doe")
            self.assertEqual(data[key]["email"], "johndoe@example.com")

    def test_reload_user(self):
        """Test if User instance is correctly reloaded from file.json."""
        self.storage.new(self.user)
        self.storage.save()

        # Create a new storage instance to simulate reloading
        new_storage = storage
        loaded_data = new_storage.reload()  # Reload data from file

        key = f"User.{self.user.id}"
        self.assertIn(key, loaded_data)  # Check if key exists
        self.assertEqual(loaded_data[key]["first_name"], "John")
        self.assertEqual(loaded_data[key]["last_name"], "Doe")
        self.assertEqual(loaded_data[key]["email"], "johndoe@example.com")


if __name__ == "__main__":
    unittest.main()
