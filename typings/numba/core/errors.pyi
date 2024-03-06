"""
This type stub file was generated by pyright.
"""

import abc
import contextlib
import os
from abc import abstractmethod

"""
Numba-specific errors and warnings.
"""
__all__ = []
class NumbaWarning(Warning):
    """
    Base category for all Numba compiler warnings.
    """
    def __init__(self, msg, loc=..., highlighting=...) -> None:
        ...
    


class NumbaPerformanceWarning(NumbaWarning):
    """
    Warning category for when an operation might not be
    as fast as expected.
    """
    ...


class NumbaDeprecationWarning(NumbaWarning, DeprecationWarning):
    """
    Warning category for use of a deprecated feature.
    """
    ...


class NumbaPendingDeprecationWarning(NumbaWarning, PendingDeprecationWarning):
    """
    Warning category for use of a feature that is pending deprecation.
    """
    ...


class NumbaParallelSafetyWarning(NumbaWarning):
    """
    Warning category for when an operation in a prange
    might not have parallel semantics.
    """
    ...


class NumbaTypeSafetyWarning(NumbaWarning):
    """
    Warning category for unsafe casting operations.
    """
    ...


class NumbaExperimentalFeatureWarning(NumbaWarning):
    """
    Warning category for using an experimental feature.
    """
    ...


class NumbaInvalidConfigWarning(NumbaWarning):
    """
    Warning category for using an invalid configuration.
    """
    ...


class NumbaPedanticWarning(NumbaWarning):
    """
    Warning category for reporting pedantic messages.
    """
    def __init__(self, msg, **kwargs) -> None:
        ...
    


class NumbaIRAssumptionWarning(NumbaPedanticWarning):
    """
    Warning category for reporting an IR assumption violation.
    """
    ...


class NumbaDebugInfoWarning(NumbaWarning):
    """
    Warning category for an issue with the emission of debug information.
    """
    ...


class NumbaSystemWarning(NumbaWarning):
    """
    Warning category for an issue with the system configuration.
    """
    ...


class _ColorScheme(metaclass=abc.ABCMeta):
    @abstractmethod
    def code(self, msg): # -> None:
        ...
    
    @abstractmethod
    def errmsg(self, msg): # -> None:
        ...
    
    @abstractmethod
    def filename(self, msg): # -> None:
        ...
    
    @abstractmethod
    def indicate(self, msg): # -> None:
        ...
    
    @abstractmethod
    def highlight(self, msg): # -> None:
        ...
    
    @abstractmethod
    def reset(self, msg): # -> None:
        ...
    


class _DummyColorScheme(_ColorScheme):
    def __init__(self, theme=...) -> None:
        ...
    
    def code(self, msg): # -> None:
        ...
    
    def errmsg(self, msg): # -> None:
        ...
    
    def filename(self, msg): # -> None:
        ...
    
    def indicate(self, msg): # -> None:
        ...
    
    def highlight(self, msg): # -> None:
        ...
    
    def reset(self, msg): # -> None:
        ...
    


_termcolor_inst = ...
colorama_version = ...
if tuple([int(x) for x in colorama_version.split('.')]) < (0, 3, 9):
    msg = ...
if os.environ.get('NUMBA_DISABLE_ERROR_MESSAGE_HIGHLIGHTING', None):
    ...
pedantic_warning_info = ...
feedback_details = ...
unsupported_error_info = ...
interpreter_error_info = ...
constant_inference_info = ...
typing_error_info = ...
reportable_issue_info = ...
error_extras = ...
def deprecated(arg): # -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any] | Callable[..., _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]]:
    """Define a deprecation decorator.
    An optional string should refer to the new API to be used instead.

    Example:
      @deprecated
      def old_func(): ...

      @deprecated('new_func')
      def old_func(): ..."""
    ...

class WarningsFixer:
    """
    An object "fixing" warnings of a given category caught during
    certain phases.  The warnings can have their filename and lineno fixed,
    and they are deduplicated as well.

    When used as a context manager, any warnings caught by `.catch_warnings()`
    will be flushed at the exit of the context manager.
    """
    def __init__(self, category) -> None:
        ...
    
    @contextlib.contextmanager
    def catch_warnings(self, filename=..., lineno=...): # -> Generator[None, Any, None]:
        """
        Store warnings and optionally fix their filename and lineno.
        """
        ...
    
    def flush(self): # -> None:
        """
        Emit all stored warnings.
        """
        ...
    
    def __enter__(self): # -> None:
        ...
    
    def __exit__(self, exc_type, exc_value, traceback): # -> None:
        ...
    


class NumbaError(Exception):
    def __init__(self, msg, loc=..., highlighting=...) -> None:
        ...
    
    @property
    def contexts(self): # -> list[Any]:
        ...
    
    def add_context(self, msg): # -> Self:
        """
        Add contextual info.  The exception message is expanded with the new
        contextual information.
        """
        ...
    
    def patch_message(self, new_message): # -> None:
        """
        Change the error message to the given new message.
        """
        ...
    


class UnsupportedError(NumbaError):
    """
    Numba does not have an implementation for this functionality.
    """
    ...


class UnsupportedRewriteError(UnsupportedError):
    """UnsupportedError from rewrite passes
    """
    ...


class IRError(NumbaError):
    """
    An error occurred during Numba IR generation.
    """
    ...


class RedefinedError(IRError):
    """
    An error occurred during interpretation of IR due to variable redefinition.
    """
    ...


class NotDefinedError(IRError):
    """
    An undefined variable is encountered during interpretation of IR.
    """
    def __init__(self, name, loc=...) -> None:
        ...
    


class VerificationError(IRError):
    """
    An error occurred during IR verification. Once Numba's internal
    representation (IR) is constructed it is then verified to ensure that
    terminators are both present and in the correct places within the IR. If
    it is the case that this condition is not met, a VerificationError is
    raised.
    """
    ...


class DeprecationError(NumbaError):
    """
    Functionality is deprecated.
    """
    ...


class LoweringError(NumbaError):
    """
    An error occurred during lowering.
    """
    def __init__(self, msg, loc=...) -> None:
        ...
    


class UnsupportedParforsError(NumbaError):
    """
    An error occurred because parfors is not supported on the platform.
    """
    ...


class ForbiddenConstruct(LoweringError):
    """
    A forbidden Python construct was encountered (e.g. use of locals()).
    """
    ...


class TypingError(NumbaError):
    """
    A type inference failure.
    """
    ...


class UntypedAttributeError(TypingError):
    def __init__(self, value, attr, loc=...) -> None:
        ...
    


class ByteCodeSupportError(NumbaError):
    """
    Failure to extract the bytecode of the user's function.
    """
    def __init__(self, msg, loc=...) -> None:
        ...
    


class CompilerError(NumbaError):
    """
    Some high-level error in the compiler.
    """
    ...


class ConstantInferenceError(NumbaError):
    """
    Failure during constant inference.
    """
    def __init__(self, value, loc=...) -> None:
        ...
    


class InternalError(NumbaError):
    """
    For wrapping internal error occurred within the compiler
    """
    def __init__(self, exception) -> None:
        ...
    


class InternalTargetMismatchError(InternalError):
    """For signalling a target mismatch error occurred internally within the
    compiler.
    """
    def __init__(self, kind, target_hw, hw_clazz) -> None:
        ...
    


class RequireLiteralValue(TypingError):
    """
    For signalling that a function's typing requires a constant value for
    some of its arguments.
    """
    ...


class ForceLiteralArg(NumbaError):
    """A Pseudo-exception to signal the dispatcher to type an argument literally

    Attributes
    ----------
    requested_args : frozenset[int]
        requested positions of the arguments.
    """
    def __init__(self, arg_indices, fold_arguments=..., loc=...) -> None:
        """
        Parameters
        ----------
        arg_indices : Sequence[int]
            requested positions of the arguments.
        fold_arguments: callable
            A function ``(tuple, dict) -> tuple`` that binds and flattens
            the ``args`` and ``kwargs``.
        loc : numba.ir.Loc or None
        """
        ...
    
    def bind_fold_arguments(self, fold_arguments): # -> ForceLiteralArg:
        """Bind the fold_arguments function
        """
        ...
    
    def combine(self, other): # -> ForceLiteralArg:
        """Returns a new instance by or'ing the requested_args.
        """
        ...
    
    def __or__(self, other): # -> ForceLiteralArg:
        """Same as self.combine(other)
        """
        ...
    


class LiteralTypingError(TypingError):
    """
    Failure in typing a Literal type
    """
    ...


class NumbaValueError(TypingError):
    ...


class NumbaTypeError(TypingError):
    ...


class NumbaAttributeError(TypingError):
    ...


class NumbaAssertionError(TypingError):
    ...


class NumbaNotImplementedError(TypingError):
    ...


class NumbaKeyError(TypingError):
    ...


class NumbaIndexError(TypingError):
    ...


class NumbaRuntimeError(NumbaError):
    ...


_numba_path = ...
loc_info = ...
@contextlib.contextmanager
def new_error_context(fmt_, *args, **kwargs): # -> Generator[None, Any, None]:
    """
    A contextmanager that prepend contextual information to any exception
    raised within.  If the exception type is not an instance of NumbaError,
    it will be wrapped into a InternalError.   The exception class can be
    changed by providing a "errcls_" keyword argument with the exception
    constructor.

    The first argument is a message that describes the context.  It can be a
    format string.  If there are additional arguments, it will be used as
    ``fmt_.format(*args, **kwargs)`` to produce the final message string.
    """
    ...

__all__ += [name for (name, value) in globals().items() if not name.startswith('_') and isinstance(value, type) and issubclass(value, (Exception, Warning))]