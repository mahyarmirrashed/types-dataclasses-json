import abc
from typing import Any, Callable, Dict, Optional, Tuple, Type, TypeVar, Union, overload

from dataclasses_json.cfg import LetterCase
from dataclasses_json.core import Json
from dataclasses_json.mm import JsonInput, SchemaType
from dataclasses_json.undefined import Undefined
from marshmallow import types

T = TypeVar("T")
U = TypeVar("U", bound="DataClassJsonMixin")

class DataClassJsonMixin(abc.ABC):
    dataclass_json_config: Optional[Dict[str, Any]]
    def to_json(
        self,
        *,
        skipkeys: bool = False,
        ensure_ascii: bool = True,
        check_circular: bool = True,
        allow_nan: bool = True,
        indent: Optional[Union[int, str]] = None,
        separators: Optional[Tuple[str, str]] = None,
        default: Optional[Callable[[Any], Any]] = None,
        sort_keys: bool = False,
        **kwargs: Dict[str, Any]
    ) -> str: ...
    @classmethod
    def from_json(
        cls: Type[U],
        s: JsonInput,
        *,
        parse_float: Optional[Callable[[str], Any]] = None,
        parse_int: Optional[Callable[[str], Any]] = None,
        parse_constant: Optional[Callable[[str], Any]] = None,
        infer_missing: bool = False,
        **kwargs: Dict[str, Any]
    ) -> U: ...
    @classmethod
    def from_dict(cls: Type[U], kvs: Json, *, infer_missing: bool = False) -> U: ...
    def to_dict(self, encode_json: bool = False) -> Dict[str, Json]: ...
    @classmethod
    def schema(
        cls: Type[U],
        *,
        infer_missing: bool = False,
        only: Optional[types.StrSequenceOrSet] = None,
        exclude: types.StrSequenceOrSet = (),
        many: bool = False,
        context: Optional[Dict[str, Any]] = None,
        load_only: types.StrSequenceOrSet = (),
        dump_only: types.StrSequenceOrSet = (),
        partial: bool = False,
        unknown: Optional[str] = None
    ) -> "SchemaType[U]": ...

@overload
def dataclass_json(_cls: Type[T]) -> Type[T]: ...
@overload
def dataclass_json(
    *,
    letter_case: Optional[Union[Callable[[str], str], LetterCase]] = ...,
    undefined: Optional[Union[str, Undefined]] = ...
) -> Callable[[Type[T]], Type[T]]: ...
def dataclass_json(
    _cls: Optional[Type[T]] = None,
    *,
    letter_case: Optional[Union[Callable[[str], str], LetterCase]] = None,
    undefined: Optional[Union[str, Undefined]] = None
) -> Union[Callable[[Type[T]], Type[T]], Type[T]]: ...
