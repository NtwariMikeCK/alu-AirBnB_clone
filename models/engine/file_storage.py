import json
from models.base_model import BaseModel


import json
from models.base_model import BaseModel
import os


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
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f,
                      indent=4)

    def save(self):
      try:
        with open(FileStorage.__file_path, "r") as f:
          existing_data = json.load(f)
      except(FileNotFoundError, json.JSONDecodeError):
        existing_data = {}

      # Merge new data with existing data
      for key, obj in FileStorage.__objects.items():
        existing_data[key] = obj.to_dict()
        
      # save updated data back to json
      with open(FileStorage.__file_path, "w") as f:
        json.dump(existing_data, f, indent=4)


    def reload(self):
      """Deserialize JSON file to objects (if exists)"""
      data = {}  # Initialize data with empty dict
      try:
        with open(FileStorage.__file_path, "r") as f:
          content = f.read().strip()
          if content:  # Check if file has content
            data = json.loads(content)
            for key, value in data.items():
              class_name = value["__class__"]
              if class_name == "BaseModel":
                FileStorage.__objects[key] = BaseModel(**value)
      except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is invalid, do nothing
        pass
      return data
    
    def delete(self, key):
      """Deletes the specified object from storage"""
      try:
          # we performed a storage.reload()
          with open(FileStorage.__file_path, "r") as f:
              data = json.load(f)
      except (FileNotFoundError, json.JSONDecodeError):
          return  # If file doesn't exist or is invalid, nothing to delete
      
      if key not in data:
          print(f"Error: No object found with key '{key}'.")
          return
      
      if key in data:
          # we saved the files as new data
          del data[key]  # Remove the object if it exists
          # Save the updated data back to file.json
          with open(FileStorage.__file_path, "w") as f:
              json.dump(data, f, indent=4)
              print("The instance was successfully deleted")
