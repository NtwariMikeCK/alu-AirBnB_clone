#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """Handles storage of BaseModel instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary of stored objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Add new object to storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize objects to JSON file"""
        with open(FileStorage.__file_path, "w") as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()},
                f,
                indent=4
            )

    def reload(self):
        """Deserialize JSON file to objects (if exists)"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass  # Don't raise an error if the file doesn't exist
