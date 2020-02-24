import pytest
import time
import numpy as np
from multiprocessing import shared_memory, Process, current_process

ITEM_CNT = 3
VECTOR_DIMENSIONS = 2

shm = None

#https://docs.python.org/3/library/multiprocessing.shared_memory.html#module-multiprocessing.shared_memory
#https://pymotw.com/2/multiprocessing/basics.html
#https://pymotw.com/2/multiprocessing/communication.html

@pytest.fixture(autouse=True)
def run_around_tests():
    global shm
    # Code that will run before your test, for example:
    # files_before = # ... do something to check the existing files
    # A test function will be run at this point
    yield
    # Code that will run after your test, for example:
    # files_after = # ... do something to check the existing files
    # assert files_before == files_after
    shm.close()
    shm.unlink()

def mutate_np_array(ITEM_CNT, VECTOR_DIMENSIONS):
    p = current_process()
    shm_p = shared_memory.SharedMemory(name='test123')
    print(f'process {p.name}, {shm}')
    print(ITEM_CNT, VECTOR_DIMENSIONS)
    a1 = np.ndarray((ITEM_CNT,VECTOR_DIMENSIONS), dtype=np.float32, buffer=shm_p.buf)
    print(a1)
    a1[0] = [1,2]
    a1[1] = [3,4]
    a1[2] = [5,6]
    print(a1)

def test_share():
    global shm
    # a = 2 * np.random.random_sample((ITEM_CNT, VECTOR_DIMENSIONS)) - 1
    # a = np.array([(0.0,0.1),(1.0,1.1),(2.0,2.1)], dtype=np.float32)
    # print(a.nbytes)
    # print(a)
    # shm = shared_memory.SharedMemory(name='test123', create=True, size=a.nbytes)
    shm = shared_memory.SharedMemory(name='test123', create=True, size=24)
    a = np.ndarray((ITEM_CNT,VECTOR_DIMENSIONS), dtype=np.float32, buffer=shm.buf)
    print(a)
    a[0] = [0.0,0.1]
    a[1] = [1.0,1.1]
    a[2] = [2.0,2.1]
    print(a)

    p1 = Process(name='p1', target=mutate_np_array, args=(ITEM_CNT,VECTOR_DIMENSIONS))
    p1.start()
    # time.sleep(1) # Sleep for n seconds
    p1.join()
    print(a)
