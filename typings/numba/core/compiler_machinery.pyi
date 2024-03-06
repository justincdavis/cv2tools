"""
This type stub file was generated by pyright.
"""

from abc import ABCMeta, abstractmethod

_termcolor = ...
class SimpleTimer:
    """
    A simple context managed timer
    """
    def __enter__(self): # -> Self:
        ...
    
    def __exit__(self, *exc): # -> None:
        ...
    


class CompilerPass(metaclass=ABCMeta):
    """ The base class for all compiler passes.
    """
    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def name(cls):
        """
        Returns the name of the pass
        """
        ...
    
    @property
    def pass_id(self): # -> None:
        """
        The ID of the pass
        """
        ...
    
    @pass_id.setter
    def pass_id(self, val): # -> None:
        """
        Sets the ID of the pass
        """
        ...
    
    @property
    def analysis(self): # -> None:
        """
        Analysis data for the pass
        """
        ...
    
    @analysis.setter
    def analysis(self, val): # -> None:
        """
        Set the analysis data for the pass
        """
        ...
    
    def run_initialization(self, *args, **kwargs): # -> Literal[False]:
        """
        Runs the initialization sequence for the pass, will run before
        `run_pass`.
        """
        ...
    
    @abstractmethod
    def run_pass(self, *args, **kwargs): # -> None:
        """
        Runs the pass itself. Must return True/False depending on whether
        statement level modification took place.
        """
        ...
    
    def run_finalizer(self, *args, **kwargs): # -> Literal[False]:
        """
        Runs the initialization sequence for the pass, will run before
        `run_pass`.
        """
        ...
    
    def get_analysis_usage(self, AU): # -> None:
        """ Override to set analysis usage
        """
        ...
    
    def get_analysis(self, pass_name):
        """
        Gets the analysis from a given pass
        """
        ...
    


class SSACompliantMixin:
    """ Mixin to indicate a pass is SSA form compliant. Nothing is asserted
    about this condition at present.
    """
    ...


class FunctionPass(CompilerPass):
    """ Base class for function passes
    """
    ...


class AnalysisPass(CompilerPass):
    """ Base class for analysis passes (no modification made to state)
    """
    ...


class LoweringPass(CompilerPass):
    """ Base class for lowering passes
    """
    ...


class AnalysisUsage:
    """This looks and behaves like LLVM's AnalysisUsage because its like that.
    """
    def __init__(self) -> None:
        ...
    
    def get_required_set(self): # -> set[Any]:
        ...
    
    def get_preserved_set(self): # -> set[Any]:
        ...
    
    def add_required(self, pss): # -> None:
        ...
    
    def add_preserved(self, pss): # -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


_DEBUG = ...
def debug_print(*args, **kwargs): # -> None:
    ...

pass_timings = ...
class PassManager:
    """
    The PassManager is a named instance of a particular compilation pipeline
    """
    _ENFORCING = ...
    def __init__(self, pipeline_name) -> None:
        """
        Create a new pipeline with name "pipeline_name"
        """
        ...
    
    def add_pass(self, pss, description=...): # -> None:
        """
        Append a pass to the PassManager's compilation pipeline
        """
        ...
    
    def add_pass_after(self, pass_cls, location): # -> None:
        """
        Add a pass `pass_cls` to the PassManager's compilation pipeline after
        the pass `location`.
        """
        ...
    
    def finalize(self): # -> None:
        """
        Finalize the PassManager, after which no more passes may be added
        without re-finalization.
        """
        ...
    
    @property
    def finalized(self): # -> bool:
        ...
    
    def run(self, state): # -> None:
        """
        Run the defined pipelines on the state.
        """
        ...
    
    def dependency_analysis(self): # -> dict[Any, Any]:
        """
        Computes dependency analysis
        """
        ...
    


pass_info = ...
class PassRegistry:
    """
    Pass registry singleton class.
    """
    _id = ...
    _registry = ...
    def register(self, mutates_CFG, analysis_only): # -> Callable[..., Any]:
        ...
    
    def is_registered(self, clazz): # -> bool:
        ...
    
    def get(self, clazz):
        ...
    
    def find_by_name(self, class_name):
        ...
    
    def dump(self): # -> None:
        ...
    


_pass_registry = ...
register_pass = ...