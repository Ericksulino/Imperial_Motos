import os
cwd = os.getcwd()
print(type(cwd))
dir_path = os.path.dirname(os.path.realpath(__file__))
print(type(dir_path))