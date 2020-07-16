import os
import importlib

from flails import db

libraries = {}
list_of_libraries = os.listdir("flails/models")
for dir in list_of_libraries:
    if dir not in ["__init__.py", "__pycache__"]:
        libraries[dir[0:-3].capitalize()] = getattr(importlib.import_module("." + dir[0:-3], package="flails.models"),
                                                    dir[0:-3].capitalize())
