"""
This type stub file was generated by pyright.
"""

import abc
from contextlib import contextmanager
from numba.core.compiler_machinery import AnalysisPass, FunctionPass, LoweringPass, register_pass

_TypingResults = ...
@contextmanager
def fallback_context(state, msg): # -> Generator[None, Any, None]:
    """
    Wraps code that would signal a fallback to object mode
    """
    ...

def type_inference_stage(typingctx, targetctx, interp, args, return_type, locals=..., raise_errors=...): # -> _TypingResults:
    ...

class BaseTypeInference(FunctionPass):
    _raise_errors = ...
    def __init__(self) -> None:
        ...
    
    def run_pass(self, state): # -> Literal[True]:
        """
        Type inference and legalization
        """
        ...
    


@register_pass(mutates_CFG=True, analysis_only=False)
class NopythonTypeInference(BaseTypeInference):
    _name = ...


@register_pass(mutates_CFG=True, analysis_only=False)
class PartialTypeInference(BaseTypeInference):
    _name = ...
    _raise_errors = ...


@register_pass(mutates_CFG=False, analysis_only=False)
class AnnotateTypes(AnalysisPass):
    _name = ...
    def __init__(self) -> None:
        ...
    
    def get_analysis_usage(self, AU): # -> None:
        ...
    
    def run_pass(self, state): # -> Literal[False]:
        """
        Create type annotation after type inference
        """
        ...
    


@register_pass(mutates_CFG=True, analysis_only=False)
class NopythonRewrites(FunctionPass):
    _name = ...
    def __init__(self) -> None:
        ...
    
    def run_pass(self, state): # -> Literal[True]:
        """
        Perform any intermediate representation rewrites after type
        inference.
        """
        ...
    


@register_pass(mutates_CFG=True, analysis_only=False)
class PreParforPass(FunctionPass):
    _name = ...
    def __init__(self) -> None:
        ...
    
    def run_pass(self, state): # -> Literal[True]:
        """
        Preprocessing for data-parallel computations.
        """
        ...
    


@register_pass(mutates_CFG=True, analysis_only=False)
class ParforPass(FunctionPass):
    _name = ...
    def __init__(self) -> None:
        ...
    
    def run_pass(self, state): # -> Literal[True]:
        """
        Convert data-parallel computations into Parfor nodes
        """
        ...
    


@register_pass(mutates_CFG=True, analysis_only=False)
class ParforFusionPass(FunctionPass):
    _name = ...
    def __init__(self) -> None:
        ...
    
    def run_pass(self, state): # -> Literal[True]:
        """
        Do fusion of parfor nodes.
        """
        ...
    


@register_pass(mutates_CFG=True, analysis_only=False)
class ParforPreLoweringPass(FunctionPass):
    _name = ...
    def __init__(self) -> None:
        ...
    
    def run_pass(self, state): # -> Literal[True]:
        """
        Prepare parfors for lowering.
        """
        ...
    


@register_pass(mutates_CFG=False, analysis_only=True)
class DumpParforDiagnostics(AnalysisPass):
    _name = ...
    def __init__(self) -> None:
        ...
    
    def run_pass(self, state): # -> Literal[True]:
        ...
    


class BaseNativeLowering(abc.ABC, LoweringPass):
    """The base class for a lowering pass. The lowering functionality must be
    specified in inheriting classes by providing an appropriate lowering class
    implementation in the overridden `lowering_class` property."""
    _name = ...
    def __init__(self) -> None:
        ...
    
    @property
    @abc.abstractmethod
    def lowering_class(self): # -> None:
        """Returns the class that performs the lowering of the IR describing the
        function that is the target of the current compilation."""
        ...
    
    def run_pass(self, state): # -> Literal[True]:
        ...
    


@register_pass(mutates_CFG=True, analysis_only=False)
class NativeLowering(BaseNativeLowering):
    """Lowering pass for a native function IR described solely in terms of
     Numba's standard `numba.core.ir` nodes."""
    _name = ...
    @property
    def lowering_class(self): # -> type[Lower]:
        ...
    


@register_pass(mutates_CFG=True, analysis_only=False)
class NativeParforLowering(BaseNativeLowering):
    """Lowering pass for a native function IR described using Numba's standard
    `numba.core.ir` nodes and also parfor.Parfor nodes."""
    _name = ...
    @property
    def lowering_class(self): # -> type[ParforLower]:
        ...
    


@register_pass(mutates_CFG=False, analysis_only=True)
class NoPythonSupportedFeatureValidation(AnalysisPass):
    """NoPython Mode check: Validates the IR to ensure that features in use are
    in a form that is supported"""
    _name = ...
    def __init__(self) -> None:
        ...
    
    def run_pass(self, state): # -> Literal[False]:
        ...
    


@register_pass(mutates_CFG=False, analysis_only=True)
class IRLegalization(AnalysisPass):
    _name = ...
    def __init__(self) -> None:
        ...
    
    def run_pass(self, state): # -> Literal[True]:
        ...
    


@register_pass(mutates_CFG=True, analysis_only=False)
class NoPythonBackend(LoweringPass):
    _name = ...
    def __init__(self) -> None:
        ...
    
    def run_pass(self, state): # -> Literal[True]:
        """
        Back-end: Generate LLVM IR from Numba IR, compile to machine code
        """
        ...
    


@register_pass(mutates_CFG=True, analysis_only=False)
class InlineOverloads(FunctionPass):
    """
    This pass will inline a function wrapped by the numba.extending.overload
    decorator directly into the site of its call depending on the value set in
    the 'inline' kwarg to the decorator.

    This is a typed pass. CFG simplification and DCE are performed on
    completion.
    """
    _name = ...
    def __init__(self) -> None:
        ...
    
    _DEBUG = ...
    def run_pass(self, state): # -> Literal[True]:
        """Run inlining of overloads
        """
        ...
    


@register_pass(mutates_CFG=False, analysis_only=False)
class DeadCodeElimination(FunctionPass):
    """
    Does dead code elimination
    """
    _name = ...
    def __init__(self) -> None:
        ...
    
    def run_pass(self, state): # -> Literal[True]:
        ...
    


@register_pass(mutates_CFG=False, analysis_only=False)
class PreLowerStripPhis(FunctionPass):
    """Remove phi nodes (ir.Expr.phi) introduced by SSA.

    This is needed before Lowering because the phi nodes in Numba IR do not
    match the semantics of phi nodes in LLVM IR. In Numba IR, phi nodes may
    expand into multiple LLVM instructions.
    """
    _name = ...
    def __init__(self) -> None:
        ...
    
    def run_pass(self, state): # -> Literal[True]:
        ...
    

