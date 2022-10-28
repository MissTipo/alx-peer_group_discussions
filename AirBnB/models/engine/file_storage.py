'''
Store instances created in JSON format in the database
'''

import json


class FileStorage():
    '''
    FileStorage Class for that serializes instances 
    to a JSON file and deserializes JSON file to instances
    '''

    '''Private class attributes'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj): 
        '''sets in __objects the obj with key <obj class name>.id'''
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj.to_dict()
        #type(self).__objects[key] = obj

    def save(self): 
        '''serializes __objects to the JSON file'''
        new_dict = self.__objects.copy()
        if new_dict is not None:
            json_fmt =json.dumps(new_dict)
            with open(FileStorage.__file_path, 'a', encoding='utf-8') as f:
                f.write(json_fmt)
         
    def reload(self):
        '''deserializes the JSON file to __objects'''
        pass
        '''try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                objs_dict = {}
                objs_dict = json.load(f)
                
        except FileNotFoundError:
            return'''

    @staticmethod
    def from_json_string(j_string):
        if j_string is not None or j_string != '':
            dict_fmt = json.loads(j_string)
            return dict_fmt
        else:
            return

    
