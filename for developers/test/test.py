import ctypes
import os

path = os.path.dirname(os.path.realpath(__file__))
lib = ctypes.CDLL(path+"/add.dll")

result = lib.add(2, 3)
print(result)
