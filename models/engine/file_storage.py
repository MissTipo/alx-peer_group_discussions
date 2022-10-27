import json
#from models.base_model import BaseModel


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return (FileStorage.__objects)

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = obj.__class__.__name__ + "." + obj.id
        #key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
        #__objects[key] = obj

    def reload(self):
        '''deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist,
         no exception should be raised)'''
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                return (json.load(f))
        except FileNotFoundError:
            return

    def save(self):
        '''method of storage
        __init__(self, *args, **kwargs):
        if it’s a new instance (not from a dictionary representation),
         add a call to the method new(self) on storage'''
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(FileStorage.__objects, f)
