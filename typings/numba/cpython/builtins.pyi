"""
This type stub file was generated by pyright.
"""

import operator
from numba.core.imputils import lower_builtin, lower_cast, lower_constant, lower_getattr_generic
from numba.core import types
from numba.core.extending import intrinsic, overload
from numba.core.typing.builtins import IndexValue
from numba.extending import overload, register_jitable

@overload(operator.truth)
def ol_truth(val): # -> Callable[..., Any] | None:
    ...

@lower_builtin(operator.is_not, types.Any, types.Any)
def generic_is_not(context, builder, sig, args):
    """
    Implement `x is not y` as `not (x is y)`.
    """
    ...

@lower_builtin(operator.is_, types.Any, types.Any)
def generic_is(context, builder, sig, args): # -> Constant:
    """
    Default implementation for `x is y`
    """
    ...

@lower_builtin(operator.is_, types.Opaque, types.Opaque)
def opaque_is(context, builder, sig, args): # -> Constant:
    """
    Implementation for `x is y` for Opaque types.
    """
    ...

@lower_builtin(operator.is_, types.Boolean, types.Boolean)
def bool_is_impl(context, builder, sig, args):
    """
    Implementation for `x is y` for types derived from types.Boolean
    (e.g. BooleanLiteral), and cross-checks between literal and non-literal
    booleans, to satisfy Python's behavior preserving identity for bools.
    """
    ...

@lower_builtin(operator.eq, types.Literal, types.Literal)
@lower_builtin(operator.eq, types.IntegerLiteral, types.IntegerLiteral)
def const_eq_impl(context, builder, sig, args): # -> Constant:
    ...

@lower_builtin(operator.ne, types.Literal, types.Literal)
@lower_builtin(operator.ne, types.IntegerLiteral, types.IntegerLiteral)
def const_ne_impl(context, builder, sig, args): # -> Constant:
    ...

def gen_non_eq(val): # -> Callable[..., Callable[..., Any] | None]:
    ...

@lower_getattr_generic(types.DeferredType)
def deferred_getattr(context, builder, typ, value, attr):
    """
    Deferred.__getattr__ => redirect to the actual type.
    """
    ...

@lower_cast(types.Any, types.DeferredType)
@lower_cast(types.Optional, types.DeferredType)
@lower_cast(types.Boolean, types.DeferredType)
def any_to_deferred(context, builder, fromty, toty, val):
    ...

@lower_cast(types.DeferredType, types.Any)
@lower_cast(types.DeferredType, types.Boolean)
@lower_cast(types.DeferredType, types.Optional)
def deferred_to_any(context, builder, fromty, toty, val):
    ...

@lower_builtin(operator.getitem, types.CPointer, types.Integer)
def getitem_cpointer(context, builder, sig, args):
    ...

@lower_builtin(operator.setitem, types.CPointer, types.Integer, types.Any)
def setitem_cpointer(context, builder, sig, args): # -> None:
    ...

def do_minmax(context, builder, argtys, args, cmpop):
    ...

@lower_builtin(max, types.BaseTuple)
def max_iterable(context, builder, sig, args):
    ...

@lower_builtin(max, types.VarArg(types.Any))
def max_vararg(context, builder, sig, args):
    ...

@lower_builtin(min, types.BaseTuple)
def min_iterable(context, builder, sig, args):
    ...

@lower_builtin(min, types.VarArg(types.Any))
def min_vararg(context, builder, sig, args):
    ...

@lower_builtin(round, types.Float)
def round_impl_unary(context, builder, sig, args):
    ...

@lower_builtin(round, types.Float, types.Integer)
def round_impl_binary(context, builder, sig, args):
    ...

@lower_builtin(int, types.Any)
@lower_builtin(float, types.Any)
def int_impl(context, builder, sig, args):
    ...

@lower_builtin(complex, types.VarArg(types.Any))
def complex_impl(context, builder, sig, args):
    ...

@lower_builtin(types.NumberClass, types.Any)
def number_constructor(context, builder, sig, args):
    """
    Call a number class, e.g. np.int32(...)
    """
    ...

@lower_constant(types.Dummy)
def constant_dummy(context, builder, ty, pyval):
    ...

@lower_constant(types.ExternalFunctionPointer)
def constant_function_pointer(context, builder, ty, pyval):
    ...

@lower_constant(types.Optional)
def constant_optional(context, builder, ty, pyval):
    ...

@lower_builtin(type, types.Any)
def type_impl(context, builder, sig, args):
    """
    One-argument type() builtin.
    """
    ...

@lower_builtin(iter, types.IterableType)
def iter_impl(context, builder, sig, args):
    ...

@lower_builtin(next, types.IteratorType)
def next_impl(context, builder, sig, args):
    ...

@lower_builtin("not in", types.Any, types.Any)
def not_in(context, builder, sig, args):
    ...

@lower_builtin(len, types.ConstSized)
def constsized_len(context, builder, sig, args):
    ...

@lower_builtin(bool, types.Sized)
def sized_bool(context, builder, sig, args): # -> Constant:
    ...

@lower_builtin(tuple)
def lower_empty_tuple(context, builder, sig, args):
    ...

@lower_builtin(tuple, types.BaseTuple)
def lower_tuple(context, builder, sig, args):
    ...

@overload(bool)
def bool_sequence(x): # -> Callable[..., bool] | None:
    ...

@overload(bool, inline='always')
def bool_none(x): # -> Callable[..., Literal[False]] | None:
    ...

def get_type_max_value(typ): # -> float | int:
    ...

def get_type_min_value(typ): # -> float | int:
    ...

@lower_builtin(get_type_min_value, types.NumberClass)
@lower_builtin(get_type_min_value, types.DType)
def lower_get_type_min_value(context, builder, sig, args): # -> Constant:
    ...

@lower_builtin(get_type_max_value, types.NumberClass)
@lower_builtin(get_type_max_value, types.DType)
def lower_get_type_max_value(context, builder, sig, args): # -> Constant:
    ...

@lower_builtin(IndexValue, types.intp, types.Type)
@lower_builtin(IndexValue, types.uintp, types.Type)
def impl_index_value(context, builder, sig, args): # -> Any:
    ...

@overload(min)
def indval_min(indval1, indval2): # -> Callable[..., Any] | None:
    ...

@overload(min)
def boolval_min(val1, val2): # -> Callable[..., Any] | None:
    ...

@overload(max)
def indval_max(indval1, indval2): # -> Callable[..., Any] | None:
    ...

@overload(max)
def boolval_max(val1, val2): # -> Callable[..., Any] | None:
    ...

greater_than = ...
less_than = ...
@register_jitable
def min_max_impl(iterable, op): # -> Callable[..., Any] | None:
    ...

@overload(min)
def iterable_min(iterable): # -> Callable[..., Any] | None:
    ...

@overload(max)
def iterable_max(iterable): # -> Callable[..., Any] | None:
    ...

@lower_builtin(types.TypeRef, types.VarArg(types.Any))
def redirect_type_ctor(context, builder, sig, args):
    """Redirect constructor implementation to `numba_typeref_ctor(cls, *args)`,
    which should be overloaded by the type's implementation.

    For example:

        d = Dict()

    `d` will be typed as `TypeRef[DictType]()`.  Thus, it will call into this
    implementation.  We need to redirect the lowering to a function
    named ``numba_typeref_ctor``.
    """
    ...

@overload(sum)
def ol_sum(iterable, start=...): # -> Callable[..., int | Any] | None:
    ...

@overload(map)
def ol_map(func, iterable, *args): # -> Callable[..., Generator[Any, Any, None]]:
    ...

@overload(filter)
def ol_filter(func, iterable): # -> Callable[..., Generator[Any, Any, None]]:
    ...

@overload(isinstance)
def ol_isinstance(var, typs): # -> Callable[..., Literal[True]]:
    ...

@overload(_getattr_raise_attr_exc)
def ol__getattr_raise_attr_exc(obj, name): # -> Callable[..., NoReturn]:
    ...

@intrinsic
def resolve_getattr(tyctx, obj, name, default): # -> tuple[Any | Signature, Callable[..., Any]]:
    ...

_getattr_default_type = ...
_getattr_default = ...
@overload(getattr, prefer_literal=True)
def ol_getattr_2(obj, name): # -> Callable[..., Any]:
    ...

@overload(getattr)
def ol_getattr_3(obj, name, default): # -> Callable[..., Any]:
    ...

@intrinsic
def resolve_hasattr(tyctx, obj, name): # -> tuple[Any | Signature, Callable[..., Constant | Any]]:
    ...

@overload(hasattr)
def ol_hasattr(obj, name): # -> Callable[..., Any]:
    ...

@overload(repr)
def ol_repr_generic(obj): # -> Callable[..., Any | str]:
    ...

@overload(str)
def ol_str_generic(object=...): # -> Callable[..., Any | str]:
    ...

