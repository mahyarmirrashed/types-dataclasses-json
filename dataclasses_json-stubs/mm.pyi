from typing import Any, Dict, Generic, List, Optional, TypeVar, Union, overload

from marshmallow import Schema

T = TypeVar("T")
JsonInput = Union[str, bytes, bytearray]
EncodedDict = Dict[str, Any]
OneOrMany = Union[T, List[T]]
OneOrManyEncoded = Union[EncodedDict, List[EncodedDict]]

class SchemaF(Schema, Generic[T]):
    """Lift Schema into a type constructor"""

    def __init__(self, *args, **kwargs) -> None: ...
    @overload
    def dump(self, obj: List[T], many: Optional[bool] = None) -> List[EncodedDict]: ...
    @overload
    def dump(self, obj: T, many: Optional[bool] = None) -> EncodedDict: ...
    def dump(self, obj: OneOrMany, many: Optional[bool] = None) -> OneOrManyEncoded: ...
    @overload
    def dumps(
        self, obj: List[T], many: Optional[bool] = None, *args, **kwargs
    ) -> str: ...
    @overload
    def dumps(self, obj: T, many: Optional[bool] = None, *args, **kwargs) -> str: ...
    def dumps(
        self, obj: OneOrMany, many: Optional[bool] = None, *args, **kwargs
    ) -> str: ...
    @overload
    def load(
        self,
        data: List[EncodedDict],
        many: bool = True,
        partial: Optional[bool] = None,
        unknown: Optional[str] = None,
    ) -> List[T]: ...
    @overload
    def load(
        self,
        data: EncodedDict,
        many: Optional[bool] = None,
        partial: Optional[bool] = None,
        unknown: Optional[str] = None,
    ) -> T: ...
    def load(
        self,
        data: OneOrManyEncoded,
        many: Optional[bool] = None,
        partial: Optional[bool] = None,
        unknown: Optional[str] = None,
    ) -> OneOrMany: ...
    @overload
    def loads(
        self,
        json_data: JsonInput,
        many: bool = True,
        partial: Optional[bool] = None,
        unknown: Optional[str] = None,
        **kwargs,
    ) -> List[T]: ...
    @overload
    def loads(
        self,
        json_data: JsonInput,
        many: Optional[bool] = None,
        partial: Optional[bool] = None,
        unknown: Optional[str] = None,
        **kwargs,
    ) -> T: ...
    def loads(
        self,
        json_data: JsonInput,
        many: Optional[bool] = None,
        partial: Optional[bool] = None,
        unknown: Optional[str] = None,
        **kwargs,
    ) -> OneOrMany: ...

SchemaType = SchemaF[T]
