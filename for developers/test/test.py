import tkinter as tk
from tkinter import ttk

class MetroNavigatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("METRO NAVIGATOR APP")

        # Create dropdowns for from and to stations
        self.from_station_label = ttk.Label(root, text="FROM STATION:")
        self.from_station_label.grid(row=0, column=0, padx=10, pady=10)
        self.from_station_var = tk.StringVar()
        self.from_station_dropdown = ttk.Combobox(root, textvariable=self.from_station_var)
        self.from_station_dropdown['values'] = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E',
                                                'Station F', 'Station G', 'Station H', 'Station I', 'Station J',
                                                'Station K', 'Station L', 'Station M', 'Station N', 'Station O',
                                                'Station P', 'Station Q', 'Station R', 'Station S', 'Station T']
        self.from_station_dropdown.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.to_station_label = ttk.Label(root, text="TO STATION:")
        self.to_station_label.grid(row=1, column=0, padx=10, pady=10)
        self.to_station_var = tk.StringVar()
        self.to_station_dropdown = ttk.Combobox(root, textvariable=self.to_station_var)
        self.to_station_dropdown['values'] = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E',
                                              'Station F', 'Station G', 'Station H', 'Station I', 'Station J',
                                              'Station K', 'Station L', 'Station M', 'Station N', 'Station O',
                                              'Station P', 'Station Q', 'Station R', 'Station S', 'Station T']
        self.to_station_dropdown.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        # Create a "Find Route" button
        self.find_route_button = ttk.Button(root, text="FIND ROUTE", command=self.find_route)
        self.find_route_button.grid(row=2, column=0, columnspan=3, pady=10, sticky='ew')  # Centered horizontally

        # Create a canvas for drawing stations, links, and time information
        self.canvas = tk.Canvas(root, width=200, height=300)
        self.canvas.grid(row=3, column=0, columnspan=3, pady=10)

    def find_route(self):
        from_station = self.from_station_var.get()
        to_station = self.to_station_var.get()

        # Replace this with your actual route-finding logic
        # Assuming a simple route for demonstration purposes
        route_found = [f"Station {i}" for i in range(ord(from_station[-1]), ord(to_station[-1]) + 1)]
        time_taken = len(route_found) * 5  # Replace with your time calculation logic

        # Draw red dots and lines on the canvas with station names
        self.canvas.delete("all")  # Clear existing drawings

        for i, station in enumerate(route_found):
            x = 100
            y = 50 + i * 30
            radius = 5
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="red")  # Draw red dot

            # Add station names on the left side of the red dot
            self.canvas.create_text(x - radius - 5, y, text=station, anchor="e", fill="black")

            if i < len(route_found) - 1:
                # Draw a line between stations
                y_next = y + 30
                self.canvas.create_line(x, y + radius, x, y_next - radius, fill="red", width=2)

                # Display time information on the right side of the red dot
                self.canvas.create_text(x + radius + 5, y, text=f"{time_taken} min", anchor="w", fill="blue")

if __name__ == "__main__":
    root = tk.Tk()
    app = MetroNavigatorApp(root)
    root.mainloop()
