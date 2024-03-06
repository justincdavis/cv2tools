"""
This type stub file was generated by pyright.
"""

import dis
from dataclasses import dataclass
from typing import Mapping, NamedTuple, Optional, Protocol, TYPE_CHECKING, TypeVar, Union, runtime_checkable
from numba_rvsdg.core.datastructures.byte_flow import ByteFlow
from numba_rvsdg.core.datastructures.scfg import SCFG
from numba_rvsdg.core.datastructures.basic_block import BasicBlock, PythonBytecodeBlock, RegionBlock, SyntheticAssignment, SyntheticBranch
from numba.core.utils import MutableSortedMap, MutableSortedSet
from .regionpasses import RegionTransformer, RegionVisitor
from .regionrenderer import GraphBuilder

if TYPE_CHECKING:
    ...
DEBUG_GRAPH = ...
T = TypeVar("T")
@dataclass(frozen=True)
class ValueState:
    """For representing a RVSDG Value (State).

    For most compiler passes, Value and State can be treated as the same.
    """
    parent: Optional[Op]
    name: str
    out_index: int
    is_effect: bool = ...
    def short_identity(self) -> str:
        ...
    
    def __hash__(self) -> int:
        ...
    


@dataclass(frozen=True)
class Op:
    """For representing a RVSDG operation.

    An Op has inputs and outputs ports that are ValueStates.
    An Op can optionally have a bytecode instruction associated with it.
    """
    opname: str
    bc_inst: Optional[dis.Instruction]
    _inputs: dict[str, ValueState] = ...
    _outputs: dict[str, ValueState] = ...
    def add_input(self, name, vs: ValueState): # -> None:
        ...
    
    def add_output(self, name: str, is_effect=...) -> ValueState:
        ...
    
    def short_identity(self) -> str:
        ...
    
    def summary(self) -> str:
        ...
    
    @property
    def outputs(self) -> list[ValueState]:
        ...
    
    @property
    def inputs(self) -> list[ValueState]:
        ...
    
    @property
    def input_ports(self) -> Mapping[str, ValueState]:
        ...
    
    @property
    def output_ports(self) -> Mapping[str, ValueState]:
        ...
    
    def __hash__(self) -> int:
        ...
    


@runtime_checkable
class DDGProtocol(Protocol):
    incoming_states: MutableSortedSet[str]
    outgoing_states: MutableSortedSet[str]
    ...


@dataclass(frozen=True)
class DDGRegion(RegionBlock):
    incoming_states: MutableSortedSet[str] = ...
    outgoing_states: MutableSortedSet[str] = ...


@dataclass(frozen=True)
class DDGBranch(SyntheticBranch):
    incoming_states: MutableSortedSet[str] = ...
    outgoing_states: MutableSortedSet[str] = ...


@dataclass(frozen=True)
class DDGControlVariable(SyntheticAssignment):
    incoming_states: MutableSortedSet[str] = ...
    outgoing_states: MutableSortedSet[str] = ...


@dataclass(frozen=True)
class DDGBlock(BasicBlock):
    in_effect: ValueState | None = ...
    out_effect: ValueState | None = ...
    in_stackvars: list[ValueState] = ...
    out_stackvars: list[ValueState] = ...
    in_vars: MutableSortedMap[str, ValueState] = ...
    out_vars: MutableSortedMap[str, ValueState] = ...
    exported_stackvars: MutableSortedMap[str, ValueState] = ...
    def __post_init__(self): # -> None:
        ...
    
    def render_graph(self, builder: GraphBuilder): # -> None:
        ...
    
    @property
    def incoming_states(self) -> MutableSortedSet:
        ...
    
    @property
    def outgoing_states(self) -> MutableSortedSet:
        ...
    
    def get_toposorted_ops(self) -> list[Op]:
        """Get a topologically sorted list of ``Op`` according
        to the data-dependence.

        Operations stored later in the list may depend on earlier operations,
        but the reverse can never be true.
        """
        ...
    


def render_scfg(byteflow): # -> None:
    ...

class CanonicalizeLoop(RegionTransformer[None]):
    """
    Make sure loops has non-region header.

    Preferably, the exiting block should be non-region as well but
    it's hard to do with the current numba_rvsdg API.

    Doing this so we don't have to fixup backedges as backedges will always
    point to a non-region node in ``_canonicalize_scfg_switch``.
    """
    def visit_loop(self, parent: SCFG, region: RegionBlock, data: None): # -> None:
        ...
    
    def visit_block(self, parent: SCFG, block: BasicBlock, data: None): # -> None:
        ...
    
    def visit_switch(self, parent: SCFG, block: BasicBlock, data: None): # -> None:
        ...
    


def canonicalize_scfg(scfg: SCFG): # -> None:
    ...

class _ExtraBranch(NamedTuple):
    branch_instlists: tuple[tuple[str, ...], ...] = ...


@dataclass(frozen=True)
class ExtraBasicBlock(BasicBlock):
    inst_list: tuple[str, ...] = ...
    @classmethod
    def make(cls, label, jump_target, instlist): # -> ExtraBasicBlock:
        ...
    
    def __str__(self) -> str:
        ...
    


class HandleConditionalPop:
    """Introduce pop-stack operations to the bytecode to correctly model
    operations that conditionally pop elements from the stack. Numba-rvsdg does
    not handle this. For example, FOR_ITER pop the stack when the iterator is
    exhausted.
    """
    def handle(self, inst: dis.Instruction) -> _ExtraBranch | None:
        ...
    
    def op_FOR_ITER(self, inst: dis.Instruction) -> _ExtraBranch:
        ...
    
    def op_JUMP_IF_TRUE_OR_POP(self, inst: dis.Instruction) -> _ExtraBranch:
        ...
    
    def op_JUMP_IF_FALSE_OR_POP(self, inst: dis.Instruction) -> _ExtraBranch:
        ...
    


def build_rvsdg(code, argnames: tuple[str, ...]) -> SCFG:
    ...

DDGTypes = ...
_DDGTypeAnn = Union[DDGBlock, DDGControlVariable, DDGBranch]
def convert_to_dataflow(byteflow: ByteFlow, argnames: tuple[str, ...]) -> SCFG:
    ...

def propagate_states(rvsdg: SCFG) -> SCFG:
    ...

def propagate_vars(rvsdg: SCFG): # -> None:
    ...

_pvData = set[str]
class PropagateVars(RegionVisitor[_pvData]):
    """
    Depends on PropagateStack
    """
    def __init__(self, _debug: bool = ...) -> None:
        ...
    
    def debug_print(self, *args, **kwargs): # -> None:
        ...
    
    def visit_linear(self, region: RegionBlock, data: _pvData) -> _pvData:
        ...
    
    def visit_block(self, block: BasicBlock, data: _pvData) -> _pvData:
        ...
    
    def visit_loop(self, region: RegionBlock, data: _pvData) -> _pvData:
        ...
    
    def visit_switch(self, region: RegionBlock, data: _pvData) -> _pvData:
        ...
    
    def make_data(self) -> _pvData:
        ...
    


_psData = tuple[str, ...]
class PropagateStack(RegionVisitor[_psData]):
    def __init__(self, _debug: bool = ...) -> None:
        ...
    
    def debug_print(self, *args, **kwargs): # -> None:
        ...
    
    def visit_block(self, block: BasicBlock, data: _psData) -> _psData:
        ...
    
    def visit_loop(self, region: RegionBlock, data: _psData) -> _psData:
        ...
    
    def visit_switch(self, region: RegionBlock, data: _psData) -> _psData:
        ...
    
    def make_data(self) -> _psData:
        ...
    


class ConnectImportedStackVars(RegionVisitor[None]):
    def visit_block(self, block: BasicBlock, data: None): # -> None:
        ...
    
    def visit_loop(self, region: RegionBlock, data: None): # -> None:
        ...
    
    def visit_switch(self, region: RegionBlock, data: None): # -> None:
        ...
    


def propagate_stack(rvsdg: SCFG): # -> None:
    ...

def connect_incoming_stack_vars(rvsdg: SCFG): # -> None:
    ...

def convert_scfg_to_dataflow(scfg, bcmap, argnames: tuple[str, ...]) -> SCFG:
    ...

def convert_extra_bb(block: ExtraBasicBlock) -> DDGBlock:
    ...

def convert_bc_to_ddg(block: PythonBytecodeBlock, bcmap: dict[int, dis.Bytecode], argnames: tuple[str, ...]) -> DDGBlock:
    ...

class BC2DDG:
    stack: list[ValueState]
    effect: ValueState
    in_effect: ValueState
    varmap: dict[str, ValueState]
    incoming_vars: dict[str, ValueState]
    incoming_stackvars: list[ValueState]
    _kw_names: ValueState | None
    def __init__(self) -> None:
        ...
    
    def push(self, val: ValueState): # -> None:
        ...
    
    def pop(self) -> ValueState:
        ...
    
    def top(self) -> ValueState:
        ...
    
    def store(self, varname: str, value: ValueState): # -> None:
        ...
    
    def load(self, varname: str) -> ValueState:
        ...
    
    def replace_effect(self, env: ValueState): # -> None:
        ...
    
    def convert(self, inst: dis.Instruction): # -> None:
        ...
    
    def set_kw_names(self, kw_vs: ValueState): # -> None:
        ...
    
    def pop_kw_names(self): # -> ValueState | None:
        ...
    
    def op_POP_TOP(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_RESUME(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_COPY_FREE_VARS(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_PUSH_NULL(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_LOAD_GLOBAL(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_LOAD_CONST(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_STORE_FAST(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_LOAD_FAST(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_LOAD_ATTR(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_LOAD_METHOD(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_LOAD_DEREF(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_PRECALL(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_KW_NAMES(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_CALL(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_GET_ITER(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_FOR_ITER(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_BINARY_OP(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_COMPARE_OP(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_IS_OP(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_UNARY_NOT(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_BINARY_SUBSCR(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_STORE_SUBSCR(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_BUILD_TUPLE(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_BUILD_SLICE(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_RETURN_VALUE(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_RAISE_VARARGS(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_JUMP_FORWARD(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_JUMP_BACKWARD(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_POP_JUMP_FORWARD_IF_TRUE(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_POP_JUMP_FORWARD_IF_FALSE(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_POP_JUMP_BACKWARD_IF_TRUE(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_POP_JUMP_BACKWARD_IF_FALSE(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_POP_JUMP_FORWARD_IF_NONE(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_POP_JUMP_FORWARD_IF_NOT_NONE(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_JUMP_IF_TRUE_OR_POP(self, inst: dis.Instruction): # -> None:
        ...
    
    def op_JUMP_IF_FALSE_OR_POP(self, inst: dis.Instruction): # -> None:
        ...
    

