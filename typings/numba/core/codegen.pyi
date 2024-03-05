"""
This type stub file was generated by pyright.
"""

from abc import ABCMeta, abstractmethod

_x86arch = ...
def dump(header, body, lang): # -> None:
    ...

class _CFG:
    """
    Wraps the CFG graph for different display method.

    Instance of the class can be stringified (``__repr__`` is defined) to get
    the graph in DOT format.  The ``.display()`` method plots the graph in
    PDF.  If in IPython notebook, the returned image can be inlined.
    """
    def __init__(self, cres, name, py_func, **kwargs) -> None:
        ...
    
    def pretty_printer(self, filename=..., view=..., render_format=..., highlight=..., interleave=..., strip_ir=..., show_key=..., fontsize=...):
        """
        "Pretty" prints the DOT graph of the CFG.
        For explanation of the parameters see the docstring for
        numba.core.dispatcher::inspect_cfg.
        """
        ...
    
    def display(self, filename=..., format=..., view=...):
        """
        Plot the CFG.  In IPython notebook, the return image object can be
        inlined.

        The *filename* option can be set to a specific path for the rendered
        output to write to.  If *view* option is True, the plot is opened by
        the system default application for the image format (PDF). *format* can
        be any valid format string accepted by graphviz, default is 'pdf'.
        """
        ...
    
    def __repr__(self): # -> str:
        ...
    


class CodeLibrary(metaclass=ABCMeta):
    """
    An interface for bundling LLVM code together and compiling it.
    It is tied to a *codegen* instance (e.g. JITCPUCodegen) that will
    determine how the LLVM code is transformed and linked together.
    """
    _finalized = ...
    _object_caching_enabled = ...
    _disable_inspection = ...
    def __init__(self, codegen: CPUCodegen, name: str) -> None:
        ...
    
    @property
    def has_dynamic_globals(self): # -> bool:
        ...
    
    @property
    def recorded_timings(self): # -> PassTimingsCollection:
        ...
    
    @property
    def codegen(self): # -> CPUCodegen:
        """
        The codegen object owning this library.
        """
        ...
    
    @property
    def name(self): # -> str:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def create_ir_module(self, name): # -> Module:
        """
        Create an LLVM IR module for use by this library.
        """
        ...
    
    @abstractmethod
    def add_linking_library(self, library): # -> None:
        """
        Add a library for linking into this library, without losing
        the original library.
        """
        ...
    
    @abstractmethod
    def add_ir_module(self, ir_module): # -> None:
        """
        Add an LLVM IR module's contents to this library.
        """
        ...
    
    @abstractmethod
    def finalize(self): # -> None:
        """
        Finalize the library.  After this call, nothing can be added anymore.
        Finalization involves various stages of code optimization and
        linking.
        """
        ...
    
    @abstractmethod
    def get_function(self, name): # -> None:
        """
        Return the function named ``name``.
        """
        ...
    
    @abstractmethod
    def get_llvm_str(self): # -> None:
        """
        Get the human-readable form of the LLVM module.
        """
        ...
    
    @abstractmethod
    def get_asm_str(self): # -> None:
        """
        Get the human-readable assembly.
        """
        ...
    
    def enable_object_caching(self): # -> None:
        ...
    


class CPUCodeLibrary(CodeLibrary):
    def __init__(self, codegen, name) -> None:
        ...
    
    def add_linking_library(self, library): # -> None:
        ...
    
    def add_ir_module(self, ir_module): # -> None:
        ...
    
    def add_llvm_module(self, ll_module): # -> None:
        ...
    
    def finalize(self): # -> None:
        ...
    
    def get_defined_functions(self): # -> Generator[ValueRef, Any, None]:
        """
        Get all functions defined in the library.  The library must have
        been finalized.
        """
        ...
    
    def get_function(self, name): # -> ValueRef:
        ...
    
    def get_llvm_str(self): # -> str:
        ...
    
    def get_asm_str(self): # -> str:
        ...
    
    def get_function_cfg(self, name, py_func=..., **kwargs): # -> _CFG:
        """
        Get control-flow graph of the LLVM function
        """
        ...
    
    def get_disasm_cfg(self, mangled_name): # -> DisasmCFG:
        """
        Get the CFG of the disassembly of the ELF object at symbol mangled_name.

        Requires python package: r2pipe
        Requires radare2 binary on $PATH.
        Notebook rendering requires python package: graphviz
        Optionally requires a compiler toolchain (via pycc) to link the ELF to
        get better disassembly results.
        """
        ...
    
    def serialize_using_bitcode(self): # -> tuple[str, Literal['bitcode'], bytes]:
        """
        Serialize this library using its bitcode as the cached representation.
        """
        ...
    
    def serialize_using_object_code(self): # -> tuple[str, Literal['object'], tuple[Any, bytes]]:
        """
        Serialize this library using its object code as the cached
        representation.  We also include its bitcode for further inlining
        with other libraries.
        """
        ...
    


class AOTCodeLibrary(CPUCodeLibrary):
    def emit_native_object(self): # -> bytes:
        """
        Return this library as a native object (a bytestring) -- for example
        ELF under Linux.

        This function implicitly calls .finalize().
        """
        ...
    
    def emit_bitcode(self): # -> bytes:
        """
        Return this library as LLVM bitcode (a bytestring).

        This function implicitly calls .finalize().
        """
        ...
    


class JITCodeLibrary(CPUCodeLibrary):
    def get_pointer_to_function(self, name): # -> Literal[0]:
        """
        Generate native code for function named *name* and return a pointer
        to the start of the function (as an integer).

        This function implicitly calls .finalize().

        Returns
        -------
        pointer : int
            - zero (null) if no symbol of *name* is defined by this code
              library.
            - non-zero if the symbol is defined.
        """
        ...
    


class RuntimeLinker:
    """
    For tracking unresolved symbols generated at runtime due to recursion.
    """
    PREFIX = ...
    def __init__(self) -> None:
        ...
    
    def scan_unresolved_symbols(self, module, engine): # -> None:
        """
        Scan and track all unresolved external symbols in the module and
        allocate memory for it.
        """
        ...
    
    def scan_defined_symbols(self, module): # -> None:
        """
        Scan and track all defined symbols.
        """
        ...
    
    def resolve(self, engine): # -> None:
        """
        Fix unresolved symbols if they are defined.
        """
        ...
    


class JitEngine:
    """Wraps an ExecutionEngine to provide custom symbol tracking.
    Since the symbol tracking is incomplete  (doesn't consider
    loaded code object), we are not putting it in llvmlite.
    """
    def __init__(self, ee) -> None:
        ...
    
    def is_symbol_defined(self, name): # -> bool:
        """Is the symbol defined in this session?
        """
        ...
    
    def add_module(self, module):
        """Override ExecutionEngine.add_module
        to keep info about defined symbols.
        """
        ...
    
    def add_global_mapping(self, gv, addr):
        """Override ExecutionEngine.add_global_mapping
        to keep info about defined symbols.
        """
        ...
    
    set_object_cache = ...
    finalize_object = ...
    get_function_address = ...
    get_global_value_address = ...


class Codegen(metaclass=ABCMeta):
    """
    Base Codegen class. It is expected that subclasses set the class attribute
    ``_library_class``, indicating the CodeLibrary class for the target.

    Subclasses should also initialize:

    ``self._data_layout``: the data layout for the target.
    ``self._target_data``: the binding layer ``TargetData`` for the target.
    """
    @property
    def target_data(self):
        """
        The LLVM "target data" object for this codegen instance.
        """
        ...
    
    def create_library(self, name, **kwargs):
        """
        Create a :class:`CodeLibrary` object for use with this codegen
        instance.
        """
        ...
    
    def unserialize_library(self, serialized):
        ...
    


class CPUCodegen(Codegen):
    def __init__(self, module_name) -> None:
        ...
    
    def magic_tuple(self): # -> tuple[str, str | Any, Any]:
        """
        Return a tuple unambiguously describing the codegen behaviour.
        """
        ...
    
    def insert_unresolved_ref(self, builder, fnty, name):
        ...
    


class AOTCPUCodegen(CPUCodegen):
    """
    A codegen implementation suitable for Ahead-Of-Time compilation
    (e.g. generation of object files).
    """
    _library_class = AOTCodeLibrary
    def __init__(self, module_name, cpu_name=...) -> None:
        ...
    


class JITCPUCodegen(CPUCodegen):
    """
    A codegen implementation suitable for Just-In-Time compilation.
    """
    _library_class = JITCodeLibrary
    def set_env(self, env_name, env): # -> None:
        """Set the environment address.

        Update the GlobalVariable named *env_name* to the address of *env*.
        """
        ...
    


def initialize_llvm(): # -> None:
    """Safe to use multiple times.
    """
    ...

def get_host_cpu_features(): # -> str:
    """Get host CPU features using LLVM.

    The features may be modified due to user setting.
    See numba.config.ENABLE_AVX.
    """
    ...

