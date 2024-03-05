"""
This type stub file was generated by pyright.
"""

from functools import singledispatch
from numba.core import types

registry = ...
lower = ...
voidptr = ...
@singledispatch
def print_item(ty, context, builder, val):
    """
    Handle printing of a single value of the given Numba type.
    A (format string, [list of arguments]) is returned that will allow
    forming the final printf()-like call.
    """
    ...

@print_item.register(types.Integer)
@print_item.register(types.IntegerLiteral)
def int_print_impl(ty, context, builder, val): # -> tuple[Literal['%llu', '%lld'], list[Any]]:
    ...

@print_item.register(types.Float)
def real_print_impl(ty, context, builder, val): # -> tuple[Literal['%f'], list[Any]]:
    ...

@print_item.register(types.StringLiteral)
def const_print_impl(ty, context, builder, sigval): # -> tuple[Literal['%s'], list[Any]]:
    ...

@lower(print, types.VarArg(types.Any))
def print_varargs(context, builder, sig, args):
    """This function is a generic 'print' wrapper for arbitrary types.
    It dispatches to the appropriate 'print' implementations above
    depending on the detected real types in the signature."""
    ...

