#!/usr/bin/env python3
from uuid import uuid4
import json
from datetime import datetime
from __init__ import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """Updates 'updated_at' current datetime"""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """Returns dictionary containing all keys/values"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def save_json_to_file(self, filename):
        '''Saves instance of BaseModel to a file'''
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f)

    def save_json_to_file2(self, filename):
        '''Saves instance of BaseModel to a file'''
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(self.to_dict()))

    def load_json_from_file2(filename):
        '''loads an instance of BaseModel from a file'''
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()

    def load_json_from_file(filename):
        '''loads an instance of BaseModel from a file'''
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
