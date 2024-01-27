#shows red dots only 

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

        # Create a canvas for drawing stations and links
        self.canvas = tk.Canvas(root, width=500, height=100)
        self.canvas.grid(row=3, column=0, columnspan=3, pady=10)

    def find_route(self):
        from_station = self.from_station_var.get()
        to_station = self.to_station_var.get()

        # Replace this with your actual route-finding logic
        # Assuming a simple route for demonstration purposes
        route_found = [f"Station {i}" for i in range(ord(from_station[-1]), ord(to_station[-1]) + 1)]

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

if __name__ == "__main__":
    root = tk.Tk()
    app = MetroNavigatorApp(root)
    root.mainloop()




                       
      #displaying time only                 
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
        self.canvas = tk.Canvas(root, width=100, height=300)
        self.canvas.grid(row=3, column=0, columnspan=3, pady=10)

    def find_route(self):
        from_station = self.from_station_var.get()
        to_station = self.to_station_var.get()

        # Replace this with your actual route-finding logic
        # Assuming a simple route for demonstration purposes
        route_found = [f"Station {i}" for i in range(ord(from_station[-1]), ord(to_station[-1]) + 1)]
        time_taken = len(route_found) * 5  # Replace with your time calculation logic

        # Draw red dots and lines on the canvas
        self.canvas.delete("all")  # Clear existing drawings

        for i, station in enumerate(route_found):
            x = 50
            y = 50 + i * 30
            radius = 5
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="red")  # Draw red dot

            if i < len(route_found) - 1:
                # Draw a line between stations
                y_next = y + 30
                self.canvas.create_line(x, y + radius, x, y_next - radius, fill="red", width=2)

                # Display time information
                self.canvas.create_text(x + 15, (y + y_next) // 2, text=f"{time_taken} min", fill="blue")

if __name__ == "__main__":
    root = tk.Tk()
    app = MetroNavigatorApp(root)
    root.mainloop()
                   
                   
                   
                   
                   
                   
                   
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_STATIONS 10

// Structure to represent a station
typedef struct {
    char name[20];
    int id;
} Station;

// Structure to represent an edge between two stations
typedef struct {
    int source;
    int destination;
    int distance;
} Edge;

// Graph structure
typedef struct {
    int numStations;
    int numEdges;
    Station stations[MAX_STATIONS];
    Edge edges[MAX_STATIONS * (MAX_STATIONS - 1)]; // Assuming a dense graph
} MetroGraph;

// Function to initialize the metro graph
void initializeMetroGraph(MetroGraph *graph) {
    graph->numStations = 0;
    graph->numEdges = 0;
}

// Function to add a station to the metro graph
void addStation(MetroGraph *graph, const char *name) {
    if (graph->numStations < MAX_STATIONS) {
        Station newStation;
        snprintf(newStation.name, sizeof(newStation.name), "%s", name);
        newStation.id = graph->numStations;
        graph->stations[graph->numStations++] = newStation;
    } else {
        printf("Cannot add more stations. Maximum limit reached.\n");
    }
}

// Function to add an edge between two stations
void addEdge(MetroGraph *graph, int source, int destination, int distance) {
    if (graph->numEdges < MAX_STATIONS * (MAX_STATIONS - 1)) {
        Edge newEdge;
        newEdge.source = source;
        newEdge.destination = destination;
        newEdge.distance = distance;
        graph->edges[graph->numEdges++] = newEdge;
    } else {
        printf("Cannot add more edges. Maximum limit reached.\n");
    }
}

// Function to print the metro graph
void printMetroGraph(MetroGraph *graph) {
    printf("Metro Graph:\n");
    printf("Stations:\n");
    for (int i = 0; i < graph->numStations; ++i) {
        printf("%d: %s\n", graph->stations[i].id, graph->stations[i].name);
    }
    printf("Edges:\n");
    for (int i = 0; i < graph->numEdges; ++i) {
        printf("%d -> %d : %d\n", graph->edges[i].source, graph->edges[i].destination, graph->edges[i].distance);
    }
}

// Dijkstra's algorithm to find the shortest path between two stations
void dijkstra(MetroGraph *graph, int source, int destination) {
    // TODO: Implement Dijkstra's algorithm
    // You'll need to use data structures like priority queue and maintain distances
    // between stations. This is a complex algorithm, and you may need to adapt it to
    // the specifics of your graph representation.
}

int main() {
    MetroGraph metro;
    initializeMetroGraph(&metro);

    // Adding stations
    addStation(&metro, "Station A");
    addStation(&metro, "Station B");
    addStation(&metro, "Station C");
    // Add more stations as needed

    // Adding edges with distances
    addEdge(&metro, 0, 1, 10); // Edge from Station A to Station B with distance 10
    addEdge(&metro, 1, 2, 15); // Edge from Station B to Station C with distance 15
    // Add more edges as needed

    // Print the metro graph
    printMetroGraph(&metro);

    // Example usage of Dijkstra's algorithm
    dijkstra(&metro, 0, 2); // Find the shortest path from Station A to Station C

    return 0;
}
                
                   
      #include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_STATIONS 20

// Structure to represent a station
typedef struct {
    char name[20];
    int id;
} Station;

// Structure to represent an edge between two stations
typedef struct {
    int source;
    int destination;
    int distance;
} Edge;

// Graph structure
typedef struct {
    int numStations;
    int numEdges;
    Station stations[MAX_STATIONS];
    Edge edges[MAX_STATIONS * (MAX_STATIONS - 1)]; // Assuming a dense graph
} MetroGraph;

// Function to initialize the metro graph
void initializeMetroGraph(MetroGraph *graph) {
    graph->numStations = 0;
    graph->numEdges = 0;
}

// Function to add a station to the metro graph
void addStation(MetroGraph *graph, const char *name) {
    if (graph->numStations < MAX_STATIONS) {
        Station newStation;
        snprintf(newStation.name, sizeof(newStation.name), "%s", name);
        newStation.id = graph->numStations;
        graph->stations[graph->numStations++] = newStation;
    } else {
        printf("Cannot add more stations. Maximum limit reached.\n");
    }
}

// Function to add an edge between two stations
void addEdge(MetroGraph *graph, int source, int destination, int distance) {
    if (graph->numEdges < MAX_STATIONS * (MAX_STATIONS - 1)) {
        Edge newEdge;
        newEdge.source = source;
        newEdge.destination = destination;
        newEdge.distance = distance;
        graph->edges[graph->numEdges++] = newEdge;
    } else {
        printf("Cannot add more edges. Maximum limit reached.\n");
    }
}

// Function to print the metro graph
void printMetroGraph(MetroGraph *graph) {
    printf("METRO NAVIGATION\n");
    printf("Number Of Stations:\n");
    for (int i = 0; i < graph->numStations; ++i) {
        printf("%d: %s\n", graph->stations[i].id, graph->stations[i].name);
    }
    printf("Edges:\n");
    for (int i = 0; i < graph->numEdges; ++i) {
        printf("%d -> %d : %d\n", graph->edges[i].source, graph->edges[i].destination, graph->edges[i].distance);
    }
}

// Dijkstra's algorithm to find the shortest path between two stations
void dijkstra(MetroGraph *graph, int source, int destination) {
    // TODO: Implement Dijkstra's algorithm
    // You'll need to use data structures like priority queue and maintain distances
    // between stations. This is a complex algorithm, and you may need to adapt it to
    // the specifics of your graph representation.
}

int main() {
    MetroGraph metro;
    initializeMetroGraph(&metro);

    // Adding 20 stations
    for (int i = 0; i < 20; ++i) {
        char stationName[20];
        snprintf(stationName, sizeof(stationName), "Station %c", 'A' + i);
        addStation(&metro, stationName);
    }

    // Adding edges with distances
    for (int i = 0; i < 19; ++i) {
        // Connect adjacent stations with distances
        addEdge(&metro, i, i + 1, 10);
        addEdge(&metro, i + 1, i, 10);
    }

    // Connect the first and last station to form a loop
    addEdge(&metro, 0, 19, 15);
    addEdge(&metro, 19, 0, 15);

    // Print the metro graph
    printMetroGraph(&metro);

    // Example usage of Dijkstra's algorithm
    dijkstra(&metro, 0, 19); // Find the shortest path from Station A to Station T

    return 0;
}








#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_STATIONS 20

// Structure to represent a station
typedef struct {
    char name[20];
    int id;
} Station;

// Structure to represent an edge between two stations
typedef struct {
    int source;
    int destination;
    int distance;
} Edge;

// Graph structure
typedef struct {
    int numStations;
    int numEdges;
    Station stations[MAX_STATIONS];
    Edge edges[MAX_STATIONS * (MAX_STATIONS - 1)]; // Assuming a dense graph
} MetroGraph;

// Function to initialize the metro graph
void initializeMetroGraph(MetroGraph *graph) {
    graph->numStations = 0;
    graph->numEdges = 0;
}

// Function to add a station to the metro graph
void addStation(MetroGraph *graph, const char *name) {
    if (graph->numStations < MAX_STATIONS) {
        Station newStation;
        snprintf(newStation.name, sizeof(newStation.name), "%s", name);
        newStation.id = graph->numStations;
        graph->stations[graph->numStations++] = newStation;
    } else {
        printf("Cannot add more stations. Maximum limit reached.\n");
    }
}

// Function to add an edge between two stations
void addEdge(MetroGraph *graph, int source, int destination, int distance) {
    if (graph->numEdges < MAX_STATIONS * (MAX_STATIONS - 1)) {
        Edge newEdge;
        newEdge.source = source;
        newEdge.destination = destination;
        newEdge.distance = distance;
        graph->edges[graph->numEdges++] = newEdge;
    } else {
        printf("Cannot add more edges. Maximum limit reached.\n");
    }
}

// Function to print the metro graph
void printMetroGraph(MetroGraph *graph) {
    printf("METRO NAVIGATION\n");
    printf("Metro Graph:\n");

    // Print Stations Table
    printf("| %-5s | %-20s |\n", "ID", "Station Name");
    printf("|--------|----------------------|\n");
    for (int i = 0; i < graph->numStations; ++i) {
        printf("| %-5d | %-20s |\n", graph->stations[i].id, graph->stations[i].name);
    }
    printf("\n");

    // Print Edges Table
    printf("| %-8s | %-14s | %-8s | %-8s |\n", "Edge ID", "Source", "Destination", "Distance");
    printf("|----------|----------------|------------|----------|\n");
    for (int i = 0; i < graph->numEdges; ++i) {
        printf("| %-8d | %-14d | %-10d | %-8d |\n",
               i,
               graph->edges[i].source,
               graph->edges[i].destination,
               graph->edges[i].distance);
    }
}

// Dijkstra's algorithm to find the shortest path between two stations
void dijkstra(MetroGraph *graph, int source, int destination, int *distances, int *previous) {
    int visited[MAX_STATIONS] = {0};

    // Initialize distances and previous array
    for (int i = 0; i < MAX_STATIONS; ++i) {
        distances[i] = INT_MAX;
        previous[i] = -1;
    }

    distances[source] = 0;

    for (int count = 0; count < MAX_STATIONS - 1; ++count) {
        // Find the minimum distance vertex from the set of vertices not yet processed
        int minDistance = INT_MAX, minIndex = -1;
        for (int v = 0; v < MAX_STATIONS; ++v) {
            if (!visited[v] && distances[v] < minDistance) {
                minDistance = distances[v];
                minIndex = v;
            }
        }

        // Mark the picked vertex as visited
        visited[minIndex] = 1;

        // Update the distance value of the neighboring vertices
        for (int v = 0; v < MAX_STATIONS; ++v) {
            if (!visited[v] && graph->edges[v].distance &&
                distances[minIndex] != INT_MAX &&
                distances[minIndex] + graph->edges[minIndex].distance < distances[v]) {
                distances[v] = distances[minIndex] + graph->edges[minIndex].distance;
                previous[v] = minIndex;
            }
        }
    }
}

// Function to find the distance between two stations
int findDistance(MetroGraph *graph, int source, int destination) {
    int distances[MAX_STATIONS];
    int previous[MAX_STATIONS];

    dijkstra(graph, source, destination, distances, previous);

    return distances[destination];
}

int main() {
    MetroGraph metro;
    initializeMetroGraph(&metro);

    // Adding 20 stations
    for (int i = 0; i < 20; ++i) {
        char stationName[20];
        snprintf(stationName, sizeof(stationName), "Station %c", 'A' + i);
        addStation(&metro, stationName);
    }

    // Adding edges with distances
    for (int i = 0; i < 19; ++i) {
        // Connect adjacent stations with distances
        addEdge(&metro, i, i + 1, 10);
        addEdge(&metro, i + 1, i, 10);
    }

    // Connect the first and last station to form a loop
    addEdge(&metro, 0, 19, 15);
    addEdge(&metro, 19, 0, 15);

    // Print the metro graph
    printMetroGraph(&metro);

    // Example usage of Dijkstra's algorithm
    int distance = findDistance(&metro, 0, 19); // Find the distance from Station A to Station T
    printf("\nDistance between Station A and Station T: %d\n", distance);

    return 0;
}

















             
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                       
                       
                       
                       
