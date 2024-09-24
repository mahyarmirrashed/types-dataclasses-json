from enum import Enum
from typing import Any, Callable, Dict, Optional, Type

from dataclasses_json.utils import CatchAllVar
from marshmallow import ValidationError

class UndefinedParameterAction:
    @staticmethod
    def handle_from_dict(obj: Type[Any], kvs: Dict[Any, Any]) -> Dict[str, Any]: ...
    @staticmethod
    def handle_to_dict(obj: Any, kvs: Dict[Any, Any]) -> Dict[Any, Any]: ...
    @staticmethod
    def handle_dump(obj: Any) -> Dict[Any, Any]: ...
    @staticmethod
    def create_init(obj: Any) -> Callable: ...

class Undefined(Enum):
    INCLUDE: Type[UndefinedParameterAction] = ...
    RAISE: Type[UndefinedParameterAction] = ...
    EXCLUDE: Type[UndefinedParameterAction] = ...

class UndefinedParameterError(ValidationError):
    pass

CatchAll = Optional[CatchAllVar]
