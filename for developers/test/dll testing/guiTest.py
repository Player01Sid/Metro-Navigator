
import ctypes
import tkinter as tk
from tkinter import ttk

# Load the DLL
metro_dll = ctypes.CDLL(r'C:\Users\gulsh\OneDrive\Documents\GitHub\Metro-Navigator\for developers\test\dll testing\metro.dll')

# Define Node structure first
class Node(ctypes.Structure):
    _fields_ = [
        ('station', ctypes.c_char * 50),
        ('time', ctypes.c_int),
        ('lineColors', ctypes.c_int * 5),
        ('numLines', ctypes.c_int),
        ('next', ctypes.POINTER('Node'))
    ]


# Define MetroMap structure
class MetroMap(ctypes.Structure):
    _fields_ = [
        ('graph', ctypes.POINTER(ctypes.POINTER(Node))),
        ('numStations', ctypes.c_int)
    ]


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






# Load the initiate function from the DLL
initiate = metro_dll.initiate
initiate.restype = ctypes.POINTER(MetroMap)

# Initialize the metro map
metro_map = initiate()

# Tkinter GUI setup
class MetroNavigatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Metro Navigator")
        self.from_label = ttk.Label(master, text="From Station:")
        self.from_label.grid(row=0, column=0, padx=5, pady=5)
        self.from_entry = ttk.Entry(master)
        self.from_entry.grid(row=0, column=1, padx=5, pady=5)

        self.to_label = ttk.Label(master, text="To Station:")
        self.to_label.grid(row=1, column=0, padx=5, pady=5)
        self.to_entry = ttk.Entry(master)
        self.to_entry.grid(row=1, column=1, padx=5, pady=5)
        self.find_route_button = ttk.Button(master, text="Find Route", command=self.find_route)
        self.find_route_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=5)

    def find_route(self):
        # Get user input for "From" and "To" stations
        from_station = self.from_entry.get()
        to_station = self.to_entry.get()

        # Find and print the route using Dijkstra's algorithm
        result = dijkstra(metro_map, from_station.encode('utf-8'), to_station.encode('utf-8'))
        self.result_label.config(text=result.decode('utf-8'))




   

# Create the Tkinter window
root = tk.Tk()
app = MetroNavigatorGUI(root)

# Print the initial map
print("Initial Metro Map:")
print_map(metro_map)


# Run the Tkinter event loop
root.mainloop()

# Free the memory allocated for the metro map
free_map(metro_map)
