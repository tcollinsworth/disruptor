import pytest
import numpy as np
from ctypes import Structure, POINTER, pointer, byref, cast, c_float
import multiprocessing

ITEM_CNT = 3
VECTOR_DIMENSIONS = 2

def p1(np_ptr):
    print(f'w1 np_ptr {np_ptr}')

    a1 = np.ctypeslib.as_array(np_ptr)
    print(f'w1 type(a1) {type(a1)}')
    print(f'w1 a1 {a1}')
    print(a1[2][1])
    a1[2][1] = 2.1
    print(a1[2][1])
    print(f'w1 a1 {a1}')
    
#broken, not the same array in other process

def test_struct():
    a = 2 * np.random.random_sample((ITEM_CNT, VECTOR_DIMENSIONS)) - 1
    print()
    print(f'type(a) {type(a)}')
    print(a)
    print(a.ctypes.data)

    ptr = np.ctypeslib.as_ctypes(a)
    print(f'ptr {ptr}')

    a1 = np.ctypeslib.as_array(ptr)
    print(f'type(a1) {type(a1)}')
    print(f'a1 {a1}')

    w1 = multiprocessing.Process(name='w1', target=p1, args=(ptr,))
    w1.start()
    w1.join()
    print(a1[2][1])
    print(f'a1 {a1}')

#https://pymotw.com/2/multiprocessing/communication.html
#https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.ctypeslib.html
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.ctypes.html
#https://stackoverflow.com/a/53387364
#https://stackoverflow.com/a/3671889
