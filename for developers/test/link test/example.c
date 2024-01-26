#include <stdio.h>

// Example function in C
__declspec(dllexport) int add_numbers(int a, int b)
{
    return a + b;
}
