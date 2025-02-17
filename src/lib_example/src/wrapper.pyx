cdef extern from "../csrc/lib.h":
    const float* get_temprature(int* size)

def get_temprature_py():
    cdef int size
    cdef const float* c_arr = get_temprature(&size)
    py_list = [c_arr[i] for i in range(size)]
    return py_list
