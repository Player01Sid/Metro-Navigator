#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure to represent a node in the adjacency list
struct Node
{
    char station[50];
    struct Node *next;
};

// Structure to represent the metro map
struct MetroMap
{
    struct Node **graph;
    int numStations;
};

// Function to create a new node
struct Node *createNode(char station[])
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    if (newNode != NULL)
    {
        strcpy(newNode->station, station);
        newNode->next = NULL;
    }
    return newNode;
}

// Function to initialize the metro map
struct MetroMap *initializeMap(int numStations)
{
    struct MetroMap *map = (struct MetroMap *)malloc(sizeof(struct MetroMap));
    if (map != NULL)
    {
        map->numStations = numStations;
        map->graph = (struct Node **)malloc(numStations * sizeof(struct Node *));
        for (int i = 0; i < numStations; i++)
        {
            map->graph[i] = createNode(""); // Initialize with an empty station
        }
    }
    return map;
}

// Function to add a station to the metro map
void addStation(struct MetroMap *map, char station[])
{
    int index = map->numStations++;
    map->graph[index] = createNode(station);
}

// Function to add a connection between two stations
void addConnection(struct MetroMap *map, char station1[], char station2[])
{
    int index1 = -1, index2 = -1;
    for (int i = 0; i < map->numStations; i++)
    {
        if (strcmp(map->graph[i]->station, station1) == 0)
        {
            index1 = i;
        }
        else if (strcmp(map->graph[i]->station, station2) == 0)
        {
            index2 = i;
        }
    }

    if (index1 != -1 && index2 != -1)
    {
        struct Node *newNode1 = createNode(station2);
        newNode1->next = map->graph[index1]->next;
        map->graph[index1]->next = newNode1;

        struct Node *newNode2 = createNode(station1);
        newNode2->next = map->graph[index2]->next;
        map->graph[index2]->next = newNode2;
    }
}

// Function to print the metro map
void printMap(struct MetroMap *map)
{
    for (int i = 0; i < map->numStations; i++)
    {
        struct Node *current = map->graph[i]->next; // Skip the empty station node
        printf("%s: ", map->graph[i]->station);

        // Print adjacent stations
        while (current != NULL)
        {
            printf("%s, ", current->station);
            current = current->next;
        }

        printf("\n");
    }
}

// Function to free the memory allocated for the metro map
void freeMap(struct MetroMap *map)
{
    for (int i = 0; i < map->numStations; i++)
    {
        struct Node *current = map->graph[i];
        while (current != NULL)
        {
            struct Node *temp = current;
            current = current->next;
            free(temp);
        }
    }
    free(map->graph);
    free(map);
}

// Example usage
int main()
{
    struct MetroMap *metroMap = initializeMap(4);

    addStation(metroMap, "Station A");
    addStation(metroMap, "Station B");
    addStation(metroMap, "Station C");
    addStation(metroMap, "Station D");

    addConnection(metroMap, "Station A", "Station B");
    addConnection(metroMap, "Station B", "Station C");
    addConnection(metroMap, "Station C", "Station D");

    printMap(metroMap);

    freeMap(metroMap);

    return 0;
}
