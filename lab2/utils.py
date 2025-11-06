from numbers import Number
from typing import Any


def validate_number(value: Any) -> None:
    if not isinstance(value, Number):
        raise TypeError(f"Invalid {value!r}! Value must be a number (integer or float), not {type(value).__name__}")
    
def validate_positive(value: Any, name:str) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be a positive number (> 0)") 
    