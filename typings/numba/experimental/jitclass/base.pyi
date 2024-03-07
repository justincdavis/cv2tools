"""
This type stub file was generated by pyright.
"""

from numba.core import types
from numba.core.datamodel import models
from numba.core.typing import templates
from numba.core.serialize import disable_pickling

class InstanceModel(models.StructModel):
    def __init__(self, dmm, fe_typ) -> None:
        ...
    


class InstanceDataModel(models.StructModel):
    def __init__(self, dmm, fe_typ) -> None:
        ...
    


_ctor_template = ...
@disable_pickling
class JitClassType(type):
    """
    The type of any jitclass.
    """
    def __new__(cls, name, bases, dct): # -> Self:
        ...
    
    def __instancecheck__(cls, instance): # -> bool:
        ...
    
    def __call__(cls, *args, **kwargs): # -> Any | Callable[..., FakeCUDAKernel] | FakeCUDAKernel | CUDADispatcher | FunctionType | None:
        ...
    


def register_class_type(cls, spec, class_ctor, builder): # -> type[__class_JitClassType]:
    """
    Internal function to create a jitclass.

    Args
    ----
    cls: the original class object (used as the prototype)
    spec: the structural specification contains the field types.
    class_ctor: the numba type to represent the jitclass
    builder: the internal jitclass builder
    """
    ...

class ConstructorTemplate(templates.AbstractTemplate):
    """
    Base class for jitclass constructor templates.
    """
    def generic(self, args, kws): # -> Signature:
        ...
    


class ClassBuilder:
    """
    A jitclass builder for a mutable jitclass.  This will register
    typing and implementation hooks to the given typing and target contexts.
    """
    class_impl_registry = ...
    implemented_methods = ...
    def __init__(self, class_type, typingctx, targetctx) -> None:
        ...
    
    def register(self): # -> None:
        """
        Register to the frontend and backend.
        """
        ...
    


@templates.infer_getattr
class ClassAttribute(templates.AttributeTemplate):
    key = types.ClassInstanceType
    def generic_resolve(self, instance, attr): # -> BoundFunction | None:
        ...
    


@ClassBuilder.class_impl_registry.lower_getattr_generic(types.ClassInstanceType)
def get_attr_impl(context, builder, typ, value, attr): # -> Any:
    """
    Generic getattr() for @jitclass instances.
    """
    ...

@ClassBuilder.class_impl_registry.lower_setattr_generic(types.ClassInstanceType)
def set_attr_impl(context, builder, sig, args, attr): # -> None:
    """
    Generic setattr() for @jitclass instances.
    """
    ...

def imp_dtor(context, module, instance_type): # -> Function:
    ...

@ClassBuilder.class_impl_registry.lower(types.ClassType, types.VarArg(types.Any))
def ctor_impl(context, builder, sig, args):
    """
    Generic constructor (__new__) for jitclasses.
    """
    ...

