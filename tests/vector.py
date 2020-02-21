from ctypes import Structure, c_float

# class DIMENSION(Structure):
#     _fields_ = [("d", c_float)]

class ReqStruct(Structure):
    _fields_ = [("vector", c_float * 512)]