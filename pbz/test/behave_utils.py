"""
This module contains tools that may come in handy when writing BDD steps.

Parsers for custom types can be added using the `register_custom_type` function.

A list of the built-in types can be found here:
http://behave.github.io/behave.example/datatype/builtin_types.html
"""

from typing import List
import behave

def register_custom_type(pattern: str):
    """
    Maps a given regex to a transformation function that produces an object.

    Behave supports these types:
    http://behave.github.io/behave.example/datatype/builtin_types.html

    However, sometimes the addition of types can reduce complexity when writing
    step implementations.

    # TODO(pebaz): Examples for:
    1. Decorator usage with class
    2. Decorator usage with function
    """
    def wrapper(func):

        # TODO(pebaz): Shorter version. Does it work?
        '''
        behave.register_type(**{func.__name__ : func})

        if isinstance(func, type):
            func_to_return = func

        else:
            def inner(*args, **kwargs):
                return func(*args, **kwargs)
            func_to_return = inner

        func_to_return.pattern = pattern
        return func_to_return
        '''

        # Register custom data type
        if isinstance(func, type):
            behave.register_type(**{func.__name__ : func})
            func.pattern = pattern
            return func

        # Register custom parser function
        else:
            behave.register_type(**{func.__name__ : func})
            def inner(*args, **kwargs):
                return func(*args, **kwargs)
            inner.pattern = pattern
            return inner

    return wrapper


def register_choice_type(**kwargs: List[str]):
    """
    Register one or multiple enum types for use in step implementations.

    Usage:
    >>> register_choice_type(Persons=['Bob', 'Jane'], States=['1', '2', '3'])
    """
    for type_name, choices in kwargs.items():
        behave.register_type(**{type_name : TypeBuilder.make_choice(choices)})


