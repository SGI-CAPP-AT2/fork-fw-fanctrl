from libc.stdlib cimport free, malloc
from libc.string cimport strdup
cimport cython

cdef extern from "../csrc/ectool_func.h":
    float get_temprature(char *sensor_id);
    float* get_temprature_of_all(int *size);

def get_temprature(sensors=None):
    list_of_temps = []
    cdef int size = len(sensors) if sensors is not None else 0
    cdef const float* c_arr = <float *>malloc(size * sizeof(float))
    cdef char* sensor_id_c
    cdef float temp
    if sensors is None:
        c_arr = get_temprature_of_all(&size)
        list_of_temps = [c_arr[i] for i in range(size)]
    else:
        for sensor_id_py in sensors:
            sensor_id_c = strdup(sensor_id_py.encode('utf-8'))
            temp = get_temprature(sensor_id_c)
            free(sensor_id_c)
            list_of_temps.append(temp)
    return list_of_temps
