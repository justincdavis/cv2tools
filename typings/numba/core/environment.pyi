"""
This type stub file was generated by pyright.
"""

from numba import _dynfunc

class Environment(_dynfunc.Environment):
    """Stores globals and constant pyobjects for runtime.

    It is often needed to convert b/w nopython objects and pyobjects.
    """
    __slots__ = ...
    _memo = ...
    @classmethod
    def from_fndesc(cls, fndesc): # -> Self:
        ...
    
    def can_cache(self): # -> bool:
        ...
    
    def __reduce__(self): # -> tuple[Callable[..., Any | Environment], tuple[Any, Any, Any]]:
        ...
    
    def __del__(self): # -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    


def lookup_environment(env_name): # -> None:
    """Returns the Environment object for the given name;
    or None if not found
    """
    ...

