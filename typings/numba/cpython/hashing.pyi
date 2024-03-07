"""
This type stub file was generated by pyright.
"""

from numba.core.extending import overload, overload_method, register_jitable
from numba.core import types
from ctypes import Structure, Union

"""
Hash implementations for Numba types
"""
_py310_or_later = ...
_hash_width = ...
_Py_hash_t = ...
_Py_uhash_t = ...
_PyHASH_INF = ...
_PyHASH_NAN = ...
_PyHASH_MODULUS = ...
_PyHASH_BITS = ...
_PyHASH_MULTIPLIER = ...
_PyHASH_IMAG = ...
_PyLong_SHIFT = ...
_Py_HASH_CUTOFF = ...
_Py_hashfunc_name = ...
@overload(_defer_hash)
def ol_defer_hash(obj, hash_func): # -> Callable[..., Any]:
    ...

@overload(hash)
def hash_overload(obj): # -> Callable[..., Any]:
    ...

@register_jitable
def process_return(val): # -> int | Any:
    ...

@overload_method(types.Integer, '__hash__')
@overload_method(types.Boolean, '__hash__')
def int_hash(val): # -> Callable[..., int | Any]:
    ...

@overload_method(types.Float, '__hash__')
def float_hash(val): # -> Callable[..., int | Any]:
    ...

@overload_method(types.Complex, '__hash__')
def complex_hash(val): # -> Callable[..., int | Any]:
    ...

if _Py_uhash_t.bitwidth // 8 > 4:
    _PyHASH_XXPRIME_1 = ...
    _PyHASH_XXPRIME_2 = ...
    _PyHASH_XXPRIME_5 = ...
else:
    _PyHASH_XXPRIME_1 = ...
    _PyHASH_XXPRIME_2 = ...
    _PyHASH_XXPRIME_5 = ...
@overload_method(types.BaseTuple, '__hash__')
def tuple_hash(val): # -> Callable[..., int | Any]:
    ...

class FNV(Structure):
    _fields_ = ...


class SIPHASH(Structure):
    _fields_ = ...


class DJBX33A(Structure):
    _fields_ = ...


class EXPAT(Structure):
    _fields_ = ...


class _Py_HashSecret_t(Union):
    _fields_ = ...


_hashsecret_entry = ...
_hashsecret = ...
if _Py_hashfunc_name in ('siphash13', 'siphash24', 'fnv'):
    _siphash13 = ...
    _siphash24 = ...
    _siphasher = ...
else:
    msg = ...
@overload_method(types.UnicodeType, '__hash__')
def unicode_hash(val): # -> Callable[..., Any | int]:
    ...

