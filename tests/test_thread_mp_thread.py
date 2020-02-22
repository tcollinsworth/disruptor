import pytest
from ctypes import Structure, c_float, POINTER, pointer, byref, cast

class DIMENSION(Structure):
    _fields_ = [("d", c_float * 2)]

class ReqStruct(Structure):
    _fields_ = [("vector", DIMENSION)]

def test_struct():
    r = ReqStruct()
    r.vector.d[0] = 0.1234
    r.vector.d[1] = 0.234
    assert r.vector.d[0] == 0.1234000027179718
    assert r.vector.d[1] == 0.23399999737739563

    ptr = byref(r)

    r1 = cast(ptr, POINTER(ReqStruct)).contents
    assert r.vector.d[0] == r1.vector.d[0]

    ReqStructType = POINTER(ReqStruct)
    r2 = ReqStructType.from_param(pointer(r)).contents
    assert r.vector.d[0] == r2.vector.d[0]

    r3 = cast(ptr, ReqStructType).contents
    assert r.vector.d[0] == r3.vector.d[0]
