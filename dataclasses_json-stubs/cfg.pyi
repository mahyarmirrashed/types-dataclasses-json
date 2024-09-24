from enum import Enum
from typing import Any, Callable, Dict, Optional, TypeVar, Union

from dataclasses_json.undefined import Undefined
from marshmallow.fields import Field

T = TypeVar("T")
U = TypeVar("U")

global_config: _GlobalConfig

class _GlobalConfig: ...

class Exclude:
    ALWAYS: Callable[[], bool]
    NEVER: Callable[[], bool]

class LetterCase(Enum):
    CAMEL: Callable[[str], str]
    KEBAB: Callable[[str], str]
    SNAKE: Callable[[str], str]
    PASCAL: Callable[[str], str]

def config(
    metadata: Optional[Dict[str, Any]] = None,
    *,
    encoder: Optional[Callable[[U], str]] = None,
    decoder: Optional[Callable[[str], U]] = None,
    mm_field: Optional[Field] = None,
    letter_case: Optional[Union[Callable[[str], str], LetterCase]] = None,
    undefined: Optional[Union[str, Undefined]] = None,
    field_name: Optional[str] = None,
    exclude: Optional[Union[Callable[[str, T], bool], Exclude]] = None,
) -> Dict[str, Any]: ...
