#!/usr/bin/python
import uuid
from uuid import uuid4
from datetime import datetime
import models
import json

"""
Base model class that defines all common attributes/methods for other classes

"""
date_now = datetime.now()
class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = str(date_now)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        self.updated_at = str(date_now)

    def to_dict(self):
        dic = {}

        for key, item in self.__dict__.items():
            dic[key] = item
        
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        
        return dic


