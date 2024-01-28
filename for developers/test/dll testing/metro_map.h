// metro_map.h

#ifndef METRO_MAP_H
#define METRO_MAP_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define MAX_LINES 5 // Maximum number of lines

struct Node
{
    char station[50];
    int time;                  // Time associated with the station
    int lineColors[MAX_LINES]; // Array to store line colors
    int numLines;              // Number of lines associated with the station
    struct Node *next;
};

struct MetroMap
{
    struct Node **graph;
    int numStations;
};

// Function declarations
#ifdef __cplusplus
extern "C"
{
#endif

    struct MetroMap *initializeMap(int numStations);
    void addStation(struct MetroMap *map, char station[], int time, int lineColor);
    void addConnection(struct MetroMap *map, char station1[], char station2[], int time, int lineColor);
    void printMap(struct MetroMap *map);
    void dijkstra(struct MetroMap *map, char startStation[], char endStation[]);
    void freeMap(struct MetroMap *map);

#ifdef __cplusplus
}
#endif

#endif // METRO_MAP_H
