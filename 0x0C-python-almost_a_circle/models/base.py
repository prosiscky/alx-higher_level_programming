#!/usr/python3
class Base:
    """
        Base class 
        Attributes:
            __nb_objects: counts the number of instance created in a seesion
            id: id of each instance as they are created starting from 1
    """

    __nb_objects = 0
	
    def __init__(self, id=None):
        """ A method thst initializes the insatance (object)
        args:
        id: id of the instance created (object)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
