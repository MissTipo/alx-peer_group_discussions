import os
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
"""
class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        user = os.environ.get("HBNB_MYSQL_USER")
        password = os.environ.get("HBNB_MYSQL_PWD")
        host = os.environ.get("HBNB_MYSQL_HOST") # (here = localhost)
        database = os.environ.get("HBNB_MYSQL_DB")
        env = os.environ.get("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database, pool_pre_ping=True))

        if (env == "test"):
            # drop all tables if the environment variable HBNB_ENV is equal to test
            #drop_all(engine)
            Base.metadata.drop_all(self.__engine)

            # User.__table__.drop()
            # Session = sessionmaker(bind=self.__engine)
            # session = Session()
            # drop = session.

    def all(self, cls=None):
        """query on the current database session (self.__session)
            all objects depending of the class name (argument cls)
        """

        """
        all_classes = ["State", "City", "Amenity", "User", "Place", "Review"]

        entities = dict()

        if cls:
            return self.get_data_from_table(cls, entities)

        for entity in all_classes:
            entities = self.get_data_from_table(eval(entity), entities)

        return entities
        """
        """ Queries a database for objects """
        if not cls:
            from models.state import State
            #res_list = self.__session.query(Amenity)
            #res_list.extend(self.__session.query(City))
            #res_list.extend(self.__session.query(Place))
            #res_list.extend(self.__session.query(Review))
            res_list = (self.__session.query(State))
            #res_list.extend(self.__session.query(User))
        else:
            res_list = self.__session.query(cls).all()
        if res_list:

            return {'{}.{}'.format(type(obj).__name__, obj.id): obj
                    for obj in res_list}
        else:
            print("Welcome")
        """
        from model.state import State
        objects = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
        db_dict = {}
        if (cls is None):
            for class_obj in objects:
                obj_list = self.__session.query(class_obj) # returns objects in a list
                for obj in obj_list:
                    #key = "{}.{}".format(type(obj.__name__), obj.id)
                    key = "{}.{}".format(type(obj.__name__), obj.id)
                    db_dict[key] = obj
                    # return db_dict

        else:
            obj_list = self.__session.query(cls) # returns list of objects of class cls
            for obj in obj_list:
                key = "{}.{}".format(type(obj.__name__), obj.id)
                db_dict[key] = obj
                # return db_dict
        return db_dict
        """

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if (obj):
            self.__session.delete(obj)
        else:
            pass

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
