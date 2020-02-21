from vector import ReqStruct
import pytest
# from ctypes import byref, cast, POINTER
import ctypes

def test_struct():
    v = ReqStruct()
    # for d in v:
    #     print(d)
    v.vector[0] = 0.1234
    # print(f'*** {v.vector[0]}')
    assert v.vector[0] == 0.1234000027179718

    x = ReqStruct

    x = ctypes.byref(v) # this is correct
    print(f'byref: {x}')

    # v2 = ctypes.cast(x, ctypes.POINTER(ReqStruct))
    ReqStructType = ctypes.POINTER(ReqStruct)
    v2 = ReqStructType.from_param(ctypes.pointer(v)).contents
    v3 = ReqStructType.from_param(x)
    v4 = ctypes.cast(x, ReqStructType).contents
    # v2 = ctypes.POINTER(ReqStruct).from_param(x)
    # print(ctypes.pointer(v))
    print(f'type(v) {type(v)}')
    print(f'type(x) {type(x)}')
    print(f'type(v2) {type(v2)}')
    print(f'type(v3) {type(v3)}')
    print(f'type(v4) {type(v4)}')
    print(f'v {v}')
    print(f'x {x}')
    print(f'v2 {v2.vector[0]}')
    # print(f'v3 {v3.vector[0]}')
    print(f'v4 {v4.vector[0]}')

    assert v.vector[0] == v2.vector[0]
    assert v.vector[0] == v4.vector[0]
