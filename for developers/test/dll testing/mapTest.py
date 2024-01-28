import ctypes

# Forward declare the Node class
class Node(ctypes.Structure):
    pass

# Define the structure for MetroMap
class MetroMap(ctypes.Structure):
    _fields_ = [("graph", ctypes.POINTER(ctypes.POINTER(Node))),
                ("numStations", ctypes.c_int)]

# Complete the definition for the Node class
Node._fields_ = [("station", ctypes.c_char * 50),
                ("time", ctypes.c_int),
                ("lineColors", ctypes.c_int * 5),
                ("numLines", ctypes.c_int),
                ("next", ctypes.POINTER(Node))]

# Load the DLL
metro_dll = ctypes.CDLL("./metro.dll")  # Replace with the actual path to your DLL

# Define function prototypes
metro_dll.dijkstra.restype = None
metro_dll.dijkstra.argtypes = [ctypes.POINTER(MetroMap), ctypes.c_char_p, ctypes.c_char_p]

# Create an instance of MetroMap
metro_map = MetroMap()

# Initialize the metro map using the initiate function from the DLL
metro_dll.initiate.restype = ctypes.POINTER(MetroMap)
metro_map_ptr = metro_dll.initiate()

# Assign the result to metro_map using contents
metro_map.contents = metro_map_ptr.contents

# Call the dijkstra function
start_station = "Station A"
end_station = "Station K"
metro_dll.dijkstra(ctypes.byref(metro_map), start_station.encode('utf-8'), end_station.encode('utf-8'))

# Note: You may need to adjust the argument types and encoding based on your specific requirements and Python version.
