#include <stdio.h>
#include <limits.h>
#include<string.h>

#define MAX_LOCATIONS 10

// Structure to represent a location
typedef struct {
    char name[50];
} Location;

// Structure to represent the weighted graph
typedef struct {
    int adjacencyMatrix[MAX_LOCATIONS][MAX_LOCATIONS];
    Location locations[MAX_LOCATIONS];
    int numLocations;
} Map;

// Function to add a location to the map
void addLocation(Map* map, const char* name) {
    if (map->numLocations < MAX_LOCATIONS) {
        snprintf(map->locations[map->numLocations].name, sizeof(map->locations[map->numLocations].name), "%s", name);
        map->numLocations++;
    }
}

// Function to add a weighted edge between two locations
void addEdge(Map* map, int from, int to, int weight) {
    if (from >= 0 && from < map->numLocations && to >= 0 && to < map->numLocations) {
        map->adjacencyMatrix[from][to] = weight;
        map->adjacencyMatrix[to][from] = weight; // Assuming bidirectional connections
    }
}

// Function to find the index of a location by its name
int findLocationIndex(Map* map, const char* name) {
    for (int i = 0; i < map->numLocations; i++) {
        if (strcmp(map->locations[i].name, name) == 0) {
            return i;
        }
    }
    return -1; // Location not found
}

// Function to perform Dijkstra's algorithm for pathfinding
void dijkstra(Map* map, int start, int end) {
    int distances[MAX_LOCATIONS];
    int visited[MAX_LOCATIONS];

    // Initialize distances and visited array
    for (int i = 0; i < map->numLocations; i++) {
        distances[i] = INT_MAX;
        visited[i] = 0;
    }

    distances[start] = 0;

    for (int count = 0; count < map->numLocations - 1; count++) {
        int minDistance = INT_MAX;
        int minIndex = -1;

        // Find the minimum distance vertex not yet processed
        for (int v = 0; v < map->numLocations; v++) {
            if (!visited[v] && distances[v] < minDistance) {
                minDistance = distances[v];
                minIndex = v;
            }
        }

        // Mark the selected vertex as visited
        visited[minIndex] = 1;

        // Update the distance value of the neighboring vertices
        for (int v = 0; v < map->numLocations; v++) {
            if (!visited[v] && map->adjacencyMatrix[minIndex][v] && distances[minIndex] != INT_MAX &&
                distances[minIndex] + map->adjacencyMatrix[minIndex][v] < distances[v]) {
                distances[v] = distances[minIndex] + map->adjacencyMatrix[minIndex][v];
            }
        }
    }

    // Print the result
    printf("Shortest distance from %s to %s: %d\n", map->locations[start].name, map->locations[end].name, distances[end]);
}

int main() {
    Map navigationMap;
    navigationMap.numLocations = 0;

    // Add locations to the map
    addLocation(&navigationMap, "Location A");
    addLocation(&navigationMap, "Location B");
    addLocation(&navigationMap, "Location C");
    addLocation(&navigationMap, "Location D");

    // Add connections between locations with weights (distances)
    addEdge(&navigationMap, findLocationIndex(&navigationMap, "Location A"), findLocationIndex(&navigationMap, "Location B"), 1);
    addEdge(&navigationMap, findLocationIndex(&navigationMap, "Location B"), findLocationIndex(&navigationMap, "Location C"), 2);
    addEdge(&navigationMap, findLocationIndex(&navigationMap, "Location C"), findLocationIndex(&navigationMap, "Location D"), 3);

    // Perform navigation
    dijkstra(&navigationMap, findLocationIndex(&navigationMap, "Location A"), findLocationIndex(&navigationMap, "Location D"));

    return 0;
}

