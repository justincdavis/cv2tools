"""
This type stub file was generated by pyright.
"""

import operator
from numba.core.extending import box, intrinsic, models, overload, overload_method, register_jitable, register_model, unbox
from numba.core.imputils import RefType, iternext_impl, lower_builtin, lower_cast, lower_constant
from numba.core.datamodel import StructModel, register_default
from numba.core import types
from numba.core.utils import PYVERSION

if PYVERSION in ((3, 9), (3, 10), (3, 11)):
    ...
_MAX_UNICODE = ...
_BLOOM_WIDTH = ...
@register_model(types.UnicodeType)
class UnicodeModel(models.StructModel):
    def __init__(self, dmm, fe_type) -> None:
        ...
    


@register_default(types.UnicodeIteratorType)
class UnicodeIteratorModel(StructModel):
    def __init__(self, dmm, fe_type) -> None:
        ...
    


def compile_time_get_string_data(obj): # -> tuple[bytes, int, int, int, int]:
    """Get string data from a python string for use at compile-time to embed
    the string data into the LLVM module.
    """
    ...

def make_string_from_constant(context, builder, typ, literal_string): # -> Any:
    """
    Get string data by `compile_time_get_string_data()` and return a
    unicode_type LLVM value
    """
    ...

@lower_cast(types.StringLiteral, types.unicode_type)
def cast_from_literal(context, builder, fromty, toty, val): # -> Any:
    ...

@lower_constant(types.unicode_type)
def constant_unicode(context, builder, typ, pyval): # -> Any:
    ...

@unbox(types.UnicodeType)
def unbox_unicode_str(typ, obj, c): # -> NativeValue:
    """
    Convert a unicode str object to a native unicode structure.
    """
    ...

@box(types.UnicodeType)
def box_unicode_str(typ, val, c):
    """
    Convert a native unicode structure to a unicode string
    """
    ...

def make_deref_codegen(bitsize): # -> Callable[..., Any]:
    ...

@intrinsic
def deref_uint8(typingctx, data, offset): # -> tuple[Any | Signature, Callable[..., Any]]:
    ...

@intrinsic
def deref_uint16(typingctx, data, offset): # -> tuple[Any | Signature, Callable[..., Any]]:
    ...

@intrinsic
def deref_uint32(typingctx, data, offset): # -> tuple[Any | Signature, Callable[..., Any]]:
    ...

def make_set_codegen(bitsize): # -> Callable[..., Any]:
    ...

@intrinsic
def set_uint8(typingctx, data, idx, ch): # -> tuple[Any | Signature, Callable[..., Any]]:
    ...

@intrinsic
def set_uint16(typingctx, data, idx, ch): # -> tuple[Any | Signature, Callable[..., Any]]:
    ...

@intrinsic
def set_uint32(typingctx, data, idx, ch): # -> tuple[Any | Signature, Callable[..., Any]]:
    ...

if PYVERSION in ((3, 12), ):
    ...
else:
    ...
if PYVERSION in ((3, 12), ):
    ...
else:
    ...
@overload(len)
def unicode_len(s): # -> Callable[..., Any] | None:
    ...

@overload(operator.eq)
def unicode_eq(a, b): # -> Callable[..., bool] | None:
    ...

@overload(operator.ne)
def unicode_ne(a, b): # -> Callable[..., bool] | None:
    ...

@overload(operator.lt)
def unicode_lt(a, b): # -> Callable[..., bool] | None:
    ...

@overload(operator.gt)
def unicode_gt(a, b): # -> Callable[..., bool] | None:
    ...

@overload(operator.le)
def unicode_le(a, b): # -> Callable[..., bool] | None:
    ...

@overload(operator.ge)
def unicode_ge(a, b): # -> Callable[..., bool] | None:
    ...

@overload(operator.contains)
def unicode_contains(a, b): # -> Callable[..., Any] | None:
    ...

def unicode_idx_check_type(ty, name): # -> None:
    """Check object belongs to one of specific types
    ty: type
        Type of the object
    name: str
        Name of the object
    """
    ...

def unicode_sub_check_type(ty, name): # -> None:
    """Check object belongs to unicode type"""
    ...

def generate_finder(find_func): # -> Callable[..., Any | Literal[-1]]:
    """Generate finder either left or right."""
    ...

_find = ...
_rfind = ...
@overload_method(types.UnicodeType, 'find')
def unicode_find(data, substr, start=..., end=...): # -> Callable[..., Any]:
    """Implements str.find()"""
    ...

@overload_method(types.UnicodeType, 'rfind')
def unicode_rfind(data, substr, start=..., end=...): # -> Callable[..., Any]:
    """Implements str.rfind()"""
    ...

@overload_method(types.UnicodeType, 'rindex')
def unicode_rindex(s, sub, start=..., end=...): # -> Callable[..., Any]:
    """Implements str.rindex()"""
    ...

@overload_method(types.UnicodeType, 'index')
def unicode_index(s, sub, start=..., end=...): # -> Callable[..., Any]:
    """Implements str.index()"""
    ...

@overload_method(types.UnicodeType, 'partition')
def unicode_partition(data, sep): # -> Callable[..., tuple[Any, Any, Any] | tuple[Any, str, Any]]:
    """Implements str.partition()"""
    ...

@overload_method(types.UnicodeType, 'count')
def unicode_count(src, sub, start=..., end=...): # -> Callable[..., int]:
    ...

@overload_method(types.UnicodeType, 'rpartition')
def unicode_rpartition(data, sep): # -> Callable[..., tuple[Any, Any, Any] | tuple[Any, str, Any]]:
    """Implements str.rpartition()"""
    ...

@overload_method(types.UnicodeType, 'startswith')
def unicode_startswith(s, prefix, start=..., end=...): # -> Callable[..., bool]:
    ...

@overload_method(types.UnicodeType, 'endswith')
def unicode_endswith(s, substr, start=..., end=...): # -> Callable[..., bool] | None:
    ...

@overload_method(types.UnicodeType, 'expandtabs')
def unicode_expandtabs(data, tabsize=...): # -> Callable[..., Any]:
    """Implements str.expandtabs()"""
    ...

@overload_method(types.UnicodeType, 'split')
def unicode_split(a, sep=..., maxsplit=...): # -> Callable[..., Any] | None:
    ...

def generate_rsplit_whitespace_impl(isspace_func): # -> Callable[..., list[Any]]:
    """Generate whitespace rsplit func based on either ascii or unicode"""
    ...

unicode_rsplit_whitespace_impl = ...
ascii_rsplit_whitespace_impl = ...
@overload_method(types.UnicodeType, 'rsplit')
def unicode_rsplit(data, sep=..., maxsplit=...): # -> Callable[..., Any]:
    """Implements str.unicode_rsplit()"""
    ...

@overload_method(types.UnicodeType, 'center')
def unicode_center(string, width, fillchar=...): # -> Callable[..., Any]:
    ...

def gen_unicode_Xjust(STRING_FIRST): # -> Callable[..., Callable[..., Any]]:
    ...

def generate_splitlines_func(is_line_break_func): # -> Callable[..., list[Any]]:
    """Generate splitlines performer based on ascii or unicode line breaks."""
    ...

_ascii_splitlines = ...
_unicode_splitlines = ...
@overload_method(types.UnicodeType, 'splitlines')
def unicode_splitlines(data, keepends=...): # -> Callable[..., Any]:
    """Implements str.splitlines()"""
    ...

@register_jitable
def join_list(sep, parts): # -> Literal['']:
    ...

@overload_method(types.UnicodeType, 'join')
def unicode_join(sep, parts): # -> Callable[..., Any | Literal['']] | None:
    ...

@overload_method(types.UnicodeType, 'zfill')
def unicode_zfill(string, width): # -> Callable[..., Any]:
    ...

@register_jitable
def unicode_strip_left_bound(string, chars): # -> int:
    ...

@register_jitable
def unicode_strip_right_bound(string, chars): # -> int:
    ...

def unicode_strip_types_check(chars): # -> None:
    ...

@overload_method(types.UnicodeType, 'lstrip')
def unicode_lstrip(string, chars=...): # -> Callable[..., Any]:
    ...

@overload_method(types.UnicodeType, 'rstrip')
def unicode_rstrip(string, chars=...): # -> Callable[..., Any]:
    ...

@overload_method(types.UnicodeType, 'strip')
def unicode_strip(string, chars=...): # -> Callable[..., Any]:
    ...

@register_jitable
def normalize_str_idx(idx, length, is_start=...): # -> Literal[0]:
    """
    Parameters
    ----------
    idx : int or None
        the index
    length : int
        the string length
    is_start : bool; optional with defaults to True
        Is it the *start* or the *stop* of the slice?

    Returns
    -------
    norm_idx : int
        normalized index
    """
    ...

@overload(operator.getitem)
def unicode_getitem(s, idx): # -> Callable[..., Any] | None:
    ...

@overload(operator.add)
@overload(operator.iadd)
def unicode_concat(a, b): # -> Callable[..., Any] | None:
    ...

@overload(operator.mul)
def unicode_repeat(a, b): # -> Callable[..., Any | Literal[''] | None] | None:
    ...

@overload(operator.not_)
def unicode_not(a): # -> Callable[..., bool] | None:
    ...

@overload_method(types.UnicodeType, 'replace')
def unicode_replace(s, old_str, new_str, count=...): # -> Callable[..., Any | LiteralString]:
    ...

def gen_isAlX(ascii_func, unicode_func): # -> Callable[..., Callable[..., Any | bool]]:
    ...

_unicode_is_alnum = ...
_always_false = ...
_ascii_is_upper = ...
_unicode_is_upper = ...
@overload_method(types.UnicodeType, 'isupper')
def unicode_isupper(a): # -> Callable[..., Any]:
    """
    Implements .isupper()
    """
    ...

@overload_method(types.UnicodeType, 'isascii')
def unicode_isascii(data): # -> Callable[..., Any]:
    """Implements UnicodeType.isascii()"""
    ...

@overload_method(types.UnicodeType, 'istitle')
def unicode_istitle(data): # -> Callable[..., bool]:
    """
    Implements UnicodeType.istitle()
    The algorithm is an approximate translation from CPython:
    https://github.com/python/cpython/blob/1d4b6ba19466aba0eb91c4ba01ba509acf18c723/Objects/unicodeobject.c#L11829-L11885 # noqa: E501
    """
    ...

@overload_method(types.UnicodeType, 'islower')
def unicode_islower(data): # -> Callable[..., bool]:
    """
    impl is an approximate translation of:
    https://github.com/python/cpython/blob/201c8f79450628241574fba940e08107178dc3a5/Objects/unicodeobject.c#L11900-L11933    # noqa: E501
    mixed with:
    https://github.com/python/cpython/blob/201c8f79450628241574fba940e08107178dc3a5/Objects/bytes_methods.c#L131-L156    # noqa: E501
    """
    ...

@overload_method(types.UnicodeType, 'isidentifier')
def unicode_isidentifier(data): # -> Callable[..., bool]:
    """Implements UnicodeType.isidentifier()"""
    ...

def gen_isX(_PyUnicode_IS_func, empty_is_false=...): # -> Callable[..., Callable[..., Any | bool]]:
    ...

def case_operation(ascii_func, unicode_func): # -> Callable[..., Any]:
    """Generate common case operation performer."""
    ...

_unicode_upper = ...
_unicode_lower = ...
_ascii_upper = ...
_ascii_lower = ...
@overload_method(types.UnicodeType, 'lower')
def unicode_lower(data): # -> Callable[..., Any]:
    """Implements .lower()"""
    ...

@overload_method(types.UnicodeType, 'upper')
def unicode_upper(data): # -> Callable[..., Any]:
    """Implements .upper()"""
    ...

@overload_method(types.UnicodeType, 'casefold')
def unicode_casefold(data): # -> Callable[..., Any]:
    """Implements str.casefold()"""
    ...

@overload_method(types.UnicodeType, 'capitalize')
def unicode_capitalize(data): # -> Callable[..., Any]:
    ...

@overload_method(types.UnicodeType, 'title')
def unicode_title(data): # -> Callable[..., Any]:
    """Implements str.title()"""
    ...

@overload_method(types.UnicodeType, 'swapcase')
def unicode_swapcase(data): # -> Callable[..., Any]:
    ...

@overload(ord)
def ol_ord(c): # -> Callable[..., Any | Literal[0]] | None:
    ...

_out_of_range_msg = ...
@overload(chr)
def ol_chr(i): # -> Callable[..., Any] | None:
    ...

@overload_method(types.UnicodeType, "__str__")
def unicode_str(s): # -> Callable[..., Any]:
    ...

@overload_method(types.UnicodeType, "__repr__")
def unicode_repr(s): # -> Callable[..., Any]:
    ...

@overload_method(types.Integer, "__str__")
def integer_str(n): # -> Callable[..., Any | Literal['0']]:
    ...

@overload_method(types.Integer, "__repr__")
def integer_repr(n): # -> Callable[..., Any]:
    ...

@overload_method(types.Boolean, "__repr__")
@overload_method(types.Boolean, "__str__")
def boolean_str(b): # -> Callable[..., Literal['True', 'False']]:
    ...

@lower_builtin('getiter', types.UnicodeType)
def getiter_unicode(context, builder, sig, args):
    ...

@lower_builtin('iternext', types.UnicodeIteratorType)
@iternext_impl(RefType.NEW)
def iternext_unicode(context, builder, sig, args, result): # -> None:
    ...

