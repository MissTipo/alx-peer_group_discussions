"""Filestorage class"""
import json
# from models.base_model import BaseModel

class FileStorage():
    """Filestorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        print("All method call")
        new_copy = FileStorage.__objects.copy()
        for k in new_copy.keys():
            new_copy[k] = new_copy[k].to_dict()
            print(new_copy)
        """Returns the dictionary"""
        return new_copy

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj
        """sets obj with its key in __objects"""

    def save(self):
        """serialize __objects to json"""
        new_dict = FileStorage.__objects.copy()
        #print("Before")
        for k in new_dict.keys():
            #print("Before change")
            #print(new_dict[k])
            #print("after change")
            new_dict[k] = new_dict[k].to_dict()
            #print(k)

        print("Calling save in fs")
        with open(FileStorage.__file_path, "a", encoding="utf-8") as f:
            #print("-" * 100)
            #print(new_dict)
            json.dump(new_dict, f)
            #print("dumped")

    def reload(self):
        print("Reload Method called")
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return

