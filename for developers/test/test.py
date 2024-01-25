
import tkinter as tk
from tkinter import ttk

class MetroNavigatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Metro Navigator App")

        # Create dropdowns for from and to stations
        self.from_station_label = ttk.Label(root, text="From Station:")
        self.from_station_label.grid(row=0, column=0, padx=10, pady=10)
        self.from_station_var = tk.StringVar()
        self.from_station_dropdown = ttk.Combobox(root, textvariable=self.from_station_var)
        self.from_station_dropdown['values'] = ['Station A', 'Station B', 'Station C']  # Add your station names
        self.from_station_dropdown.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.to_station_label = ttk.Label(root, text="To Station:")
        self.to_station_label.grid(row=1, column=0, padx=10, pady=10)
        self.to_station_var = tk.StringVar()
        self.to_station_dropdown = ttk.Combobox(root, textvariable=self.to_station_var)
        self.to_station_dropdown['values'] = ['Station A', 'Station B', 'Station C']  # Add your station names
        self.to_station_dropdown.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        # Create a "Find Route" button
        self.find_route_button = ttk.Button(root, text="Find Route", command=self.find_route)
        self.find_route_button.grid(row=2, column=0, columnspan=3, pady=10, sticky='ew')  # Centered horizontally

        # Create a table with time taken information
        self.time_table_label = ttk.Label(root, text="Time Taken Table:")
        self.time_table_label.grid(row=3, column=0, columnspan=3, pady=10)

        self.time_table_frame = ttk.Frame(root, borderwidth=2, relief='groove')
        self.time_table_frame.grid(row=4, column=0, columnspan=3, pady=10)

        self.time_table = ttk.Treeview(self.time_table_frame, columns=('From', 'To', 'Time Taken'))

        self.time_table.heading('#1', text='From')
        self.time_table.heading('#2', text='To')
        self.time_table.heading('#3', text='Time Taken')
        self.time_table.pack()

        # Add sample data to the time taken table
        data = [
            ('Station A', 'Station B', '10 minutes'),
            ('Station B', 'Station C', '15 minutes'),
            ('Station A', 'Station C', '20 minutes'),
        ]
        for i, (frm, to, time_taken) in enumerate(data, start=1):
            self.time_table.insert(parent='', index='end', iid=i, values=(frm, to, time_taken))
            if i % 2 == 0:  # Set background color for alternating rows
                self.time_table.tag_configure(f'row{i}', background='#f0f0f0')  # Light gray
            else:
                self.time_table.tag_configure(f'row{i}', background='#ffffff')  # White
            self.time_table.item(i, tags=f'row{i}')  # Apply the tag to the item

        # Create a linked list label
        self.linked_list_label = ttk.Label(root, text="ROUTES:")
        self.linked_list_label.grid(row=5, column=0, columnspan=3, pady=10)

        # Create a linked list display (simplified, you would need to implement a linked list class)
        self.linked_list_text = tk.Text(root, height=5, width=50)
        self.linked_list_text.grid(row=6, column=0, columnspan=3, pady=10)

        # Create a button to generate map (simplified, you would need a dedicated library for maps)
        self.generate_map_button = ttk.Button(root, text="Generate Map", command=self.generate_map)
        self.generate_map_button.grid(row=7, column=0, columnspan=3, pady=10)

        # Add sample data to the linked list
        linked_list_data = "Station A -> Station B -> Station C"
        self.linked_list_text.insert(tk.END, linked_list_data)

    def find_route(self):
        # Replace this with your route-finding logic based on the selected "From" and "To" stations
        from_station = self.from_station_var.get()
        to_station = self.to_station_var.get()
        
        # Replace this with your actual route-finding logic
        route_found = f"Route from {from_station} to {to_station}: Station A -> Station B -> Station C"

        # Display the route in the linked list text
        self.linked_list_text.delete(1.0, tk.END)  # Clear existing text
        self.linked_list_text.insert(tk.END, route_found)

    def generate_map(self):
        # Simplified code to generate a map (you would need a dedicated library for maps)
        map_window = tk.Toplevel(self.root)
        map_window.title("Metro Map")
        map_label = ttk.Label(map_window, text="Your Metro Map Goes Here")
        map_label.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = MetroNavigatorApp(root)
    root.mainloop()
