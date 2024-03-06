"""
This type stub file was generated by pyright.
"""

from numba.core.descriptors import TargetDescriptor
from numba.core import cpu, dispatcher, utils

class CPUTarget(TargetDescriptor):
    options = cpu.CPUTargetOptions
    @property
    def target_context(self): # -> threadsafe_cached_property:
        """
        The target context for CPU targets.
        """
        ...
    
    @property
    def typing_context(self): # -> threadsafe_cached_property:
        """
        The typing context for CPU targets.
        """
        ...
    


cpu_target = ...
class CPUDispatcher(dispatcher.Dispatcher):
    targetdescr = ...


class DelayedRegistry(utils.UniqueDict):
    """
    A unique dictionary but with deferred initialisation of the values.

    Attributes
    ----------
    ondemand:

        A dictionary of key -> value, where value is executed
        the first time it is is used.  It is used for part of a deferred
        initialization strategy.
    """
    def __init__(self, *args, **kws) -> None:
        ...
    
    def __getitem__(self, item):
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    

