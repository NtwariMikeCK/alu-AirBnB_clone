#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def setUp(self):
        """Create an instance before each test."""
        self.state = State()

    def test_instance_creation(self):
        """Test if the instance is correctly created."""
        self.assertIsInstance(self.state, State)

    def test_inheritance(self):
        """Test if State inherits from BaseModel."""
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_default_attributes(self):
        """Test default attributes."""
        self.assertEqual(self.state.name, "")


if __name__ == "__main__":
    unittest.main()
