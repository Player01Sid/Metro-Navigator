#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

// Define the maximum number of stations
#define MAX_STATIONS 100

// Structure to represent a station
typedef struct {
    char name[50];
    int distance;
} Station;

// Structure to represent an edge between two stations
typedef struct {
    int source;
    int destination;
    int weight;
} Edge;

// Structure to represent the metro network
typedef struct {
    Station stations[MAX_STATIONS];
    Edge edges[MAX_STATIONS * (MAX_STATIONS - 1)]; // Assuming a fully connected network
    int numStations;
    int numEdges;
} MetroNetwork;

// Function to initialize the metro network
void initializeMetroNetwork(MetroNetwork *metro) {
    metro->numStations = 0;
    metro->numEdges = 0;
}

// Function to add a station to the metro network
void addStation(MetroNetwork *metro, const char *name) {
    if (metro->numStations < MAX_STATIONS) {
        Station newStation;
        sprintf(newStation.name, "%s", name);
        newStation.distance = INT_MAX; // Initialize distance to infinity
        metro->stations[metro->numStations++] = newStation;
    } else {
        printf("Maximum number of stations reached.\n");
    }
}

// Function to add an edge between two stations
void addEdge(MetroNetwork *metro, int source, int destination, int weight) {
    if (metro->numEdges < MAX_STATIONS * (MAX_STATIONS - 1)) {
        Edge newEdge;
        newEdge.source = source;
        newEdge.destination = destination;
        newEdge.weight = weight;
        metro->edges[metro->numEdges++] = newEdge;
    } else {
        printf("Maximum number of edges reached.\n");
    }
}

// Function to perform Dijkstra's algorithm to find the distance between two stations
void dijkstra(MetroNetwork *metro, int source, int destination) {
    // TODO: Implement Dijkstra's algorithm here
    // Update the distance of each station in the metro network
    // Print the distance between the source and destination stations
}

int main() {
    MetroNetwork metro;
    initializeMetroNetwork(&metro);

    // Adding stations
    addStation(&metro, "Station A");
    addStation(&metro, "Station B");
    addStation(&metro, "Station C");
    // ... Add more stations as needed

    // Adding edges between stations
    addEdge(&metro, 0, 1, 5); // Edge between Station A and Station B with weight 5
    addEdge(&metro, 1, 2, 3); // Edge between Station B and Station C with weight 3
    // ... Add more edges as needed

    // Example usage: find the distance between Station A and Station C
    dijkstra(&metro, 0, 2);

    return 0;
}
