"""
This type stub file was generated by pyright.
"""

from numba.core.typing.templates import AbstractTemplate, AttributeTemplate, CallableTemplate, ConcreteTemplate
from numba import cuda

registry = ...
register = ...
register_attr = ...
register_global = ...
class Cuda_array_decl(CallableTemplate):
    def generic(self): # -> Callable[..., Array | None]:
        ...
    


@register
class Cuda_shared_array(Cuda_array_decl):
    key = ...


@register
class Cuda_local_array(Cuda_array_decl):
    key = ...


@register
class Cuda_const_array_like(CallableTemplate):
    key = ...
    def generic(self): # -> Callable[..., Any]:
        ...
    


@register
class Cuda_threadfence_device(ConcreteTemplate):
    key = cuda.threadfence
    cases = ...


@register
class Cuda_threadfence_block(ConcreteTemplate):
    key = cuda.threadfence_block
    cases = ...


@register
class Cuda_threadfence_system(ConcreteTemplate):
    key = cuda.threadfence_system
    cases = ...


@register
class Cuda_syncwarp(ConcreteTemplate):
    key = cuda.syncwarp
    cases = ...


@register
class Cuda_shfl_sync_intrinsic(ConcreteTemplate):
    key = cuda.shfl_sync_intrinsic
    cases = ...


@register
class Cuda_vote_sync_intrinsic(ConcreteTemplate):
    key = cuda.vote_sync_intrinsic
    cases = ...


@register
class Cuda_match_any_sync(ConcreteTemplate):
    key = cuda.match_any_sync
    cases = ...


@register
class Cuda_match_all_sync(ConcreteTemplate):
    key = cuda.match_all_sync
    cases = ...


@register
class Cuda_activemask(ConcreteTemplate):
    key = cuda.activemask
    cases = ...


@register
class Cuda_lanemask_lt(ConcreteTemplate):
    key = cuda.lanemask_lt
    cases = ...


@register
class Cuda_popc(ConcreteTemplate):
    """
    Supported types from `llvm.popc`
    [here](http://docs.nvidia.com/cuda/nvvm-ir-spec/index.html#bit-manipulations-intrinics)
    """
    key = cuda.popc
    cases = ...


@register
class Cuda_fma(ConcreteTemplate):
    """
    Supported types from `llvm.fma`
    [here](https://docs.nvidia.com/cuda/nvvm-ir-spec/index.html#standard-c-library-intrinics)
    """
    key = cuda.fma
    cases = ...


@register
class Cuda_hfma(ConcreteTemplate):
    key = cuda.fp16.hfma
    cases = ...


@register
class Cuda_cbrt(ConcreteTemplate):
    key = cuda.cbrt
    cases = ...


@register
class Cuda_brev(ConcreteTemplate):
    key = cuda.brev
    cases = ...


@register
class Cuda_clz(ConcreteTemplate):
    """
    Supported types from `llvm.ctlz`
    [here](http://docs.nvidia.com/cuda/nvvm-ir-spec/index.html#bit-manipulations-intrinics)
    """
    key = cuda.clz
    cases = ...


@register
class Cuda_ffs(ConcreteTemplate):
    """
    Supported types from `llvm.cttz`
    [here](http://docs.nvidia.com/cuda/nvvm-ir-spec/index.html#bit-manipulations-intrinics)
    """
    key = cuda.ffs
    cases = ...


@register
class Cuda_selp(AbstractTemplate):
    key = cuda.selp
    def generic(self, args, kws): # -> Signature | None:
        ...
    


@register_global(float)
class Float(AbstractTemplate):
    def generic(self, args, kws): # -> Signature | None:
        ...
    


Cuda_hadd = ...
Cuda_add = ...
Cuda_iadd = ...
Cuda_hsub = ...
Cuda_sub = ...
Cuda_isub = ...
Cuda_hmul = ...
Cuda_mul = ...
Cuda_imul = ...
Cuda_hmax = ...
Cuda_hmin = ...
Cuda_hneg = ...
Cuda_neg = ...
Cuda_habs = ...
Cuda_abs = ...
Cuda_heq = ...
Cuda_hne = ...
Cuda_hge = ...
Cuda_hgt = ...
Cuda_hle = ...
Cuda_hlt = ...
hsin_device = ...
hcos_device = ...
hlog_device = ...
hlog10_device = ...
hlog2_device = ...
hexp_device = ...
hexp10_device = ...
hexp2_device = ...
hsqrt_device = ...
hrsqrt_device = ...
hfloor_device = ...
hceil_device = ...
hrcp_device = ...
hrint_device = ...
htrunc_device = ...
hdiv_device = ...
all_numba_types = ...
integer_numba_types = ...
unsigned_int_numba_types = ...
Cuda_atomic_add = ...
Cuda_atomic_sub = ...
Cuda_atomic_max = ...
Cuda_atomic_min = ...
Cuda_atomic_nanmax = ...
Cuda_atomic_nanmin = ...
Cuda_atomic_and = ...
Cuda_atomic_or = ...
Cuda_atomic_xor = ...
Cuda_atomic_inc = ...
Cuda_atomic_dec = ...
Cuda_atomic_exch = ...
@register
class Cuda_atomic_compare_and_swap(AbstractTemplate):
    key = cuda.atomic.compare_and_swap
    def generic(self, args, kws): # -> Signature | None:
        ...
    


@register
class Cuda_atomic_cas(AbstractTemplate):
    key = cuda.atomic.cas
    def generic(self, args, kws): # -> Signature | None:
        ...
    


@register
class Cuda_nanosleep(ConcreteTemplate):
    key = cuda.nanosleep
    cases = ...


@register_attr
class Dim3_attrs(AttributeTemplate):
    key = ...
    def resolve_x(self, mod): # -> Integer:
        ...
    
    def resolve_y(self, mod): # -> Integer:
        ...
    
    def resolve_z(self, mod): # -> Integer:
        ...
    


@register_attr
class CudaSharedModuleTemplate(AttributeTemplate):
    key = ...
    def resolve_array(self, mod): # -> Function:
        ...
    


@register_attr
class CudaConstModuleTemplate(AttributeTemplate):
    key = ...
    def resolve_array_like(self, mod): # -> Function:
        ...
    


@register_attr
class CudaLocalModuleTemplate(AttributeTemplate):
    key = ...
    def resolve_array(self, mod): # -> Function:
        ...
    


@register_attr
class CudaAtomicTemplate(AttributeTemplate):
    key = ...
    def resolve_add(self, mod): # -> Function:
        ...
    
    def resolve_sub(self, mod): # -> Function:
        ...
    
    def resolve_and_(self, mod): # -> Function:
        ...
    
    def resolve_or_(self, mod): # -> Function:
        ...
    
    def resolve_xor(self, mod): # -> Function:
        ...
    
    def resolve_inc(self, mod): # -> Function:
        ...
    
    def resolve_dec(self, mod): # -> Function:
        ...
    
    def resolve_exch(self, mod): # -> Function:
        ...
    
    def resolve_max(self, mod): # -> Function:
        ...
    
    def resolve_min(self, mod): # -> Function:
        ...
    
    def resolve_nanmin(self, mod): # -> Function:
        ...
    
    def resolve_nanmax(self, mod): # -> Function:
        ...
    
    def resolve_compare_and_swap(self, mod): # -> Function:
        ...
    
    def resolve_cas(self, mod): # -> Function:
        ...
    


@register_attr
class CudaFp16Template(AttributeTemplate):
    key = ...
    def resolve_hadd(self, mod): # -> Function:
        ...
    
    def resolve_hsub(self, mod): # -> Function:
        ...
    
    def resolve_hmul(self, mod): # -> Function:
        ...
    
    def resolve_hdiv(self, mod): # -> Function:
        ...
    
    def resolve_hneg(self, mod): # -> Function:
        ...
    
    def resolve_habs(self, mod): # -> Function:
        ...
    
    def resolve_hfma(self, mod): # -> Function:
        ...
    
    def resolve_hsin(self, mod): # -> Function:
        ...
    
    def resolve_hcos(self, mod): # -> Function:
        ...
    
    def resolve_hlog(self, mod): # -> Function:
        ...
    
    def resolve_hlog10(self, mod): # -> Function:
        ...
    
    def resolve_hlog2(self, mod): # -> Function:
        ...
    
    def resolve_hexp(self, mod): # -> Function:
        ...
    
    def resolve_hexp10(self, mod): # -> Function:
        ...
    
    def resolve_hexp2(self, mod): # -> Function:
        ...
    
    def resolve_hfloor(self, mod): # -> Function:
        ...
    
    def resolve_hceil(self, mod): # -> Function:
        ...
    
    def resolve_hsqrt(self, mod): # -> Function:
        ...
    
    def resolve_hrsqrt(self, mod): # -> Function:
        ...
    
    def resolve_hrcp(self, mod): # -> Function:
        ...
    
    def resolve_hrint(self, mod): # -> Function:
        ...
    
    def resolve_htrunc(self, mod): # -> Function:
        ...
    
    def resolve_heq(self, mod): # -> Function:
        ...
    
    def resolve_hne(self, mod): # -> Function:
        ...
    
    def resolve_hge(self, mod): # -> Function:
        ...
    
    def resolve_hgt(self, mod): # -> Function:
        ...
    
    def resolve_hle(self, mod): # -> Function:
        ...
    
    def resolve_hlt(self, mod): # -> Function:
        ...
    
    def resolve_hmax(self, mod): # -> Function:
        ...
    
    def resolve_hmin(self, mod): # -> Function:
        ...
    


@register_attr
class CudaModuleTemplate(AttributeTemplate):
    key = ...
    def resolve_cg(self, mod): # -> Module:
        ...
    
    def resolve_threadIdx(self, mod): # -> Dim3:
        ...
    
    def resolve_blockIdx(self, mod): # -> Dim3:
        ...
    
    def resolve_blockDim(self, mod): # -> Dim3:
        ...
    
    def resolve_gridDim(self, mod): # -> Dim3:
        ...
    
    def resolve_laneid(self, mod): # -> Integer:
        ...
    
    def resolve_shared(self, mod): # -> Module:
        ...
    
    def resolve_popc(self, mod): # -> Function:
        ...
    
    def resolve_brev(self, mod): # -> Function:
        ...
    
    def resolve_clz(self, mod): # -> Function:
        ...
    
    def resolve_ffs(self, mod): # -> Function:
        ...
    
    def resolve_fma(self, mod): # -> Function:
        ...
    
    def resolve_cbrt(self, mod): # -> Function:
        ...
    
    def resolve_threadfence(self, mod): # -> Function:
        ...
    
    def resolve_threadfence_block(self, mod): # -> Function:
        ...
    
    def resolve_threadfence_system(self, mod): # -> Function:
        ...
    
    def resolve_syncwarp(self, mod): # -> Function:
        ...
    
    def resolve_shfl_sync_intrinsic(self, mod): # -> Function:
        ...
    
    def resolve_vote_sync_intrinsic(self, mod): # -> Function:
        ...
    
    def resolve_match_any_sync(self, mod): # -> Function:
        ...
    
    def resolve_match_all_sync(self, mod): # -> Function:
        ...
    
    def resolve_activemask(self, mod): # -> Function:
        ...
    
    def resolve_lanemask_lt(self, mod): # -> Function:
        ...
    
    def resolve_selp(self, mod): # -> Function:
        ...
    
    def resolve_nanosleep(self, mod): # -> Function:
        ...
    
    def resolve_atomic(self, mod): # -> Module:
        ...
    
    def resolve_fp16(self, mod): # -> Module:
        ...
    
    def resolve_const(self, mod): # -> Module:
        ...
    
    def resolve_local(self, mod): # -> Module:
        ...
    

