from datetime import datetime
from uuid import uuid4
from models.engine.file_storage import FileStorage
from models import storage


class BaseModel(object):
    '''BaseModel Class'''
   
    def __init__(self, *args, **kwargs):
        '''
        Intialize public instance attributes:
        Args
                id: uuid.uuid4() # to generate unique id but don’t forget to convert to a string

                created_at: datetime - assign with the current datetime when an instance is created

                updated_at: datetime - assign with the current datetime when an instance is created 
                            and it 	will be updated every time you change your object
        '''
        if not kwargs:
            self.id = str(uuid4())
            # datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
            self.created_at = datetime.now()
            # datetime.datetime(2017, 9, 28, 21, 5, 54, 119434) (add++)
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(str(value)))
                    else:
                        setattr(self, key, value)             

    def __str__(self):
        '''
	    __str__: should print: [<class name>] (<self.id>) <self.__dict__>
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    '''
	Public instance methods:
    '''
    def save(self):
        '''
        save(self): updates the public instance attribute updated_at with the current 
        datetime
        '''
        self.updated_at = datetime.now()
        storage.save()
		
    def to_dict(self):
        '''
		to_dict(self): returns a dictionary containing all keys/values of __dict__ of the 			
        instance:

			by using self.__dict__, only instance attributes set will be returned

			a key __class__ must be added to this dictionary with the class name of the 			
            object

			created_at and updated_at must be converted to string object in ISO format:
			format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)

			you can use isoformat() of datetime object
            '''
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()             
        return new_dict
