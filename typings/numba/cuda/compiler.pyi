"""
This type stub file was generated by pyright.
"""

from numba.core.typing.templates import ConcreteTemplate
from numba.core.compiler import CompileResult, CompilerBase, Flags
from numba.core.compiler_lock import global_compiler_lock
from numba.core.compiler_machinery import LoweringPass, register_pass

class CUDAFlags(Flags):
    nvvm_options = ...
    compute_capability = ...


class CUDACompileResult(CompileResult):
    @property
    def entry_point(self): # -> int:
        ...
    


def cuda_compile_result(**entries): # -> CUDACompileResult:
    ...

@register_pass(mutates_CFG=True, analysis_only=False)
class CUDABackend(LoweringPass):
    _name = ...
    def __init__(self) -> None:
        ...
    
    def run_pass(self, state): # -> Literal[True]:
        """
        Back-end: Packages lowering output in a compile result
        """
        ...
    


@register_pass(mutates_CFG=False, analysis_only=False)
class CreateLibrary(LoweringPass):
    """
    Create a CUDACodeLibrary for the NativeLowering pass to populate. The
    NativeLowering pass will create a code library if none exists, but we need
    to set it up with nvvm_options from the flags if they are present.
    """
    _name = ...
    def __init__(self) -> None:
        ...
    
    def run_pass(self, state): # -> Literal[True]:
        ...
    


class CUDACompiler(CompilerBase):
    def define_pipelines(self): # -> list[PassManager]:
        ...
    
    def define_cuda_lowering_pipeline(self, state): # -> PassManager:
        ...
    


@global_compiler_lock
def compile_cuda(pyfunc, return_type, args, debug=..., lineinfo=..., inline=..., fastmath=..., nvvm_options=..., cc=...):
    ...

def cabi_wrap_function(context, lib, fndesc, wrapper_function_name, nvvm_options):
    """
    Wrap a Numba ABI function in a C ABI wrapper at the NVVM IR level.

    The C ABI wrapper will have the same name as the source Python function.
    """
    ...

@global_compiler_lock
def compile_ptx(pyfunc, sig, debug=..., lineinfo=..., device=..., fastmath=..., cc=..., opt=..., abi=..., abi_info=...): # -> tuple[Any, Any]:
    """Compile a Python function to PTX for a given set of argument types.

    :param pyfunc: The Python function to compile.
    :param sig: The signature representing the function's input and output
                types.
    :param debug: Whether to include debug info in the generated PTX.
    :type debug: bool
    :param lineinfo: Whether to include a line mapping from the generated PTX
                     to the source code. Usually this is used with optimized
                     code (since debug mode would automatically include this),
                     so we want debug info in the LLVM but only the line
                     mapping in the final PTX.
    :type lineinfo: bool
    :param device: Whether to compile a device function. Defaults to ``False``,
                   to compile global kernel functions.
    :type device: bool
    :param fastmath: Whether to enable fast math flags (ftz=1, prec_sqrt=0,
                     prec_div=, and fma=1)
    :type fastmath: bool
    :param cc: Compute capability to compile for, as a tuple
               ``(MAJOR, MINOR)``. Defaults to ``(5, 0)``.
    :type cc: tuple
    :param opt: Enable optimizations. Defaults to ``True``.
    :type opt: bool
    :param abi: The ABI for a compiled function - either ``"numba"`` or
                ``"c"``. Note that the Numba ABI is not considered stable.
                The C ABI is only supported for device functions at present.
    :type abi: str
    :param abi_info: A dict of ABI-specific options. The ``"c"`` ABI supports
                     one option, ``"abi_name"``, for providing the wrapper
                     function's name. The ``"numba"`` ABI has no options.
    :type abi_info: dict
    :return: (ptx, resty): The PTX code and inferred return type
    :rtype: tuple
    """
    ...

def compile_ptx_for_current_device(pyfunc, sig, debug=..., lineinfo=..., device=..., fastmath=..., opt=..., abi=..., abi_info=...):
    """Compile a Python function to PTX for a given set of argument types for
    the current device's compute capabilility. This calls :func:`compile_ptx`
    with an appropriate ``cc`` value for the current device."""
    ...

def declare_device_function(name, restype, argtypes): # -> ExternFunction:
    ...

def declare_device_function_template(name, restype, argtypes): # -> type[device_function_template]:
    class device_function_template(ConcreteTemplate):
        ...
    
    

class ExternFunction:
    def __init__(self, name, sig) -> None:
        ...
    


