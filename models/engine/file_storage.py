#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
import os


class FileStorage:
    """Handles storage of BaseModel instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary of stored objects"""
        try:
          with open(FileStorage.__file_path, "r") as f:
            content = f.read().strip()
            if content:  # Check if file has content
              data = json.loads(content)
              for key, value in data.items():
                try:
                    class_name = value["__class__"]
                    if class_name == "User":
                      FileStorage.__objects[key] = value  # Create a User instance

                    elif class_name == "BaseModel":
                      FileStorage.__objects[key] = value  # Create a User instance
                    else:
                      print("Data Not found")
                except KeyError:
                    print(f"Error: No class name found for key {key}")
        except (FileNotFoundError, json.JSONDecodeError):
          # If file doesn't exist or is invalid, do nothing
          pass
        return FileStorage.__objects


    def new(self, obj):
        """Add new object to storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

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
      """Deserializes the JSON file to __objects"""
      data = {}  # Initialize data with empty dict
      try:
        if os.path.exists(self.__file_path):
          with open(self.__file_path, 'r') as f:
            data = json.load(f)
            # Convert the data back to objects if needed
            for key, value in data.items():
                class_name = value["__class__"]
                # Create instance using the correct class
                if class_name == "BaseModel":
                    FileStorage.__objects[key] = BaseModel(**value)
                elif class_name == "User":
                    FileStorage.__objects[key] = User(**value)
      except Exception:
        # print(f"Error in reload: {e}")  # Add this for debugging
        pass

    def delete(self, key):
      """Deletes the specified object from storage"""
      try:
          # we performed a storage.reload()
          with open(FileStorage.__file_path, "r") as f:
              data = json.load(f)
      except (FileNotFoundError, json.JSONDecodeError):
          print(f"Error: No storage file found.")
          return  # If file doesn't exist or is invalid, nothing to delete
      
      if key not in data:
          print(f"Error: No object found with key '{key}'.")
          return
      
      
      del data[key]  # Remove the object if it exists
      FileStorage.__objects.pop(key, None) #remove from memory

      # Save the updated data back to file.json
      with open(FileStorage.__file_path, "w") as f:
          json.dump(data, f, indent=4)
          print("The instance was successfully deleted")
