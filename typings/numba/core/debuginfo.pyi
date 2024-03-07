"""
This type stub file was generated by pyright.
"""

import abc
from contextlib import contextmanager

"""
Implements helpers to build LLVM debuginfo.
"""
@contextmanager
def suspend_emission(builder): # -> Generator[None, Any, None]:
    """Suspends the emission of debug_metadata for the duration of the context
    managed block."""
    ...

class AbstractDIBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def mark_variable(self, builder, allocavalue, name, lltype, size, line, datamodel=..., argidx=...): # -> None:
        """Emit debug info for the variable.
        """
        ...
    
    @abc.abstractmethod
    def mark_location(self, builder, line): # -> None:
        """Emit source location information to the given IRBuilder.
        """
        ...
    
    @abc.abstractmethod
    def mark_subprogram(self, function, qualname, argnames, argtypes, line): # -> None:
        """Emit source location information for the given function.
        """
        ...
    
    @abc.abstractmethod
    def initialize(self): # -> None:
        """Initialize the debug info. An opportunity for the debuginfo to
        prepare any necessary data structures.
        """
        ...
    
    @abc.abstractmethod
    def finalize(self): # -> None:
        """Finalize the debuginfo by emitting all necessary metadata.
        """
        ...
    


class DummyDIBuilder(AbstractDIBuilder):
    def __init__(self, module, filepath, cgctx, directives_only) -> None:
        ...
    
    def mark_variable(self, builder, allocavalue, name, lltype, size, line, datamodel=..., argidx=...): # -> None:
        ...
    
    def mark_location(self, builder, line): # -> None:
        ...
    
    def mark_subprogram(self, function, qualname, argnames, argtypes, line): # -> None:
        ...
    
    def initialize(self): # -> None:
        ...
    
    def finalize(self): # -> None:
        ...
    


_BYTE_SIZE = ...
class DIBuilder(AbstractDIBuilder):
    DWARF_VERSION = ...
    DEBUG_INFO_VERSION = ...
    DBG_CU_NAME = ...
    _DEBUG = ...
    def __init__(self, module, filepath, cgctx, directives_only) -> None:
        ...
    
    def initialize(self): # -> None:
        ...
    
    def mark_variable(self, builder, allocavalue, name, lltype, size, line, datamodel=..., argidx=...):
        ...
    
    def mark_location(self, builder, line): # -> None:
        ...
    
    def mark_subprogram(self, function, qualname, argnames, argtypes, line): # -> None:
        ...
    
    def finalize(self): # -> None:
        ...
    


