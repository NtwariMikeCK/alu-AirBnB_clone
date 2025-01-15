#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        """Create an instance before each test."""
        self.city = City()

    def test_instance_creation(self):
        """Test if the instance is correctly created."""
        self.assertIsInstance(self.city, City)

    def test_inheritance(self):
        """Test if City inherits from BaseModel."""
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_default_attributes(self):
        """Test default attributes."""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")


if __name__ == "__main__":
    unittest.main()
