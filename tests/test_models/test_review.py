#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def setUp(self):
        """Create an instance before each test."""
        self.review = Review()

    def test_instance_creation(self):
        """Test if the instance is correctly created."""
        self.assertIsInstance(self.review, Review)

    def test_inheritance(self):
        """Test if Review inherits from BaseModel."""
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_default_attributes(self):
        """Test default attributes."""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")


if __name__ == "__main__":
    unittest.main()
