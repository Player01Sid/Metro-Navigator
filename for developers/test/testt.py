import tkinter as tk
from tkinter import ttk

def navigate():
    from_station = from_station_var.get()
    to_station = to_station_var.get()
    result_label.config(text=f"Navigate from {from_station} to {to_station}")

# Create the main window
window = tk.Tk()
window.title("Metro Navigation")

# Create and place labels
from_label = tk.Label(window, text="From Station:")
from_label.grid(row=0, column=0, padx=10, pady=10)

to_label = tk.Label(window, text="To Station:")
to_label.grid(row=1, column=0, padx=10, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Create and place dropdown lists
stations = ["Station A", "Station B", "Station C", "Station D", "Station E"]
from_station_var = tk.StringVar()
from_station_dropdown = ttk.Combobox(window, textvariable=from_station_var, values=stations)
from_station_dropdown.grid(row=0, column=1, padx=10, pady=10)
from_station_dropdown.current(0)  # Set default value

to_station_var = tk.StringVar()
to_station_dropdown = ttk.Combobox(window, textvariable=to_station_var, values=stations)
to_station_dropdown.grid(row=1, column=1, padx=10, pady=10)
to_station_dropdown.current(1)  # Set default value

# Create and place navigate button
navigate_button = tk.Button(window, text="Navigate", command=navigate)
navigate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Start the main event loop
window.mainloop()
