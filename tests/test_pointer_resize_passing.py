import pytest
from ctypes import Structure, c_float, POINTER, pointer, byref, cast, sizeof, resize, addressof

class Vector(Structure):
    _fields_ = [("d", c_float * 2)]

def customresize(array, new_size):
    resize(array, sizeof(array._type_) * new_size)
    return (array._type_ * new_size).from_address(addressof(array))

@pytest.mark.skip(reason="works, but not the same array in other process")
def test_struct():
    return
    a = (Vector * 2)()
    a[0].d[0] = 0.1234
    a[0].d[1] = 1.0
    a[1].d[0] = 0.234
    a[1].d[1] = 2.0
    assert a[0].d[0] == 0.1234000027179718
    assert a[0].d[1] == 1.0
    assert a[1].d[0] == 0.23399999737739563
    assert a[1].d[1] == 2.0

    ptr = byref(a)

    a1 = cast(ptr, POINTER(Vector*2)).contents
    assert a[0].d[0] == a1[0].d[0]

    VectorType = POINTER(Vector*2)
    a2 = VectorType.from_param(pointer(a)).contents
    assert a[0].d[0] == a2[0].d[0]

    a3 = cast(ptr, VectorType).contents
    assert a[0].d[0] == a3[0].d[0]

    # print(f'sizeof {sizeof(Vector())}') # 8 for 2 c_float dimensions

    # print(f'sizeof {sizeof(a)}') # 16 for array of 2 Vectors each with 2 c_float dimensions
    # resize(a, 24)
    # print(f'sizeof {sizeof(a)}') # 24 for array of 3 Vectors each with 2 c_float dimensions

    a4 = customresize(a, 3)

    a4[2].d[0] = 3.0
    a4[2].d[1] = 4.0

    assert a4[2].d[0] == 3.0
    assert a4[2].d[1] == 4.0

    ptr2 = byref(a)

    a5 = cast(ptr2, POINTER(Vector*3)).contents
    assert a4[0].d[0] == a5[0].d[0]
    assert a4[2].d[1] == a5[2].d[1]