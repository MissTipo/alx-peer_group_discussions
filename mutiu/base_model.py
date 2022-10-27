"""This is the Basemodel for the Airbnb clone project"""
from models.__init__ import storage
from datetime import datetime
from uuid import uuid4
import json


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Using kwargs for the constructor of a Basemodel
            *args: will not be used
        """

        #unused = ["__class__"]
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "__class__":
                    continue
                setattr(self, key, value)
                #self.__dict__.update({k: v})
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    

        """Inititalize the instance attribute
            Args:
                id: The unique ID for the instance
                created_at: The time the instance is created
                updated_at: The time the instancve is updated
        """

    def __str__(self):
        """Magic method to print the Instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update 'updated_at' with the current time"""
        self.updated_at = datetime.now()
        #print("call storage.save()")
        storage.save()

    def to_dict(self):
        """Returns dictionary containing all attributes"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict


"""
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
"""
