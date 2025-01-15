#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def setUp(self):
        """Create an instance before each test."""
        self.amenity = Amenity()

    def test_instance_creation(self):
        """Test if the instance is correctly created."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel."""
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_default_attributes(self):
        """Test default attributes."""
        self.assertEqual(self.amenity.name, "")


if __name__ == "__main__":
    unittest.main()
