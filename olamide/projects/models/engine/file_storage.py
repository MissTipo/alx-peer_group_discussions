#!/usr/bin/python3
import json
from models.base_model import BaseModel
#uncommented second line

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (FileStorage.__objects)

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        #key = obj.__class__.__name__
        FileStorage.__objects[key] = obj #returns an obj(an address in memory
        #FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                return (json.load(f))
        except FileNotFoundError:
            return

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f: #added 2 extra lines before the json.dump
            new_dict = {key: obj.to_dict() for key, obj in
                    FileStorage.__objects.items()}  #convert the address to a dict so we can load to json
            json.dump(new_dict, f)
            
    """
    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fname:
            new_dict = {key: obj.to_dict() for key, obj in
                    FileStorage.__objects.items()}
            json.dump(new_dict, fname)
            """
