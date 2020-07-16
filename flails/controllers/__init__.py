import os
import importlib

list_of_libraries = os.listdir("flails/controllers")
libraries = [importlib.import_module("." + dir[0:-3], package="flails.controllers") for dir in list_of_libraries if
             dir not in ["__init__.py", "__pycache__"]]


