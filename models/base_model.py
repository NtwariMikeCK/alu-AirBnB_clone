#!/usr/bin/python3
import uuid
from datetime import datetime
# from models import storage


class BaseModel:
    """BaseModel class that defines common attributes/methods"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            from models import storage  # Import here to avoid circular import
            storage.new(self)  # Add new instance to storage

    def __str__(self):
        """String representation of the instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Updates `updated_at` with the current datetime"""
        self.updated_at = datetime.now()
        from models import storage  # Import inside method
        storage.save()  # Save to JSON file

    def to_dict(self):
        """Converts instance into a dictionary format"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
