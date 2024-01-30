#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <stdbool.h>
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
    int connections;
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
        newNode->connections = 0;
        for (int i = 1; i < 5; i++)
        {
            newNode->lineColors[i] = 0;
        }
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

__declspec(dllexport) void addConnection(struct MetroMap *map, char station1[], char station2[])
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
        int color[2];

        color[0] = map->graph[index1]->lineColors[0];
        color[1] = map->graph[index2]->lineColors[0];

        map->graph[index1]->connections = map->graph[index1]->connections + 1;
        map->graph[index2]->connections = map->graph[index2]->connections + 1;

        struct Node *newNode1 = createNode(station2, color[0]);
        newNode1->next = map->graph[index1]->next;
        map->graph[index1]->next = newNode1;

        // Ensure bidirectional connection
        struct Node *newNode2 = createNode(station1, color[1]);
        newNode2->next = map->graph[index2]->next;
        map->graph[index2]->next = newNode2;

        if (color[0] != color[1])
        {
            int *temp1 = map->graph[index1]->lineColors;
            int *temp2 = map->graph[index2]->lineColors;
            int idx1 = 0; // Start index at 0
            int idx2 = 0; // Start index at 0

            // Find the end of the lineColors array for station 1
            while (temp1[idx1] != 0 && idx1 < MAX_LINES)
            {
                idx1++;
            }

            // Find the end of the lineColors array for station 2
            while (temp2[idx2] != 0 && idx2 < MAX_LINES)
            {
                idx2++;
            }

            // Add the new color to the lineColors array for station 1
            if (idx1 < MAX_LINES && temp1[idx1 - 1] != color[1] && map->graph[index1]->connections > 2)
            {
                temp1[idx1] = color[1];
            }

            if (idx2 < MAX_LINES && temp2[idx2 - 1] != color[0] && map->graph[index2]->connections > 2)
            {
                temp2[idx2] = color[0];
            }
        }
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

__declspec(dllexport) char *dijkstra(struct MetroMap *map, char startStation[], char endStation[])
{
    int numVertices = map->numStations;

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
        char *string = (char *)malloc(100 * sizeof(char));
        string = "Invalid start or end station.\n";
        return string;
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
            break;
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
                int newDistance = distance[minIndex] + 1;
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
        char *string = (char *)malloc(100 * sizeof(char));
        strcpy(string, "No path found from");
        strcat(string, startStation);
        strcat(string, " to ");
        strcat(string, endStation);
        return string;
    }

    int currentVertex = endIndex;
    int path[numVertices];
    int pathLength = 0;

    while (currentVertex != -1)
    {
        path[pathLength++] = currentVertex;
        currentVertex = previous[currentVertex];
    }
    char *string = (char *)malloc(100 * sizeof(char));
    strcpy(string, "Route: ");
    for (int i = pathLength - 1; i >= 0; i--)
    {
        strcat(string, map->graph[path[i]]->station);
        strcat(string, ":");
        if (i != pathLength - 1)
        {
            if (map->graph[path[i]]->lineColors[0] != map->graph[path[i + 1]]->lineColors[0])
            {
                bool ans = false;
                for (int j = 0; j < 5; j++)
                {
                    int a = map->graph[path[i]]->lineColors[j];
                    for (int k = 0; k < 5; k++)
                    {
                        int b = map->graph[path[i + 1]]->lineColors[k];

                        if (a == b)
                        {
                            int temp = a;
                            char color[10];
                            sprintf(color, "%d", temp);
                            strcat(string, color);
                            ans = 1;
                        }
                        if (ans == 1)
                        {
                            break;
                        }
                    }
                    if (ans == 1)
                    {
                        break;
                    }
                }
            }
            else
            {
                int temp = map->graph[path[i]]->lineColors[0];
                char color[10];
                sprintf(color, "%d", temp);
                strcat(string, color);
            }
        }
        else
        {
            int temp = map->graph[path[i]]->lineColors[0];
            char color[10];
            sprintf(color, "%d", temp);
            strcat(string, color);
        }

        if (i > 0)
        {
            strcat(string, " -> ");
        }
    }

    free(distance);
    free(visited);
    free(previous);
    return string;
}

__declspec(dllexport) int *colors(struct MetroMap *map, char targetStation[])
{
    int numVertices = map->numStations;
    for (int i = 0; i < numVertices; i++)
    {
        if (strcmp(map->graph[i]->station, targetStation) == 0)
        {
            return map->graph[i]->lineColors;
        }
    }
}

__declspec(dllexport) int noStations(struct MetroMap *map)
{
    return map->numStations / 2;
}

__declspec(dllexport) struct MetroMap *initiate()
{
    struct MetroMap *metroMap = initializeMap(26);

    addStation(metroMap, "Station A", 1);
    addStation(metroMap, "Station B", 1);
    addStation(metroMap, "Station C", 1);
    addStation(metroMap, "Station D", 1);
    addStation(metroMap, "Station E", 1);
    addStation(metroMap, "Station F", 1);
    addStation(metroMap, "Station G", 1);
    addStation(metroMap, "Station H", 1);
    addStation(metroMap, "Station I", 3);
    addStation(metroMap, "Station J", 3);
    addStation(metroMap, "Station K", 3);
    addStation(metroMap, "Station L", 3);
    addStation(metroMap, "Station M", 3);
    addStation(metroMap, "Station N", 3);
    addStation(metroMap, "Station O", 3);
    addStation(metroMap, "Station P", 4);
    addStation(metroMap, "Station Q", 4);
    addStation(metroMap, "Station R", 4);
    addStation(metroMap, "Station S", 4);
    addStation(metroMap, "Station T", 4);
    addStation(metroMap, "Station U", 4);
    addStation(metroMap, "Station V", 2);
    addStation(metroMap, "Station W", 2);
    addStation(metroMap, "Station X", 2);
    addStation(metroMap, "Station Y", 2);
    addStation(metroMap, "Station Z", 2);

    addConnection(metroMap, "Station A", "Station B");
    addConnection(metroMap, "Station B", "Station C");
    addConnection(metroMap, "Station C", "Station D");
    addConnection(metroMap, "Station D", "Station E");
    addConnection(metroMap, "Station E", "Station F");
    addConnection(metroMap, "Station F", "Station G");
    addConnection(metroMap, "Station G", "Station H");
    addConnection(metroMap, "Station I", "Station J");
    addConnection(metroMap, "Station J", "Station E");
    addConnection(metroMap, "Station E", "Station K");
    addConnection(metroMap, "Station K", "Station L");
    addConnection(metroMap, "Station L", "Station M");
    addConnection(metroMap, "Station M", "Station N");
    addConnection(metroMap, "Station N", "Station O");
    addConnection(metroMap, "Station P", "Station Q");
    addConnection(metroMap, "Station Q", "Station R");
    addConnection(metroMap, "Station R", "Station L");
    addConnection(metroMap, "Station L", "Station S");
    addConnection(metroMap, "Station S", "Station T");
    addConnection(metroMap, "Station T", "Station U");
    addConnection(metroMap, "Station V", "Station B");
    addConnection(metroMap, "Station B", "Station W");
    addConnection(metroMap, "Station W", "Station X");
    addConnection(metroMap, "Station X", "Station L");
    addConnection(metroMap, "Station L", "Station Y");
    addConnection(metroMap, "Station Y", "Station Z");

    return metroMap;
}

__declspec(dllexport) int sum(int a, int b)
{
    return a + b;
}