"""
This type stub file was generated by pyright.
"""

from .templates import AbstractTemplate

"""
This implements the typing template for `dict()`.
"""
registry = ...
infer = ...
infer_global = ...
infer_getattr = ...
_message_dict_support = ...
@infer_global(dict)
class DictBuiltin(AbstractTemplate):
    def generic(self, args, kws): # -> Signature:
        ...
    

