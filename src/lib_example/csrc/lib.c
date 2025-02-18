#include <stdio.h>
#include <stdlib.h>
#include "lib.h"

const float* get_temprature(int* size) {
    static const float arr[] = {261.59f, 286.23f, 234.3f, 342.4f, 352.5f};
    *size = sizeof(arr) / sizeof(arr[0]);
    return arr;
}

float* get_temprature_by_sensors(char* sensors[], int n) {
    float* arr = malloc(n * sizeof(float)); 
    if (arr == NULL) {
        return NULL;
    }
    for (int i = 0; i < n; i++) {
        arr[i] = i * 11.1f;  
    }
    return arr;
}
