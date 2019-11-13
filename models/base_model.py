#!/usr/bin/python3
"""base del modelo"""

import models
import uuid
from datetime import datetime

class BaseModel:
    """
    define atributos y métodos para otras clases
    """

    def __init__(self, *args, **kwargs):
        """
        instancias de la clase:
             kwargs: args constructor de BaseModel
             id, created_at, updated_at
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            string de nombre de clase, id y diccionario
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """
            representación del string
        """
        return self.__str__()

    def save(self):
        """
            actualiza la instancia pública updated_at al actual
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        crea el diccionario de la clase,
        devuelve diccionario de todos los valores  clave en __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
