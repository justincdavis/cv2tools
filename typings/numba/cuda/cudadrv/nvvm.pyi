"""
This type stub file was generated by pyright.
"""

from ctypes import c_int, c_void_p

"""
This is a direct translation of nvvm.h
"""
logger = ...
ADDRSPACE_GENERIC = ...
ADDRSPACE_GLOBAL = ...
ADDRSPACE_SHARED = ...
ADDRSPACE_CONSTANT = ...
ADDRSPACE_LOCAL = ...
nvvm_program = c_void_p
nvvm_result = c_int
RESULT_CODE_NAMES = ...
_datalayout_original = ...
_datalayout_i128 = ...
def is_available(): # -> bool:
    """
    Return if libNVVM is available
    """
    ...

_nvvm_lock = ...
class NVVM:
    '''Process-wide singleton.
    '''
    _PROTOTYPES = ...
    __INSTANCE = ...
    def __new__(cls): # -> Self:
        ...
    
    def __init__(self) -> None:
        ...
    
    @property
    def data_layout(self): # -> LiteralString:
        ...
    
    @property
    def supported_ccs(self): # -> tuple[()] | tuple[tuple[Literal[3], Literal[5]] | tuple[Literal[3], Literal[7]] | tuple[Literal[5], Literal[0]] | tuple[Literal[5], Literal[2]] | tuple[Literal[5], Literal[3]] | tuple[Literal[6], Literal[0]] | tuple[Literal[6], Literal[1]] | tuple[Literal[6], Literal[2]] | tuple[Literal[7], Literal[0]] | tuple[Literal[7], Literal[2]] | tuple[Literal[7], Literal[5]] | tuple[Literal[8], Literal[0]] | tuple[Literal[8], Literal[6]] | tuple[Literal[8], Literal[7]] | tuple[Literal[8], Literal[9]] | tuple[Literal[9], Literal[0]], ...]:
        ...
    
    def get_version(self): # -> tuple[int, int]:
        ...
    
    def get_ir_version(self): # -> tuple[int, int, int, int]:
        ...
    
    def check_error(self, error, msg, exit=...): # -> None:
        ...
    


class CompilationUnit:
    def __init__(self) -> None:
        ...
    
    def __del__(self): # -> None:
        ...
    
    def add_module(self, buffer): # -> None:
        """
         Add a module level NVVM IR to a compilation unit.
         - The buffer should contain an NVVM module IR either in the bitcode
           representation (LLVM3.0) or in the text representation.
        """
        ...
    
    def lazy_add_module(self, buffer): # -> None:
        """
        Lazily add an NVVM IR module to a compilation unit.
        The buffer should contain NVVM module IR either in the bitcode
        representation or in the text representation.
        """
        ...
    
    def compile(self, **options): # -> list[Any]:
        """Perform Compilation.

        Compilation options are accepted as keyword arguments, with the
        following considerations:

        - Underscores (`_`) in option names are converted to dashes (`-`), to
          match NVVM's option name format.
        - Options that take a value will be emitted in the form
          "-<name>=<value>".
        - Booleans passed as option values will be converted to integers.
        - Options which take no value (such as `-gen-lto`) should have a value
          of `None` passed in and will be emitted in the form "-<name>".

        For documentation on NVVM compilation options, see the CUDA Toolkit
        Documentation:

        https://docs.nvidia.com/cuda/libnvvm-api/index.html#_CPPv418nvvmCompileProgram11nvvmProgramiPPKc
        """
        ...
    
    def get_log(self): # -> Any | Literal['']:
        ...
    


COMPUTE_CAPABILITIES = ...
CTK_SUPPORTED = ...
def ccs_supported_by_ctk(ctk_version): # -> tuple[tuple[Literal[3], Literal[5]] | tuple[Literal[3], Literal[7]] | tuple[Literal[5], Literal[0]] | tuple[Literal[5], Literal[2]] | tuple[Literal[5], Literal[3]] | tuple[Literal[6], Literal[0]] | tuple[Literal[6], Literal[1]] | tuple[Literal[6], Literal[2]] | tuple[Literal[7], Literal[0]] | tuple[Literal[7], Literal[2]] | tuple[Literal[7], Literal[5]] | tuple[Literal[8], Literal[0]] | tuple[Literal[8], Literal[6]] | tuple[Literal[8], Literal[7]] | tuple[Literal[8], Literal[9]] | tuple[Literal[9], Literal[0]], ...]:
    ...

def get_supported_ccs(): # -> tuple[()] | tuple[tuple[Literal[3], Literal[5]] | tuple[Literal[3], Literal[7]] | tuple[Literal[5], Literal[0]] | tuple[Literal[5], Literal[2]] | tuple[Literal[5], Literal[3]] | tuple[Literal[6], Literal[0]] | tuple[Literal[6], Literal[1]] | tuple[Literal[6], Literal[2]] | tuple[Literal[7], Literal[0]] | tuple[Literal[7], Literal[2]] | tuple[Literal[7], Literal[5]] | tuple[Literal[8], Literal[0]] | tuple[Literal[8], Literal[6]] | tuple[Literal[8], Literal[7]] | tuple[Literal[8], Literal[9]] | tuple[Literal[9], Literal[0]], ...]:
    ...

def find_closest_arch(mycc): # -> tuple[Literal[3], Literal[5]] | tuple[Literal[3], Literal[7]] | tuple[Literal[5], Literal[0]] | tuple[Literal[5], Literal[2]] | tuple[Literal[5], Literal[3]] | tuple[Literal[6], Literal[0]] | tuple[Literal[6], Literal[1]] | tuple[Literal[6], Literal[2]] | tuple[Literal[7], Literal[0]] | tuple[Literal[7], Literal[2]] | tuple[Literal[7], Literal[5]] | tuple[Literal[8], Literal[0]] | tuple[Literal[8], Literal[6]] | tuple[Literal[8], Literal[7]] | tuple[Literal[8], Literal[9]] | tuple[Literal[9], Literal[0]]:
    """
    Given a compute capability, return the closest compute capability supported
    by the CUDA toolkit.

    :param mycc: Compute capability as a tuple ``(MAJOR, MINOR)``
    :return: Closest supported CC as a tuple ``(MAJOR, MINOR)``
    """
    ...

def get_arch_option(major, minor): # -> str:
    """Matches with the closest architecture option
    """
    ...

MISSING_LIBDEVICE_FILE_MSG = ...
class LibDevice:
    _cache_ = ...
    def __init__(self) -> None:
        ...
    
    def get(self): # -> bytes:
        ...
    


cas_nvvm = ...
ir_numba_atomic_binary_template = ...
ir_numba_atomic_inc_template = ...
ir_numba_atomic_dec_template = ...
ir_numba_atomic_minmax_template = ...
def ir_cas(Ti): # -> str:
    ...

def ir_numba_atomic_binary(T, Ti, OP, FUNC): # -> str:
    ...

def ir_numba_atomic_minmax(T, Ti, NAN, OP, PTR_OR_VAL, FUNC): # -> str:
    ...

def ir_numba_atomic_inc(T, Tu): # -> str:
    ...

def ir_numba_atomic_dec(T, Tu): # -> str:
    ...

def llvm_replace(llvmir): # -> LiteralString:
    ...

def llvm_to_ptx(llvmir, **opts): # -> list[Any]:
    ...

re_attributes_def = ...
def llvm140_to_70_ir(ir): # -> LiteralString:
    """
    Convert LLVM 14.0 IR for LLVM 7.0.
    """
    ...

def set_cuda_kernel(function): # -> None:
    """
    Mark a function as a CUDA kernel. Kernels have the following requirements:

    - Metadata that marks them as a kernel.
    - Addition to the @llvm.used list, so that they will not be discarded.
    - The noinline attribute is not permitted, because this causes NVVM to emit
      a warning, which counts as failing IR verification.

    Presently it is assumed that there is one kernel per module, which holds
    for Numba-jitted functions. If this changes in future or this function is
    to be used externally, this function may need modification to add to the
    @llvm.used list rather than creating it.
    """
    ...

def add_ir_version(mod): # -> None:
    """Add NVVM IR version to module"""
    ...

