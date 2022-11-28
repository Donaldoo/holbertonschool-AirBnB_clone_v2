#!/usr/bin/python3
"""SQLAlchemy DB storage"""
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.schema import MetaData


username = getenv('HBNB_MYSQL_USER')
password = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')
v_env = getenv('HBNB_ENV')

url = "mysql+mysqldb://{}:{}@{}/{}".format(username, password, host, db)


class DBStorage:
    """SQLAlchemy storage"""
    __engine = None
    __session = None

    def __init__(self):
        """init engine"""
        self.__engine = create_engine(url, pool_pre_ping=True)

        if v_env == 'test':
            metadata = MetaData(self.__engine)
            metadata.reflect()
            metadata.drop_all()

    def all(self, cls=None):
        """query on the current database session """
        """if (cls):
            objects_list = self.__session.query(cls).all()
        else:
            object_list = self.__session.query(State).all()
            object_list.extend(self.__session.query(City).all())
            object_list.extend(self.__session.query(User).all())
            object_list.extend(self.__session.query(Place).all())
            object_list.extend(self.__session.query(Review).all())
            object_list.extend(self.__session.query(Amenity).all())

        object_dict = {}
        for obj in object_list:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            object_dict[key] = obj
        return object_dict"""

        classDict = {"City": City, "State": State,
                     "User": User, "Place": Place,
                     "Review": Review, "Amenity": Amenity}
        objects = {}
        if cls is None:
            for className in classDict:
                data = self.__session.query(classDict[className]).all()
                for obj in data:
                    objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

        else:
            if isinstance(cls, str):
                cls = classDict[cls]
            data = self.__session.query(cls).all()
            for obj in data:
                objects[f"{obj.id}"] = obj
        return objects

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)

        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """closes session"""
        self.__session.remove()
