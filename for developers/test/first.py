from ctypes import *
<<<<<<< HEAD
c_file = "D:\\Git Hub\\Metro-Navigator\\for developers\\test\\mylib1.dll"
=======
c_file = "C:\\Users\\gulsh\\OneDrive\\Documents\\GitHub\\Metro-Navigator\\for developers\\test\\mylib1.so"
>>>>>>> d4463d04e1e6b761a856820b2e5f06977cb2657b
print(c_file)
c_fun = CDLL(c_file)

rsult = c_fun.produc(2,5)
print(rsult)
