from ctypes import *
c_file = "D:\Git Hub\Metro-Navigator\\for developers\\test\mylib1.so"
print(c_file)
c_fun = CDLL(c_file)