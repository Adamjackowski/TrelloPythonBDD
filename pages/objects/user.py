import os
import inspect
from os.path import dirname
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
rootdir = os.path.dirname(parentdir)

class User:

    '''
    Constructor which assign all fields. Some fields can have default value.
    '''
    def __init__(self, email, password):
        self._email = email
        self._password = password

