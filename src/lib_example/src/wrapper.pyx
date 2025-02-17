cdef extern from "../csrc/const_array.h":
    const float* get_constant_array(int* size)
    float* get_dynamic_array(int* size)

def py_get_constant_array():
    cdef int size
    cdef const float* c_arr = get_constant_array(&size)
    py_list = [c_arr[i] for i in range(size)]
    return py_list
