import os
import ctypes

# Get the absolute path to the DLL
dll_path = os.path.abspath('example.dll')

# Load the shared library
lib_example = ctypes.windll.LoadLibrary(dll_path)

# Call the C function from Python
result = lib_example.add_numbers(3, 5)

print(f"Python program: Result from C function: {result}")
