#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

// Structure to represent a station
typedef struct {
    char name[20];
    int id;
} 
Station;

// Structure to represent an edge between two stations
typedef struct {
    int source;
    int destination;
    int distance; // distance in meters
    int time;     // travel time in minutes
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

// Function to add an edge between two stations
void addEdge(MetroGraph *graph, int source, int destination, int distance, int time) {
    if (graph->numEdges < INT_MAX) {
        Edge newEdge;
        newEdge.source = source;
        newEdge.destination = destination;
        newEdge.distance = distance;
        newEdge.time = time;
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
    printf("| %-8s | %-20s | %-20s | %-10s | %-8s |\n", "Edge ID", "FROM Station", "TO Station", "Distance (m)", "Time (min)");
    printf("|----------|----------------------|----------------------|-------------|----------|\n");
    for (int i = 0; i < graph->numEdges; ++i) {
        printf("| %-8d | %-20d | %-20d | %-11d | %-8d |\n",
               i,
               graph->edges[i].source,
               graph->edges[i].destination,
               graph->edges[i].distance,
               graph->edges[i].time);
    }
}

// Dijkstra's algorithm to find the shortest path between two stations
void dijkstra(MetroGraph *graph, int source, int destination, int *distances, int *previous) {
    int visited[graph->numStations];

    // Initialize distances and previous array
    for (int i = 0; i < graph->numStations; ++i) {
        distances[i] = INT_MAX;
        previous[i] = -1;
        visited[i] = 0;
    }

    distances[source] = 0;

    for (int count = 0; count < graph->numStations - 1; ++count) {
        // Find the minimum distance vertex from the set of vertices not yet processed
        int minDistance = INT_MAX, minIndex = -1;
        for (int v = 0; v < graph->numStations; ++v) {
            if (!visited[v] && distances[v] < minDistance) {
                minDistance = distances[v];
                minIndex = v;
            }
        }

        // Mark the picked vertex as visited
        visited[minIndex] = 1;

        // Update the distance value of the neighboring vertices
        for (int v = 0; v < graph->numStations; ++v) {
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
    int distances[graph->numStations];
    int previous[graph->numStations];

    dijkstra(graph, source, destination, distances, previous);

    return distances[destination];
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
        printf("Enter the name of Station %c: ", 'A' + i);
        scanf("%s", stationName);
        addStation(&metro, stationName);
    }

    // Adding edges with distances and times
    for (int i = 0; i < numStations - 1; ++i) {
        // Connect adjacent stations with distances and times
        int distance, time;
        printf("Enter distance (in meters) and time (in minutes) between Station %c and Station %c: ", 'A' + i, 'A' + i + 1);
        scanf("%d %d", &distance, &time);

        addEdge(&metro, i, i + 1, distance, time);
        addEdge(&metro, i + 1, i, distance, time);
    }

    // Print the metro graph
    printMetroGraph(&metro);

    // Example usage of Dijkstra's algorithm
    int source, destination;
    printf("\nEnter the source station (ID): ");
    scanf("%d", &source);
    printf("Enter the destination station (ID): ");
    scanf("%d", &destination);

    if (source < 0 || source >= numStations || destination < 0 || destination >= numStations) {
        printf("Invalid source or destination station ID. Exiting.\n");
        return 1;
    }

    int distance = findDistance(&metro, source, destination); // Find the distance between two stations
    printf("\nDistance between Station %c and Station %c: %d minutes\n", 'A' + source, 'A' + destination, distance);

    // Free dynamically allocated memory
    free(metro.stations);
    free(metro.edges);

    return 0;
}
