"""
This type stub file was generated by pyright.
"""

import cmath
from numba.core.typing.templates import ConcreteTemplate

registry = ...
infer_global = ...
@infer_global(cmath.acos)
@infer_global(cmath.asin)
@infer_global(cmath.asinh)
@infer_global(cmath.atan)
@infer_global(cmath.atanh)
@infer_global(cmath.cos)
@infer_global(cmath.exp)
@infer_global(cmath.sin)
@infer_global(cmath.sqrt)
@infer_global(cmath.tan)
class CMath_unary(ConcreteTemplate):
    cases = ...


@infer_global(cmath.isinf)
@infer_global(cmath.isnan)
class CMath_predicate(ConcreteTemplate):
    cases = ...


@infer_global(cmath.isfinite)
class CMath_isfinite(CMath_predicate):
    ...


@infer_global(cmath.log)
class Cmath_log(ConcreteTemplate):
    cases = ...


