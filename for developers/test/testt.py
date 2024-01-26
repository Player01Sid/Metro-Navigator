import tkinter as tk
from tkinter import ttk

class MetroNavigatorApp:
    def __init__(self, root):
        # ... (previous code remains unchanged)

        # Create a canvas for drawing stations, links, and time information
        self.canvas = tk.Canvas(root, width=500, height=100)
        self.canvas.grid(row=3, column=0, columnspan=3, pady=10)

    def find_route(self):
        from_station = self.from_station_var.get()
        to_station = self.to_station_var.get()

        # Replace this with your actual route-finding logic
        # Assuming a simple route for demonstration purposes
        route_found = [f"Station {i}" for i in range(ord(from_station[-1]), ord(to_station[-1]) + 1)]
        time_taken = len(route_found) * 5  # Replace with your time calculation logic

        # Draw red dots and links on the canvas
        self.canvas.delete("all")  # Clear existing drawings

        for i, station in enumerate(route_found):
            x = 30 + i * 30
            y = 50
            radius = 5
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="red")  # Draw red dot

            if i < len(route_found) - 1:
                # Draw a line between stations
                x_next = x + 30
                self.canvas.create_line(x + radius, y, x_next - radius, y, fill="red", width=2)

                # Display time information
                self.canvas.create_text((x + x_next) // 2, y - 10, text=f"{time_taken} min", fill="blue")

if __name__ == "__main__":
    root = tk.Tk()
    app = MetroNavigatorApp(root)
    root.mainloop()
