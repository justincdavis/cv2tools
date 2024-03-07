"""
This type stub file was generated by pyright.
"""

import contextlib
from numba.core import types

"""
Type inference base on CPA.
The algorithm guarantees monotonic growth of type-sets for each variable.

Steps:
    1. seed initial types
    2. build constraints
    3. propagate constraints
    4. unify types

Constraint propagation is precise and does not regret (no backtracing).
Constraints push types forward following the dataflow.
"""
_logger = ...
class NOTSET:
    ...


_termcolor = ...
class TypeVar:
    def __init__(self, context, var) -> None:
        ...
    
    def add_type(self, tp, loc): # -> Type | None:
        ...
    
    def lock(self, tp, loc, literal_value=...): # -> None:
        ...
    
    def union(self, other, loc): # -> Type | None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    @property
    def defined(self): # -> bool:
        ...
    
    def get(self): # -> tuple[Type | Any] | tuple[()]:
        ...
    
    def getone(self): # -> Type:
        ...
    
    def __len__(self): # -> Literal[1, 0]:
        ...
    


class ConstraintNetwork:
    """
    TODO: It is possible to optimize constraint propagation to consider only
          dirty type variables.
    """
    def __init__(self) -> None:
        ...
    
    def append(self, constraint): # -> None:
        ...
    
    def propagate(self, typeinfer): # -> list[Any]:
        """
        Execute all constraints.  Errors are caught and returned as a list.
        This allows progressing even though some constraints may fail
        due to lack of information
        (e.g. imprecise types such as List(undefined)).
        """
        ...
    


class Propagate:
    """
    A simple constraint for direct propagation of types for assignments.
    """
    def __init__(self, dst, src, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    
    def refine(self, typeinfer, target_type): # -> None:
        ...
    


class ArgConstraint:
    def __init__(self, dst, src, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    


class BuildTupleConstraint:
    def __init__(self, target, items, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    


class _BuildContainerConstraint:
    def __init__(self, target, items, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    


class BuildListConstraint(_BuildContainerConstraint):
    def __init__(self, target, items, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    


class BuildSetConstraint(_BuildContainerConstraint):
    container_type = types.Set


class BuildMapConstraint:
    def __init__(self, target, items, special_value, value_indexes, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    


class ExhaustIterConstraint:
    def __init__(self, target, count, iterator, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    


class PairFirstConstraint:
    def __init__(self, target, pair, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    


class PairSecondConstraint:
    def __init__(self, target, pair, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    


class StaticGetItemConstraint:
    def __init__(self, target, value, index, index_var, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    
    def get_call_signature(self): # -> None:
        ...
    


class TypedGetItemConstraint:
    def __init__(self, target, value, dtype, index, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    
    def get_call_signature(self): # -> Signature:
        ...
    


def fold_arg_vars(typevars, args, vararg, kws): # -> tuple[tuple[Any, ...] | Any, dict[Any, Any]] | None:
    """
    Fold and resolve the argument variables of a function call.
    """
    ...

class CallConstraint:
    """Constraint for calling functions.
    Perform case analysis foreach combinations of argument types.
    """
    signature = ...
    def __init__(self, target, func, args, kws, vararg, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    
    def resolve(self, typeinfer, typevars, fnty): # -> None:
        ...
    
    def refine(self, typeinfer, updated_type): # -> None:
        ...
    
    def get_call_signature(self): # -> None:
        ...
    


class IntrinsicCallConstraint(CallConstraint):
    def __call__(self, typeinfer): # -> None:
        ...
    


class GetAttrConstraint:
    def __init__(self, target, attr, value, loc, inst) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    
    def refine(self, typeinfer, target_type): # -> None:
        ...
    
    def __repr__(self): # -> LiteralString:
        ...
    


class SetItemRefinement:
    """A mixin class to provide the common refinement logic in setitem
    and static setitem.
    """
    ...


class SetItemConstraint(SetItemRefinement):
    def __init__(self, target, index, value, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    
    def get_call_signature(self):
        ...
    


class StaticSetItemConstraint(SetItemRefinement):
    def __init__(self, target, index, index_var, value, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    
    def get_call_signature(self):
        ...
    


class DelItemConstraint:
    def __init__(self, target, index, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    
    def get_call_signature(self):
        ...
    


class SetAttrConstraint:
    def __init__(self, target, attr, value, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    
    def get_call_signature(self):
        ...
    


class PrintConstraint:
    def __init__(self, args, vararg, loc) -> None:
        ...
    
    def __call__(self, typeinfer): # -> None:
        ...
    
    def get_call_signature(self):
        ...
    


class TypeVarMap(dict):
    def set_context(self, context): # -> None:
        ...
    
    def __getitem__(self, name):
        ...
    
    def __setitem__(self, name, value): # -> None:
        ...
    


_temporary_dispatcher_map = ...
_temporary_dispatcher_map_ref_count = ...
@contextlib.contextmanager
def register_dispatcher(disp): # -> Generator[None, Any, None]:
    """
    Register a Dispatcher for inference while it is not yet stored
    as global or closure variable (e.g. during execution of the @jit()
    call).  This allows resolution of recursive calls with eager
    compilation.
    """
    ...

typeinfer_extensions = ...
class TypeInferer:
    """
    Operates on block that shares the same ir.Scope.
    """
    def __init__(self, context, func_ir, warnings) -> None:
        ...
    
    def copy(self, skip_recursion=...): # -> TypeInferer:
        ...
    
    def get_argument_types(self): # -> list[Any]:
        ...
    
    def seed_argument(self, name, index, typ): # -> None:
        ...
    
    def seed_type(self, name, typ): # -> None:
        """All arguments should be seeded.
        """
        ...
    
    def seed_return(self, typ): # -> None:
        """Seeding of return value is optional.
        """
        ...
    
    def build_constraint(self): # -> None:
        ...
    
    def return_types_from_partial(self): # -> FunctionType | numba.core.types.misc.NoneType | None:
        """
        Resume type inference partially to deduce the return type.
        Note: No side-effect to `self`.

        Returns the inferred return type or None if it cannot deduce the return
        type.
        """
        ...
    
    def propagate(self, raise_errors=...): # -> list[Any] | None:
        ...
    
    def add_type(self, var, tp, loc, unless_locked=...): # -> None:
        ...
    
    def add_calltype(self, inst, signature): # -> None:
        ...
    
    def copy_type(self, src_var, dest_var, loc): # -> None:
        ...
    
    def lock_type(self, var, tp, loc, literal_value=...): # -> None:
        ...
    
    def propagate_refined_type(self, updated_var, updated_type): # -> None:
        ...
    
    def unify(self, raise_errors=...): # -> tuple[UniqueDict, Generator | FunctionType | Any | numba.core.types.misc.NoneType | None, UniqueDict | None]:
        """
        Run the final unification pass over all inferred types, and
        catch imprecise types.
        """
        ...
    
    def get_generator_type(self, typdict, retty, raise_errors=...): # -> Generator:
        ...
    
    def get_function_types(self, typemap): # -> UniqueDict:
        """
        Fill and return the calltypes map.
        """
        ...
    
    def get_return_type(self, typemap): # -> FunctionType | NoneType:
        ...
    
    def get_state_token(self): # -> list[Any]:
        """The algorithm is monotonic.  It can only grow or "refine" the
        typevar map.
        """
        ...
    
    def constrain_statement(self, inst): # -> None:
        ...
    
    def typeof_setitem(self, inst): # -> None:
        ...
    
    def typeof_storemap(self, inst): # -> None:
        ...
    
    def typeof_static_setitem(self, inst): # -> None:
        ...
    
    def typeof_delitem(self, inst): # -> None:
        ...
    
    def typeof_setattr(self, inst): # -> None:
        ...
    
    def typeof_print(self, inst): # -> None:
        ...
    
    def typeof_assign(self, inst): # -> None:
        ...
    
    def resolve_value_type(self, inst, val):
        """
        Resolve the type of a simple Python value, such as can be
        represented by literals.
        """
        ...
    
    def typeof_arg(self, inst, target, arg): # -> None:
        ...
    
    def typeof_const(self, inst, target, const): # -> None:
        ...
    
    def typeof_yield(self, inst, target, yield_): # -> None:
        ...
    
    def sentry_modified_builtin(self, inst, gvar): # -> None:
        """
        Ensure that builtins are not modified.
        """
        ...
    
    def resolve_call(self, fnty, pos_args, kw_args): # -> Any | Signature:
        """
        Resolve a call to a given function type.  A signature is returned.
        """
        ...
    
    def typeof_global(self, inst, target, gvar): # -> None:
        ...
    
    def typeof_expr(self, inst, target, expr): # -> None:
        ...
    
    def typeof_call(self, inst, target, call): # -> None:
        ...
    
    def typeof_intrinsic_call(self, inst, target, func, *args): # -> None:
        ...
    


class NullDebug:
    def propagate_started(self): # -> None:
        ...
    
    def propagate_finished(self): # -> None:
        ...
    
    def unify_finished(self, typdict, retty, fntys): # -> None:
        ...
    


class TypeInferDebug:
    def __init__(self, typeinfer) -> None:
        ...
    
    def propagate_started(self): # -> None:
        ...
    
    def propagate_finished(self): # -> None:
        ...
    
    def unify_finished(self, typdict, retty, fntys): # -> None:
        ...
    


