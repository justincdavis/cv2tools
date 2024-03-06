"""
This type stub file was generated by pyright.
"""

def declare_atomic_cas_int(lmod, isize): # -> Function:
    ...

def atomic_cmpxchg(builder, lmod, isize, ptr, cmp, val):
    ...

def declare_atomic_add_float32(lmod): # -> Function:
    ...

def declare_atomic_add_float64(lmod): # -> Function:
    ...

def declare_atomic_sub_float32(lmod): # -> Function:
    ...

def declare_atomic_sub_float64(lmod): # -> Function:
    ...

def declare_atomic_inc_int32(lmod): # -> Function:
    ...

def declare_atomic_inc_int64(lmod): # -> Function:
    ...

def declare_atomic_dec_int32(lmod): # -> Function:
    ...

def declare_atomic_dec_int64(lmod): # -> Function:
    ...

def declare_atomic_max_float32(lmod): # -> Function:
    ...

def declare_atomic_max_float64(lmod): # -> Function:
    ...

def declare_atomic_min_float32(lmod): # -> Function:
    ...

def declare_atomic_min_float64(lmod): # -> Function:
    ...

def declare_atomic_nanmax_float32(lmod): # -> Function:
    ...

def declare_atomic_nanmax_float64(lmod): # -> Function:
    ...

def declare_atomic_nanmin_float32(lmod): # -> Function:
    ...

def declare_atomic_nanmin_float64(lmod): # -> Function:
    ...

def declare_cudaCGGetIntrinsicHandle(lmod): # -> Function:
    ...

def declare_cudaCGSynchronize(lmod): # -> Function:
    ...

def declare_string(builder, value):
    ...

def declare_vprint(lmod): # -> Function:
    ...

SREG_MAPPING = ...
def call_sreg(builder, name):
    ...

class SRegBuilder:
    def __init__(self, builder) -> None:
        ...
    
    def tid(self, xyz):
        ...
    
    def ctaid(self, xyz):
        ...
    
    def ntid(self, xyz):
        ...
    
    def nctaid(self, xyz):
        ...
    
    def getdim(self, xyz):
        ...
    


def get_global_id(builder, dim): # -> list[Any]:
    ...
