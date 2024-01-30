
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

# Print the initial map
print("Initial Metro Map:")
print_map(metro_map)

# Tkinter GUI setup
class MetroNavigatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Metro Navigator")

        # Entry widgets for "From" and "To" stations
        self.from_station_entry = ttk.Entry(master)
        self.from_station_entry.grid(row=0, column=0, padx=5, pady=5)

        self.to_station_entry = ttk.Entry(master)
        self.to_station_entry.grid(row=0, column=1, padx=5, pady=5)

        # Find Route button
        self.find_route_button = ttk.Button(master, text="Find Route", command=self.find_route)
        self.find_route_button.grid(row=1, column=0, columnspan=2, pady=10)

         # Canvas for drawing red dot lines below the route button
        self.line_canvas = tk.Canvas(master, width=500, height=50, background='white')
        self.line_canvas.grid(row=1, column=0, columnspan=2, padx=10)

        # Canvas for drawing red dot lines
        self.canvas = tk.Canvas(master, width=500, height=300, background='white')
        self.canvas.grid(row=2, column=0, columnspan=2, padx=10)

        # Result label
        self.result_label = ttk.Label(master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=5)

    def find_route(self):
        from_station = self.from_station_entry.get()
        to_station = self.to_station_entry.get()

      
        # Clear previous drawings
        self.canvas.delete("all")
        self.line_canvas.delete("all")

# Draw horizontal lines connecting red dots below the route button
        for i in range(metro_map.contents.numStations - 1):
            x1 = i * 30 + 15
            x2 = (i + 1) * 30 + 15
            self.line_canvas.create_line(x1, 10, x2, 10, fill='red')
            self.line_canvas.create_line(x1, 40, x2, 40, fill='red')

        # Draw horizontal lines connecting red dots
        for i in range(metro_map.contents.numStations - 1):
            y1 = i * 30 + 15
            y2 = (i + 1) * 30 + 15
            self.canvas.create_line(10, y1, 250, y1, fill='red')
            self.canvas.create_line(10, y2, 250, y2, fill='red')

        # Draw red dots and station names
        for i in range(metro_map.contents.numStations):
            station_name = metro_map.contents.graph[i][0].station.decode('utf-8')
            center_x = 250
            center_y = i * 30 + 15
            self.canvas.create_oval(center_x - 5, center_y - 5, center_x + 5, center_y + 5, fill='red')
            self.canvas.create_text(center_x + 20, center_y, text=station_name, anchor='w')

        
        # Find and display the route using Dijkstra's algorithm
        result = dijkstra(metro_map, from_station.encode('utf-8'), to_station.encode('utf-8'))
        self.result_label.config(text=result.decode('utf-8'))
root = tk.Tk()
app = MetroNavigatorGUI(root)

 
# Run the Tkinter event loop
root.mainloop()
 
# Free the memory allocated for the metro map
free_map(metro_map)

