from PyGenerator.PyGenerator import project
from config.PyGenerator.metadata import META


# generate folder structure for project and add to sys.path
project(META, 'code', overwrite=True, syspath=True)
