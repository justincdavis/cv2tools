"""
This type stub file was generated by pyright.
"""

import contextlib
import numpy as np
import operator
from numba.core.extending import overload, register_jitable

"""
Implementation of linear algebra operations.
"""
ll_char = ...
ll_char_p = ...
ll_void_p = ...
ll_intc = ...
ll_intc_p = ...
intp_t = ...
ll_intp_p = ...
F_INT_nptype = np.int32
F_INT_nbtype = ...
_blas_kinds = ...
def get_blas_kind(dtype, func_name=...): # -> str:
    ...

def ensure_blas(): # -> None:
    ...

def ensure_lapack(): # -> None:
    ...

def make_constant_slot(context, builder, ty, val):
    ...

class _BLAS:
    """
    Functions to return type signatures for wrapped
    BLAS functions.
    """
    def __init__(self) -> None:
        ...
    
    @classmethod
    def numba_xxnrm2(cls, dtype): # -> ExternalFunction:
        ...
    
    @classmethod
    def numba_xxgemm(cls, dtype): # -> ExternalFunction:
        ...
    


class _LAPACK:
    """
    Functions to return type signatures for wrapped
    LAPACK functions.
    """
    def __init__(self) -> None:
        ...
    
    @classmethod
    def numba_xxgetrf(cls, dtype): # -> ExternalFunction:
        ...
    
    @classmethod
    def numba_ez_xxgetri(cls, dtype): # -> ExternalFunction:
        ...
    
    @classmethod
    def numba_ez_rgeev(cls, dtype): # -> ExternalFunction:
        ...
    
    @classmethod
    def numba_ez_cgeev(cls, dtype): # -> ExternalFunction:
        ...
    
    @classmethod
    def numba_ez_xxxevd(cls, dtype): # -> ExternalFunction:
        ...
    
    @classmethod
    def numba_xxpotrf(cls, dtype): # -> ExternalFunction:
        ...
    
    @classmethod
    def numba_ez_gesdd(cls, dtype): # -> ExternalFunction:
        ...
    
    @classmethod
    def numba_ez_geqrf(cls, dtype): # -> ExternalFunction:
        ...
    
    @classmethod
    def numba_ez_xxgqr(cls, dtype): # -> ExternalFunction:
        ...
    
    @classmethod
    def numba_ez_gelsd(cls, dtype): # -> ExternalFunction:
        ...
    
    @classmethod
    def numba_xgesv(cls, dtype): # -> ExternalFunction:
        ...
    


@contextlib.contextmanager
def make_contiguous(context, builder, sig, args): # -> Generator[tuple[Signature, tuple[Any, ...]], Any, None]:
    """
    Ensure that all array arguments are contiguous, if necessary by
    copying them.
    A new (sig, args) tuple is yielded.
    """
    ...

def check_c_int(context, builder, n): # -> None:
    """
    Check whether *n* fits in a C `int`.
    """
    ...

def check_blas_return(context, builder, res): # -> None:
    """
    Check the integer error return from one of the BLAS wrappers in
    _helperlib.c.
    """
    ...

def check_lapack_return(context, builder, res): # -> None:
    """
    Check the integer error return from one of the LAPACK wrappers in
    _helperlib.c.
    """
    ...

def call_xxdot(context, builder, conjugate, dtype, n, a_data, b_data, out_data): # -> None:
    """
    Call the BLAS vector * vector product function for the given arguments.
    """
    ...

def call_xxgemv(context, builder, do_trans, m_type, m_shapes, m_data, v_data, out_data): # -> None:
    """
    Call the BLAS matrix * vector product function for the given arguments.
    """
    ...

def call_xxgemm(context, builder, x_type, x_shapes, x_data, y_type, y_shapes, y_data, out_type, out_shapes, out_data): # -> None:
    """
    Call the BLAS matrix * matrix product function for the given arguments.
    """
    ...

def dot_2_mm(context, builder, sig, args):
    """
    np.dot(matrix, matrix)
    """
    ...

def dot_2_vm(context, builder, sig, args):
    """
    np.dot(vector, matrix)
    """
    ...

def dot_2_mv(context, builder, sig, args):
    """
    np.dot(matrix, vector)
    """
    ...

def dot_2_vv(context, builder, sig, args, conjugate=...):
    """
    np.dot(vector, vector)
    np.vdot(vector, vector)
    """
    ...

@overload(np.dot)
def dot_2(left, right): # -> Callable[..., Any] | None:
    """
    np.dot(a, b)
    """
    ...

@overload(operator.matmul)
def matmul_2(left, right): # -> Callable[..., Any] | None:
    """
    a @ b
    """
    ...

def dot_2_impl(name, left, right): # -> Callable[..., Any] | None:
    ...

@overload(np.vdot)
def vdot(left, right): # -> Callable[..., Any] | None:
    """
    np.vdot(a, b)
    """
    ...

def dot_3_vm_check_args(a, b, out): # -> None:
    ...

def dot_3_mv_check_args(a, b, out): # -> None:
    ...

def dot_3_vm(context, builder, sig, args): # -> Any:
    """
    np.dot(vector, matrix, out)
    np.dot(matrix, vector, out)
    """
    ...

def dot_3_mm(context, builder, sig, args): # -> Any:
    """
    np.dot(matrix, matrix, out)
    """
    ...

@overload(np.dot)
def dot_3(left, right, out): # -> Callable[..., Any] | None:
    """
    np.dot(a, b, out)
    """
    ...

fatal_error_func = ...
@overload(_copy_to_fortran_order)
def ol_copy_to_fortran_order(a): # -> Callable[..., NDArray[Any]]:
    ...

@overload(np.linalg.inv)
def inv_impl(a): # -> Callable[..., Any]:
    ...

@overload(np.linalg.cholesky)
def cho_impl(a): # -> Callable[..., Any]:
    ...

@overload(np.linalg.eig)
def eig_impl(a): # -> Callable[..., tuple[NDArray[float64], NDArray[float64]]]:
    ...

@overload(np.linalg.eigvals)
def eigvals_impl(a): # -> Callable[..., NDArray[float64]]:
    ...

@overload(np.linalg.eigh)
def eigh_impl(a): # -> Callable[..., tuple[NDArray[bool_ | object_ | void], Any]]:
    ...

@overload(np.linalg.eigvalsh)
def eigvalsh_impl(a): # -> Callable[..., NDArray[bool_ | object_ | void]]:
    ...

@overload(np.linalg.svd)
def svd_impl(a, full_matrices=...): # -> Callable[..., tuple[NDArray[float64], NDArray[bool_ | object_ | void], NDArray[float64]]]:
    ...

@overload(np.linalg.qr)
def qr_impl(a): # -> Callable[..., tuple[Any, NDArray[float64]]]:
    ...

@overload(np.linalg.lstsq)
def lstsq_impl(a, b, rcond=...): # -> Callable[..., tuple[Any, NDArray[bool_ | object_ | void], Any, ndarray[Any, dtype[bool_ | object_ | void]]]]:
    ...

@overload(np.linalg.solve)
def solve_impl(a, b): # -> Callable[..., NoReturn]:
    ...

@overload(np.linalg.pinv)
def pinv_impl(a, rcond=...): # -> Callable[..., Any]:
    ...

@overload(np.linalg.slogdet)
def slogdet_impl(a): # -> Callable[..., tuple[Any, Any] | tuple[float, float] | tuple[Any, float | Any]]:
    ...

@overload(np.linalg.det)
def det_impl(a): # -> Callable[..., Any]:
    ...

@overload(np.linalg.norm)
def norm_impl(x, ord=...): # -> Callable[..., NoReturn] | None:
    ...

@overload(np.linalg.cond)
def cond_impl(x, p=...): # -> Callable[..., float | Any | floating[Any]]:
    ...

@overload(np.linalg.matrix_rank)
def matrix_rank_impl(A, tol=...): # -> Callable[..., Literal[1, 0]] | None:
    """
    Computes rank for matrices and vectors.
    The only issue that may arise is that because numpy uses double
    precision lapack calls whereas numba uses type specific lapack
    calls, some singular values may differ and therefore counting the
    number of them above a tolerance may lead to different counts,
    and therefore rank, in some cases.
    """
    ...

@overload(np.linalg.matrix_power)
def matrix_power_impl(a, n): # -> Callable[..., NDArray[bool_ | object_ | void] | Any | None]:
    """
    Computes matrix power. Only integer powers are supported in numpy.
    """
    ...

@overload(np.trace)
def matrix_trace_impl(a, offset=...): # -> Callable[..., Any | Literal[0]]:
    """
    Computes the trace of an array.
    """
    ...

@register_jitable
def outer_impl_none(a, b, out): # -> NDArray[Any]:
    ...

@register_jitable
def outer_impl_arr(a, b, out):
    ...

@overload(np.outer)
def outer_impl(a, b, out=...): # -> Callable[..., NDArray[Any]]:
    ...

@overload(np.kron)
def kron_impl(a, b): # -> Callable[..., Any]:
    ...
