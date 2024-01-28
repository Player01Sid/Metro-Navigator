#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define MAX_LINES 5 // Maximum number of lines

__declspec(dllexport) const char *getRouteText(const char *buffer)
{
    return buffer;
}

struct Node
{
    char station[50];
    int time;
    int lineColors[5]; // Array to store line colors
    int numLines;      // Number of lines associated with the station
    struct Node *next;
};

struct MetroMap
{
    struct Node **graph;
    int numStations;
};

struct Node *createNode(char station[], int lineColor)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    if (newNode != NULL)
    {
        strcpy(newNode->station, station);
        newNode->numLines = 1;
        newNode->lineColors[0] = lineColor;
        newNode->next = NULL;
    }
    return newNode;
}
__declspec(dllexport) struct MetroMap *initializeMap(int numStations)
{
    struct MetroMap *map = (struct MetroMap *)malloc(sizeof(struct MetroMap));
    if (map != NULL)
    {
        map->numStations = numStations;
        map->graph = (struct Node **)malloc(numStations * sizeof(struct Node *));
        for (int i = 0; i < numStations; i++)
        {
            map->graph[i] = createNode("", 0); // Initialize with an empty station node
        }
    }
    return map;
}

__declspec(dllexport) void addStation(struct MetroMap *map, char station[], int lineColor)
{
    int index = map->numStations;
    map->graph = (struct Node **)realloc(map->graph, (index + 1) * sizeof(struct Node *));
    if (map->graph != NULL)
    {
        map->graph[index] = createNode(station, lineColor);
        map->numStations++;
    }
    else
    {
        printf("Memory allocation error.\n");
    }
}

__declspec(dllexport) void addConnection(struct MetroMap *map, char station1[], char station2[], int lineColor)
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
        struct Node *newNode1 = createNode(station2, lineColor);
        newNode1->next = map->graph[index1]->next;
        map->graph[index1]->next = newNode1;

        // Ensure bidirectional connection
        struct Node *newNode2 = createNode(station1, lineColor);
        newNode2->next = map->graph[index2]->next;
        map->graph[index2]->next = newNode2;
    }
}

__declspec(dllexport) void printMap(struct MetroMap *map)
{
    for (int i = 0; i < map->numStations; i++)
    {
        struct Node *current = map->graph[i]->next; // Skip the empty station node
        printf("%s (Time: %d, Lines: ", map->graph[i]->station, map->graph[i]->time);

        for (int j = 0; j < map->graph[i]->numLines; j++)
        {
            printf("%d ", map->graph[i]->lineColors[j]);
        }

        printf("): ");

        while (current != NULL)
        {
            printf("%s (Time: %d, Lines: ", current->station, current->time);

            for (int j = 0; j < current->numLines; j++)
            {
                printf("%d ", current->lineColors[j]);
            }

            printf("), ");
            current = current->next;
        }

        printf("\n");
    }
}

__declspec(dllexport) void freeMap(struct MetroMap *map)
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

// Dijkstra's Algorithm to find the shortest route
__declspec(dllexport) void dijkstra(struct MetroMap *map, char startStation[], char endStation[])
{
    int numVertices = map->numStations;
    printf("%s", startStation);
    for (int i = 0; i < numVertices; i++)
    {
        printf("Station Name: %s\n", map->graph[i]->station);
    }

    int *distance = (int *)malloc(numVertices * sizeof(int));
    int *visited = (int *)malloc(numVertices * sizeof(int));
    int *previous = (int *)malloc(numVertices * sizeof(int));

    for (int i = 0; i < numVertices; i++)
    {
        distance[i] = INT_MAX;
        visited[i] = 0;
        previous[i] = -1;
    }

    int startIndex = -1;
    int endIndex = -1;

    for (int i = 0; i < numVertices; i++)
    {
        if (strcmp(map->graph[i]->station, startStation) == 0)
        {
            startIndex = i;
        }
        else if (strcmp(map->graph[i]->station, endStation) == 0)
        {
            endIndex = i;
        }
    }

    if (startIndex == -1 || endIndex == -1)
    {
        printf("Invalid start or end station.\n");
        return;
    }

    distance[startIndex] = 0;

    for (int i = 0; i < numVertices - 1; i++)
    {
        int minDistance = INT_MAX;
        int minIndex = -1;

        for (int j = 0; j < numVertices; j++)
        {
            if (!visited[j] && distance[j] < minDistance)
            {
                minDistance = distance[j];
                minIndex = j;
            }
        }

        if (minIndex == -1)
        {
            break; // No more reachable vertices
        }

        visited[minIndex] = 1;

        struct Node *current = map->graph[minIndex]->next;
        while (current != NULL)
        {
            int neighborIndex = -1;
            for (int k = 0; k < numVertices; k++)
            {
                if (strcmp(map->graph[k]->station, current->station) == 0)
                {
                    neighborIndex = k;
                    break;
                }
            }

            if (neighborIndex != -1 && !visited[neighborIndex])
            {
                int newDistance = distance[minIndex] + 1; // Assuming each connection takes 1 unit of time
                if (newDistance < distance[neighborIndex])
                {
                    distance[neighborIndex] = newDistance;
                    previous[neighborIndex] = minIndex;
                }
            }

            current = current->next;
        }
    }

    if (distance[endIndex] == INT_MAX)
    {
        printf("No path found from %s to %s.\n", startStation, endStation);
        return;
    }

    printf("Shortest route from %s to %s (Time: %d):\n", startStation, endStation, distance[endIndex]);

    // Backtrack to find the path
    int currentVertex = endIndex;
    int path[numVertices];
    int pathLength = 0;

    while (currentVertex != -1)
    {
        path[pathLength++] = currentVertex;
        currentVertex = previous[currentVertex];
    }

    // Print the path in reverse order
    for (int i = pathLength - 1; i >= 0; i--)
    {
        printf("%s", map->graph[path[i]]->station);
        if (i > 0)
        {
            printf(" -> ");
        }
    }

    printf("\n");

    free(distance);
    free(visited);
    free(previous);
}

__declspec(dllexport) struct MetroMap *initiate()
{
    // Initialize the metro map
    struct MetroMap *metroMap = initializeMap(8);

    // Add stations to the metro map
    addStation(metroMap, "Station A", 1); // Line 1
    addStation(metroMap, "Station B", 1); // Line 2
    addStation(metroMap, "Station C", 1); // Line 3
    addStation(metroMap, "Station D", 1); // Line 1
    addStation(metroMap, "Station E", 1); // Line 2
    addStation(metroMap, "Station F", 2); // Line 3
    addStation(metroMap, "Station G", 2); // Line 1
    addStation(metroMap, "Station H", 2); // Line 2
    addStation(metroMap, "Station I", 3); // Line 2
    addStation(metroMap, "Station J", 3); // Line 2
    addStation(metroMap, "Station K", 3); // Line 2

    // Add connections between stations
    addConnection(metroMap, "Station A", "Station B", 1); // Line 1
    addConnection(metroMap, "Station B", "Station C", 1); // Line 2
    addConnection(metroMap, "Station C", "Station D", 1); // Line 3
    addConnection(metroMap, "Station D", "Station E", 1); // Line 1
    addConnection(metroMap, "Station C", "Station F", 1); // Line 2
    addConnection(metroMap, "Station F", "Station G", 1); // Line 3
    addConnection(metroMap, "Station G", "Station H", 1); // Line 1
    addConnection(metroMap, "Station G", "Station I", 1); // Line 2
    addConnection(metroMap, "Station G", "Station I", 1); // Line 2
    addConnection(metroMap, "Station I", "Station J", 1); // Line 2
    addConnection(metroMap, "Station J", "Station k", 1); // Line 2
    addConnection(metroMap, "Station K", "Station D", 1); // Line 2

    return metroMap;
}

__declspec(dllexport) int sum(int a, int b)
{
    return a + b;
}