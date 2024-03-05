"""
This type stub file was generated by pyright.
"""

from numba.core import types

"""
This file implements print functionality for the CPU.
"""
registry = ...
lower = ...
@lower("print_item", types.Literal)
def print_item_impl(context, builder, sig, args):
    """
    Print a single constant value.
    """
    ...

@lower("print_item", types.Any)
def print_item_impl(context, builder, sig, args):
    """
    Print a single native value by boxing it in a Python object and
    invoking the Python interpreter's print routine.
    """
    ...

@lower(print, types.VarArg(types.Any))
def print_varargs_impl(context, builder, sig, args):
    """
    A entire print() call.
    """
    ...

