"""
This type stub file was generated by pyright.
"""

from numba.core.extending import intrinsic

"""
Exception handling intrinsics.
"""
@intrinsic
def exception_check(typingctx): # -> tuple[Any | Signature, Callable[..., Any]]:
    """An intrinsic to check if an exception is raised
    """
    ...

@intrinsic
def mark_try_block(typingctx): # -> tuple[Any | Signature, Callable[..., Any]]:
    """An intrinsic to mark the start of a *try* block.
    """
    ...

@intrinsic
def end_try_block(typingctx): # -> tuple[Any | Signature, Callable[..., Any]]:
    """An intrinsic to mark the end of a *try* block.
    """
    ...

@intrinsic
def exception_match(typingctx, exc_value, exc_class): # -> tuple[Any | Signature, Callable[..., Constant | Any]]:
    """Basically do ``isinstance(exc_value, exc_class)`` for exception objects.
    Used in ``except Exception:`` syntax.
    """
    ...

