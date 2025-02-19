from libc.stdlib cimport free
from libc.string cimport strdup
cimport cython

cdef extern from "../csrc/lib.h":
    float* get_temprature(int* size)
    float* get_temprature_by_sensors(char* sensors[], int n)

cdef extern from "stdlib.h":
    void* malloc(size_t size)
    void free(void* ptr)

@cython.boundscheck(False)
@cython.wraparound(False)
def get_temperature_by_sensors_py(list sensor_names):
    cdef int n = len(sensor_names)
    cdef char** c_sensors = <char**>malloc(n * sizeof(char*))
    cdef float* c_temps
    cdef list temperatures = []

    if not c_sensors:
        return temperatures
        
    try:
        for i in range(n):
            c_sensors[i] = strdup(sensor_names[i].encode('utf-8'))

        c_temps = get_temprature_by_sensors(c_sensors, n)

        if c_temps:
            temperatures = [c_temps[i] for i in range(n)]
            free(c_temps)  
    finally:
        for i in range(n):
            free(c_sensors[i])  
        free(c_sensors)

    return temperatures


def get_temprature_py():
    cdef int size
    cdef const float* c_arr = get_temprature(&size)
    py_list = [c_arr[i] for i in range(size)]
    return py_list
