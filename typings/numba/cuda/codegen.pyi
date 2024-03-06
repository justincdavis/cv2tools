"""
This type stub file was generated by pyright.
"""

from numba.core import serialize
from numba.core.codegen import CodeLibrary, Codegen

CUDA_TRIPLE = ...
def run_nvdisasm(cubin, flags): # -> str:
    ...

def disassemble_cubin(cubin): # -> str:
    ...

def disassemble_cubin_for_cfg(cubin): # -> str:
    ...

class CUDACodeLibrary(serialize.ReduceMixin, CodeLibrary):
    """
    The CUDACodeLibrary generates PTX, SASS, cubins for multiple different
    compute capabilities. It also loads cubins to multiple devices (via
    get_cufunc), which may be of different compute capabilities.
    """
    def __init__(self, codegen, name, entry_name=..., max_registers=..., nvvm_options=...) -> None:
        """
        codegen:
            Codegen object.
        name:
            Name of the function in the source.
        entry_name:
            Name of the kernel function in the binary, if this is a global
            kernel and not a device function.
        max_registers:
            The maximum register usage to aim for when linking.
        nvvm_options:
                Dict of options to pass to NVVM.
        """
        ...
    
    @property
    def llvm_strs(self): # -> list[str]:
        ...
    
    def get_llvm_str(self): # -> str:
        ...
    
    def get_asm_str(self, cc=...): # -> str:
        ...
    
    def get_cubin(self, cc=...): # -> bytes:
        ...
    
    def get_cufunc(self): # -> Any:
        ...
    
    def get_linkerinfo(self, cc):
        ...
    
    def get_sass(self, cc=...): # -> str:
        ...
    
    def get_sass_cfg(self, cc=...): # -> str:
        ...
    
    def add_ir_module(self, mod): # -> None:
        ...
    
    def add_linking_library(self, library): # -> None:
        ...
    
    def add_linking_file(self, filepath): # -> None:
        ...
    
    def get_function(self, name):
        ...
    
    @property
    def modules(self): # -> list[Any | None]:
        ...
    
    @property
    def linking_libraries(self): # -> list[Any]:
        ...
    
    def finalize(self): # -> None:
        ...
    


class JITCUDACodegen(Codegen):
    """
    This codegen implementation for CUDA only generates optimized LLVM IR.
    Generation of PTX code is done separately (see numba.cuda.compiler).
    """
    _library_class = CUDACodeLibrary
    def __init__(self, module_name) -> None:
        ...
    
    def magic_tuple(self): # -> tuple[tuple[int, int], Any]:
        """
        Return a tuple unambiguously describing the codegen behaviour.
        """
        ...
    

