#include <stdlib.h>
#include <stddef.h>
// this is a of ectool function
/*
float cmd_temprature(int argc, char *argv[])
it requires sensor id as argument at [1]
*/
float get_temprature(char *sensor_id){
    return 43.2;
}
float* get_temprature_of_all(int *size){
    int n = 5;
    *size = n;
    float* arr = malloc(n * sizeof(float));
    if (arr == NULL) {
        return NULL;
    }
    for (int i = 0; i < n; i++) {
        arr[i] = get_temprature("s");  
    }
    return arr;
}