import ctypes

# Define Node structure first
class Node(ctypes.Structure):
    _fields_ = [
        ('station', ctypes.c_char * 50),
        ('time', ctypes.c_int),
        ('lineColors', ctypes.c_int * 5),
        ('numLines', ctypes.c_int),
        ('next', ctypes.POINTER('Node'))
    ]

# Now define MetroMap structure
class MetroMap(ctypes.Structure):
    _fields_ = [
        ('graph', ctypes.POINTER(ctypes.POINTER(Node))),
        ('numStations', ctypes.c_int)
    ]

# Load the DLL
metro_dll = ctypes.CDLL('./metro.dll')  # Replace with the actual DLL filename

# Load the functions from the DLL
get_route_text = metro_dll.getRouteText
get_route_text.restype = ctypes.c_char_p

initialize_map = metro_dll.initializeMap
initialize_map.argtypes = [ctypes.c_int]
initialize_map.restype = ctypes.POINTER(MetroMap)

add_station = metro_dll.addStation
add_station.argtypes = [ctypes.POINTER(MetroMap), ctypes.c_char_p, ctypes.c_int]

add_connection = metro_dll.addConnection
add_connection.argtypes = [ctypes.POINTER(MetroMap), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]

print_map = metro_dll.printMap
print_map.argtypes = [ctypes.POINTER(MetroMap)]

free_map = metro_dll.freeMap
free_map.argtypes = [ctypes.POINTER(MetroMap)]

dijkstra = metro_dll.dijkstra
dijkstra.argtypes = [ctypes.POINTER(MetroMap), ctypes.c_char_p, ctypes.c_char_p]
dijkstra.restype = ctypes.c_char_p

initiate = metro_dll.initiate
initiate.restype = ctypes.POINTER(MetroMap)

# Initialize the metro map
metro_map = initiate()

# Print the initial map
print("Initial Metro Map:")
print_map(metro_map)

# Get user input for "From" and "To" stations
from_station = input("Enter the 'From' station: ")
to_station = input("Enter the 'To' station: ")

# Find and print the route using Dijkstra's algorithm
result = dijkstra(metro_map, from_station.encode('utf-8'), to_station.encode('utf-8'))
print(result.decode('utf-8'))

# Free the memory allocated for the metro map
free_map(metro_map)
