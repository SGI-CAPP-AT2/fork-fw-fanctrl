#include <stdio.h>
#include "lib.h"

const float* get_temprature(int* size) {
    static const float arr[] = {261.59f, 286.23f, 234.3f, 342.4f, 352.5f};
    *size = sizeof(arr) / sizeof(arr[0]);
    return arr;
}
