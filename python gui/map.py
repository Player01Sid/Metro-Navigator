import tkinter as tk

# Define station coordinates
stations = {
    'A': (0, 1), 'B': (1, 2), 'C': (2, 2), 'D': (3, 2),
    'E': (4, 2), 'F': (5, 2), 'G': (6, 2), 'H': (7, 2),
    'I': (4, 0), 'J': (4, 1), 'K': (4, 3), 'L': (4, 4),
    'M': (4, 5), 'N': (3, 6), 'O': (2, 7), 'P': (1, 4),
    'Q': (2, 4), 'R': (3, 4), 'S': (5, 4), 'T': (6, 4),
    'U': (7, 4), 'V': (2, 1), 'W': (2, 3), 'X': (3, 3),
    'Y': (5, 5), 'Z': (6, 6),
}

# Create a window
root = tk.Tk()
root.title("Metro Map")

# Create a canvas
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Plot connections on the canvas
connections = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('C', 'E'),
               ('C', 'F'), ('C', 'G'), ('C', 'H'), ('I', 'J'),
               ('J', 'K'), ('K', 'L'), ('L', 'M'), ('M', 'N'),
               ('N', 'O'), ('P', 'Q'), ('Q', 'R'), ('R', 'S'),
               ('S', 'T'), ('T', 'U'), ('B', 'W'), ('V', 'B'),
               ('X', 'W'), ('X', 'L'), ('Y', 'Z'), ('Y', 'L')]

for start, end in connections:
    x1, y1 = stations[start]
    x2, y2 = stations[end]
    canvas.create_line(x1 * 50 + 10, y1 * 50 + 10, x2 * 50 + 10, y2 * 50 + 10, fill='black', width=2)

# Plot stations on the canvas
for station, (x, y) in stations.items():
    color = 'red' if 'A' <= station <= 'H' else 'yellow' if 'I' <= station <= 'O' else 'blue' if 'P' <= station <= 'U' else 'green' if 'V' <= station <= 'Z' else 'gray'
    canvas.create_oval(x * 50, y * 50, x * 50 + 20, y * 50 + 20, fill=color)
    canvas.create_text(x * 50 + 10, y * 50 + 10, text=station, font=('Helvetica', 8), fill='black')

# Run the tkinter event loop
root.mainloop()
