#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def setUp(self):
        """Create an instance before each test."""
        self.place = Place()

    def test_instance_creation(self):
        """Test if the instance is correctly created."""
        self.assertIsInstance(self.place, Place)

    def test_inheritance(self):
        """Test if Place inherits from BaseModel."""
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))

    def test_default_attributes(self):
        """Test default attributes."""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
