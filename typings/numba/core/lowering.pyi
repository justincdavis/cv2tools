"""
This type stub file was generated by pyright.
"""

from numba.core import generators

_VarArgItem = ...
class BaseLower:
    """
    Lower IR to LLVM
    """
    def __init__(self, context, library, fndesc, func_ir, metadata=...) -> None:
        ...
    
    @property
    def call_conv(self):
        ...
    
    def init(self): # -> None:
        ...
    
    def init_pyapi(self): # -> None:
        """
        Init the Python API and Environment Manager for the function being
        lowered.
        """
        ...
    
    def pre_lower(self): # -> None:
        """
        Called before lowering all blocks.
        """
        ...
    
    def post_lower(self): # -> None:
        """
        Called after all blocks are lowered
        """
        ...
    
    def pre_block(self, block): # -> None:
        """
        Called before lowering a block.
        """
        ...
    
    def post_block(self, block): # -> None:
        """
        Called after lowering a block.
        """
        ...
    
    def return_dynamic_exception(self, exc_class, exc_args, nb_types, loc=...): # -> None:
        ...
    
    def return_exception(self, exc_class, exc_args=..., loc=...): # -> None:
        """Propagate exception to the caller.
        """
        ...
    
    def set_exception(self, exc_class, exc_args=..., loc=...): # -> None:
        """Set exception state in the current function.
        """
        ...
    
    def emit_environment_object(self): # -> None:
        """Emit a pointer to hold the Environment object.
        """
        ...
    
    def lower(self): # -> None:
        ...
    
    def extract_function_arguments(self):
        ...
    
    def lower_normal_function(self, fndesc): # -> None:
        """
        Lower non-generator *fndesc*.
        """
        ...
    
    def lower_function_body(self): # -> None:
        """
        Lower the current function's body, and return the entry block.
        """
        ...
    
    def lower_block(self, block): # -> None:
        """
        Lower the given block.
        """
        ...
    
    def create_cpython_wrapper(self, release_gil=...): # -> None:
        """
        Create CPython wrapper(s) around this function (or generator).
        """
        ...
    
    def create_cfunc_wrapper(self): # -> None:
        """
        Create C wrapper around this function.
        """
        ...
    
    def setup_function(self, fndesc): # -> None:
        ...
    
    def typeof(self, varname):
        ...
    
    def debug_print(self, msg): # -> None:
        ...
    
    def print_variable(self, msg, varname): # -> None:
        """Helper to emit ``print(msg, varname)`` for debugging.

        Parameters
        ----------
        msg : str
            Literal string to be printed.
        varname : str
            A variable name whose value will be printed.
        """
        ...
    


class Lower(BaseLower):
    GeneratorLower = generators.GeneratorLower
    def init(self): # -> None:
        ...
    
    def pre_block(self, block): # -> None:
        ...
    
    def post_block(self, block): # -> None:
        ...
    
    def lower_inst(self, inst): # -> None:
        ...
    
    def lower_setitem(self, target_var, index_var, value_var, signature):
        ...
    
    def lower_try_dynamic_raise(self, inst): # -> None:
        ...
    
    def lower_dynamic_raise(self, inst): # -> None:
        ...
    
    def lower_static_raise(self, inst): # -> None:
        ...
    
    def lower_static_try_raise(self, inst): # -> None:
        ...
    
    def lower_assign(self, ty, inst):
        ...
    
    def lower_yield(self, retty, inst):
        ...
    
    def lower_binop(self, resty, expr, op):
        ...
    
    def lower_getitem(self, resty, expr, value, index, signature):
        ...
    
    def fold_call_args(self, fnty, signature, pos_args, vararg, kw_args): # -> list[Any] | tuple[Any, ...]:
        ...
    
    def lower_print(self, inst): # -> None:
        """
        Lower a ir.Print()
        """
        ...
    
    def lower_call(self, resty, expr):
        ...
    
    def lower_expr(self, resty, expr):
        ...
    
    def getvar(self, name):
        """
        Get a pointer to the given variable's slot.
        """
        ...
    
    def loadvar(self, name): # -> LoadInstr:
        """
        Load the given variable's value.
        """
        ...
    
    def storevar(self, value, name, argidx=...): # -> None:
        """
        Store the value into the given variable.
        """
        ...
    
    def delvar(self, name): # -> None:
        """
        Delete the given variable.
        """
        ...
    
    def alloca(self, name, type): # -> AllocaInstr:
        ...
    
    def alloca_lltype(self, name, lltype, datamodel=...): # -> AllocaInstr:
        ...
    
    def incref(self, typ, val): # -> None:
        ...
    
    def decref(self, typ, val): # -> None:
        ...
    


