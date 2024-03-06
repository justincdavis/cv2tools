"""
This type stub file was generated by pyright.
"""

from numba.core.rewrites import Rewrite, register_rewrite

@register_rewrite('before-inference')
class RewriteConstRaises(Rewrite):
    """
    Rewrite IR statements of the kind `raise(value)`
    where `value` is the result of instantiating an exception with
    constant arguments
    into `static_raise(exception_type, constant args)`.

    This allows lowering in nopython mode, where one can't instantiate
    exception instances from runtime data.
    """
    def match(self, func_ir, block, typemap, calltypes): # -> bool:
        ...
    
    def apply(self):
        """
        Rewrite all matching setitems as static_setitems.
        """
        ...
    

