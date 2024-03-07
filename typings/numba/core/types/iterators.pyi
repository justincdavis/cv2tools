"""
This type stub file was generated by pyright.
"""

from .common import SimpleIterableType, SimpleIteratorType

class RangeType(SimpleIterableType):
    def __init__(self, dtype) -> None:
        ...
    
    def unify(self, typingctx, other): # -> RangeType | None:
        ...
    


class RangeIteratorType(SimpleIteratorType):
    def __init__(self, dtype) -> None:
        ...
    
    def unify(self, typingctx, other): # -> RangeIteratorType | None:
        ...
    


class Generator(SimpleIteratorType):
    """
    Type class for Numba-compiled generator objects.
    """
    def __init__(self, gen_func, yield_type, arg_types, state_types, has_finalizer) -> None:
        ...
    
    @property
    def key(self): # -> tuple[Any, tuple[Any, ...], Any, Any, tuple[Any, ...]]:
        ...
    


class EnumerateType(SimpleIteratorType):
    """
    Type class for `enumerate` objects.
    Type instances are parametered with the underlying source type.
    """
    def __init__(self, iterable_type) -> None:
        ...
    
    @property
    def key(self):
        ...
    


class ZipType(SimpleIteratorType):
    """
    Type class for `zip` objects.
    Type instances are parametered with the underlying source types.
    """
    def __init__(self, iterable_types) -> None:
        ...
    
    @property
    def key(self): # -> tuple[Any, ...]:
        ...
    


class ArrayIterator(SimpleIteratorType):
    """
    Type class for iterators of array and buffer objects.
    """
    def __init__(self, array_type) -> None:
        ...
    


