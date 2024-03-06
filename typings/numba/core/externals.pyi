"""
This type stub file was generated by pyright.
"""

"""
Register external C functions necessary for Numba code generation.
"""
def compile_multi3(context):
    """
    Compile the multi3() helper function used by LLVM
    for 128-bit multiplication on 32-bit platforms.
    """
    ...

class _Installer:
    _installed = ...
    def install(self, context): # -> None:
        """
        Install the functions into LLVM.  This only needs to be done once,
        as the mappings are persistent during the process lifetime.
        """
        ...
    


class _ExternalMathFunctions(_Installer):
    """
    Map the math functions from the C runtime library into the LLVM
    execution environment.
    """
    ...


c_math_functions = ...