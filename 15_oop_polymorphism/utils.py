from numbers import Number

def validate_number(value):        
    if not isinstance(value, Number):
        raise TypeError(f"value must be number not {type(value)}")