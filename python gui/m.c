


#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>

// Structure to represent a station
typedef struct {
    char name[20];
    int id;
} Station;

// Structure to represent an edge between two stations
typedef struct {
    int source;
    int destination;
} Edge;

// Graph structure
typedef struct {
    int numStations;
    int numEdges;
    Station *stations;
    Edge *edges;
} MetroGraph;

// Function to initialize the metro graph
void initializeMetroGraph(MetroGraph *graph, int numStations) {
    graph->numStations = 0;
    graph->numEdges = 0;
    graph->stations = (Station *)malloc(numStations * sizeof(Station));
    graph->edges = (Edge *)malloc(numStations * (numStations - 1) * sizeof(Edge));
}

// Function to add a station to the metro graph
void addStation(MetroGraph *graph, const char *name) {
    if (graph->numStations < INT_MAX) {
        Station newStation;
        snprintf(newStation.name, sizeof(newStation.name), "%s", name);
        newStation.id = graph->numStations;
        graph->stations[graph->numStations++] = newStation;
    } else {
        printf("Cannot add more stations. Maximum limit reached.\n");
    }
}

// Function to find the station ID by name
int findStationID(MetroGraph *graph, const char *name) {
    for (int i = 0; i < graph->numStations; ++i) {
        if (strcmp(graph->stations[i].name, name) == 0) {
            return graph->stations[i].id;
        }
    }
    return -1; // Station not found
}

// Function to add an edge between two stations
void addEdge(MetroGraph *graph, int source, int destination) {
    if (graph->numEdges < INT_MAX) {
        Edge newEdge;
        newEdge.source = source;
        newEdge.destination = destination;
        graph->edges[graph->numEdges++] = newEdge;
    } else {
        printf("Cannot add more edges. Maximum limit reached.\n");
    }
}

// Function to print the metro graph
void printMetroGraph(MetroGraph *graph) {
    printf("METRO NAVIGATION\n");

    // Print Stations Table
    printf("\nStations Table:\n");
    printf("| %-5s | %-20s |\n", "ID", "Station Name");
    printf("|--------|----------------------|\n");
    for (int i = 0; i < graph->numStations; ++i) {
        printf("| %-5d | %-20s |\n", graph->stations[i].id, graph->stations[i].name);
    }
    printf("\n");

    // Print Edges Table
    printf("Edges Table:\n");
    printf("| %-8s | %-20s | %-20s |\n", "Edge ID", "FROM Station", "TO Station");
    printf("|----------|----------------------|----------------------|\n");
    for (int i = 0; i < graph->numEdges; ++i) {
        printf("| %-8d | %-20d | %-20d |\n",
               i,
               graph->edges[i].source,
               graph->edges[i].destination);
    }
}

// Dijkstra's algorithm to find the shortest path between two stations
void dijkstra(MetroGraph *graph, int source, int destination, int *previous) {
    int visited[graph->numStations];

    // Initialize previous array
    for (int i = 0; i < graph->numStations; ++i) {
        previous[i] = -1;
        visited[i] = 0;
    }

    for (int count = 0; count < graph->numStations - 1; ++count) {
        // Find the minimum distance vertex from the set of vertices not yet processed
        int minIndex = -1;
        for (int v = 0; v < graph->numStations; ++v) {
            if (!visited[v] && (minIndex == -1 || v < minIndex)) {
                minIndex = v;
            }
        }

        // Mark the picked vertex as visited
        visited[minIndex] = 1;

        // Update the previous array based on the neighboring vertices
        for (int v = 0; v < graph->numStations; ++v) {
            if (!visited[v] && graph->edges[v].source == minIndex) {
                previous[v] = minIndex;
            }
        }
    }
}

// Function to find the distance between two stations
int findDistance(MetroGraph *graph, int source, int destination) {
    int previous[graph->numStations];

    dijkstra(graph, source, destination, previous);

    // Count the number of stations between source and destination
    int distance = 0;
    int current = destination;

    while (current != source && current != -1) {
        current = previous[current];
        ++distance;
    }

    return (current == source) ? distance : -1; // Return -1 if there is no path
}

int main() {
    int numStations;

    // Get the number of stations from the user
    printf("Enter the number of stations (up to 10): ");
    scanf("%d", &numStations);

    if (numStations <= 0 || numStations > 10) {
        printf("Invalid number of stations. Exiting.\n");
        return 1;
    }

    MetroGraph metro;
    initializeMetroGraph(&metro, numStations);

    // Adding stations
    for (int i = 0; i < numStations; ++i) {
        char stationName[20];
        printf("Enter the name of Station %d: ", i + 1);
        scanf("%s", stationName);
        addStation(&metro, stationName);
    }

    // Adding edges
    for (int i = 0; i < numStations - 1; ++i) {
        // Connect adjacent stations
        printf("Enter the index of the destination station for Station %s: ", metro.stations[i].name);
        int destination;
        scanf("%d", &destination);

        if (destination < 0 || destination >= numStations) {
            printf("Invalid destination index. Exiting.\n");
            return 1;
        }

        addEdge(&metro, i, destination);
    }

    // Print the metro graph
    printMetroGraph(&metro);

    // Example usage of Dijkstra's algorithm
    char sourceName[20], destinationName[20];
    int source, destination;

    // Get source station name from the user
    printf("\nEnter the source station name: ");
    scanf("%s", sourceName);
    source = findStationID(&metro, sourceName);

    // Get destination station name from the user
    printf("Enter the destination station name: ");
    scanf("%s", destinationName);
    destination = findStationID(&metro, destinationName);

    if (source == -1 || destination == -1) {
        printf("Invalid source or destination station name. Exiting.\n");
        return 1;
    }

    int distance = findDistance(&metro, source, destination); // Find the distance between two stations

    if (distance != -1) {
        printf("\nNumber of stations between %s and %s: %d\n", sourceName, destinationName, distance);
    } else {
        printf("\nNo path between %s and %s\n", sourceName, destinationName);
    }

    // Free dynamically allocated memory
    free(metro.stations);
    free(metro.edges);

    return 0;
}









