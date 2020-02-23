import pytest
import time
import numpy as np
from ctypes import Structure, POINTER, pointer, byref, cast, c_float
import multiprocessing

ITEM_CNT = 3
VECTOR_DIMENSIONS = 2

def p1(np_ptr, name):
    print(f'w1 np_ptr {np_ptr}')

    a1 = np.ctypeslib.as_array(np_ptr)
    print(f'{name} type(a1) {type(a1)}')
    print(f'{name} a1 {a1}')
    print(a1[3][1])
    a1[3][1] = 4.0
    print(a1[3][1])
    
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

    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.resize.html
    ptr = np.resize(ptr, (4,2)) # WARNING - copies existing array data into expanded array rows/columns
    a1 = ptr
    print(f'resized a1 {a1}')

    w1 = multiprocessing.Process(name='w1', target=p1, args=(ptr, 'w1'))
    w1.start()
    # w2 = multiprocessing.Process(name='w1', target=p1, args=(ptr, 'w2'))
    # w2.start()
    # w3 = multiprocessing.Process(name='w1', target=p1, args=(ptr, 'w3'))
    # w3.start()
    # w4 = multiprocessing.Process(name='w1', target=p1, args=(ptr, 'w4'))
    # w4.start()
    # w5 = multiprocessing.Process(name='w1', target=p1, args=(ptr, 'w5'))
    # w5.start()
    # time.sleep(5) # Sleep for 3 seconds
    w1.join()
    # w2.join()
    # w3.join()
    # w4.join()
    # w5.join()

    print(ptr[3][1])


#https://pymotw.com/2/multiprocessing/communication.html
#https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.ctypeslib.html
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.ctypes.html
#https://stackoverflow.com/a/53387364
#https://stackoverflow.com/a/3671889
