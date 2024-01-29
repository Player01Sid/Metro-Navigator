import ctypes
import tkinter as tk
from tkinter import ttk

# Load the DLL
metro_dll = ctypes.CDLL("../c backend/metro.dll")

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

free_map = metro_dll.freeMap
free_map.argtypes = [ctypes.POINTER(MetroMap)]

dijkstra = metro_dll.dijkstra
dijkstra.argtypes = [ctypes.POINTER(MetroMap), ctypes.c_char_p, ctypes.c_char_p]
dijkstra.restype = ctypes.c_char_p

noStations = metro_dll.noStations
noStations.argtypes = [ctypes.POINTER(MetroMap)]
noStations.restype = ctypes.c_int

# Load the initiate function from the DLL
initiate = metro_dll.initiate
initiate.restype = ctypes.POINTER(MetroMap)

# Initialize the metro map
metro_map = initiate()

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
        self.find_route_button.grid(row=2, column=0, columnspan=1, pady=10)
        self.noStations_button = ttk.Button(master, text="No. of Stations", command=self.count_stations)
        self.noStations_button.grid(row=2, column=1, columnspan=2, pady=10)

        # Add a Canvas widget for the station graph
        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(master, text="")
        self.result_label.grid(row=4, column=0, columnspan=3, pady=5)

    def count_stations(self):
        result = noStations(metro_map)
        self.result_label.config(text="No. of Stations: " + str(result))

    def find_route(self):
        # Get user input for "From" and "To" stations
        from_station = self.from_entry.get()
        to_station = self.to_entry.get()

        # Find the route using Dijkstra's algorithm
        result_bytes = dijkstra(metro_map, from_station.encode('utf-8'), to_station.encode('utf-8'))

        # Convert bytes to string
        result_str = result_bytes.decode('utf-8')

        # Display the result using generate_graph_gui
        self.generate_graph_gui(result_str)

    def generate_graph_gui(self, input_str):
        stations = self.parse_input(input_str)

        # Clear the existing drawings on the canvas
        self.canvas.delete("all")

        dot_radius = 3
        line_width = 0.5  # Adjusted to one-third of the original
        line_length_factor = 0.55  # Adjusted for a slightly shorter line length
        color_change_spacing = 16  # Increased space between dots of different colors
        vertical_shift = 4  # Shift "Change Train" text 4 pixels down
        horizontal_shift = 4  # Shift "Change Train" text 4 pixels to the right

        for i, (station, color) in enumerate(stations):
            x = 100
            y = 50 + i * (15 + color_change_spacing)

            # Assign colors based on the numerical value
            if color == 1:
                dot_color = 'red'
            elif color == 2:
                dot_color = 'green'
            elif color == 3:
                dot_color = 'yellow'
            elif color == 4:
                dot_color = 'blue'
            else:
                dot_color = 'green'  # Default to green for unknown colors

            self.canvas.create_oval(x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius, outline='black', fill='white', width=1)
            self.canvas.create_oval(x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius, outline='black', fill=dot_color, width=1)
            self.canvas.create_text(x + 2*dot_radius, y, text=station, anchor='w')

            if i < len(stations) - 1:
                next_color = stations[i + 1][1]
                if color != next_color:
                    # Display "Change Train" 4 pixels down and 4 pixels to the right instead of drawing a line
                    change_x = x + 20 + horizontal_shift
                    change_y = y + 8 + vertical_shift
                    self.canvas.create_text(change_x, change_y, text="Change Train", anchor='w')
                else:
                    line_x = x
                    line_y1 = y + dot_radius
                    line_y2 = y + 15 + color_change_spacing - dot_radius
                    line_length = (line_y2 - line_y1) * line_length_factor
                    line_y2 = y + 15 + color_change_spacing
                    self.canvas.create_line(line_x, line_y1, line_x, line_y2, fill='black', width=line_width)






    def parse_input(self, input_str):
        # Check if the input string starts with "Route: "
        if input_str.startswith("Route: "):
            input_str = input_str[len("Route: "):]  # Remove "Route: " from the beginning

        # Split the input string based on '->' and remove leading/trailing spaces
        stations = [s.strip() for s in input_str.split("->")]

        # Ensure each station has the expected format before parsing
        valid_stations = []
        for s in stations:
            parts = s.split(":")
            if len(parts) == 2 and parts[1].strip().isdigit():
                valid_stations.append((parts[0].strip(), int(parts[1].strip())))

        return valid_stations




# Create the Tkinter window
root = tk.Tk()
app = MetroNavigatorGUI(root)

# Run the Tkinter event loop
root.mainloop()

# Free the memory allocated for the metro map
free_map(metro_map)
