"""
This type stub file was generated by pyright.
"""

from numba.core import types
from numba.core.extending import overload_method

"""
Implementation of method overloads for Generator objects.
"""
def check_size(size): # -> None:
    ...

def check_types(obj, type_list, arg_name): # -> None:
    """
    Check if given object is one of the provided types.
    If not raises an TypeError
    """
    ...

@overload_method(types.NumPyRandomGeneratorType, 'integers')
def NumPyRandomGeneratorType_integers(inst, low, high, size=..., dtype=..., endpoint=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'shuffle')
def NumPyRandomGeneratorType_shuffle(inst, x, axis=...): # -> Callable[..., None]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'permutation')
def NumPyRandomGeneratorType_permutation(inst, x, axis=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'random')
def NumPyRandomGeneratorType_random(inst, size=..., dtype=...): # -> Callable[..., Any | Signature]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'standard_exponential')
def NumPyRandomGeneratorType_standard_exponential(inst, size=..., dtype=..., method=...): # -> Callable[..., Any | Signature]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'standard_normal')
def NumPyRandomGeneratorType_standard_normal(inst, size=..., dtype=...): # -> Callable[..., Any | Signature]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'standard_gamma')
def NumPyRandomGeneratorType_standard_gamma(inst, shape, size=..., dtype=...): # -> Callable[..., Any | Signature]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'normal')
def NumPyRandomGeneratorType_normal(inst, loc=..., scale=..., size=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'uniform')
def NumPyRandomGeneratorType_uniform(inst, low=..., high=..., size=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'exponential')
def NumPyRandomGeneratorType_exponential(inst, scale=..., size=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'gamma')
def NumPyRandomGeneratorType_gamma(inst, shape, scale=..., size=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'beta')
def NumPyRandomGeneratorType_beta(inst, a, b, size=...): # -> Callable[..., Any | None]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'f')
def NumPyRandomGeneratorType_f(inst, dfnum, dfden, size=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'chisquare')
def NumPyRandomGeneratorType_chisquare(inst, df, size=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'standard_cauchy')
def NumPyRandomGeneratorType_standard_cauchy(inst, size=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'pareto')
def NumPyRandomGeneratorType_pareto(inst, a, size=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'weibull')
def NumPyRandomGeneratorType_weibull(inst, a, size=...): # -> Callable[..., float | Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'power')
def NumPyRandomGeneratorType_power(inst, a, size=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'laplace')
def NumPyRandomGeneratorType_laplace(inst, loc=..., scale=..., size=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'logistic')
def NumPyRandomGeneratorType_logistic(inst, loc=..., scale=..., size=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'lognormal')
def NumPyRandomGeneratorType_lognormal(inst, mean=..., sigma=..., size=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'rayleigh')
def NumPyRandomGeneratorType_rayleigh(inst, scale=..., size=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'standard_t')
def NumPyRandomGeneratorType_standard_t(inst, df, size=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'wald')
def NumPyRandomGeneratorType_wald(inst, mean, scale, size=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'geometric')
def NumPyRandomGeneratorType_geometric(inst, p, size=...): # -> Callable[..., int64]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'zipf')
def NumPyRandomGeneratorType_zipf(inst, a, size=...): # -> Callable[..., int64]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'triangular')
def NumPyRandomGeneratorType_triangular(inst, left, mode, right, size=...): # -> Callable[..., Any]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'poisson')
def NumPyRandomGeneratorType_poisson(inst, lam, size=...): # -> Callable[..., int64]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'negative_binomial')
def NumPyRandomGeneratorType_negative_binomial(inst, n, p, size=...): # -> Callable[..., int64]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'noncentral_chisquare')
def NumPyRandomGeneratorType_noncentral_chisquare(inst, df, nonc, size=...): # -> Callable[..., float64]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'noncentral_f')
def NumPyRandomGeneratorType_noncentral_f(inst, dfnum, dfden, nonc, size=...): # -> Callable[..., float64]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'logseries')
def NumPyRandomGeneratorType_logseries(inst, p, size=...): # -> Callable[..., int64]:
    ...

@overload_method(types.NumPyRandomGeneratorType, 'binomial')
def NumPyRandomGeneratorType_binomial(inst, n, p, size=...): # -> Callable[..., int64]:
    ...
