"""
A regular Python Dictionary with Set operations for its keys.
"""

class DictSet(dict):
    """
    """

    # TODO(pebaz): Find out how to do this dynamically.
    # for op in 'or and'.split():
    #     operation = f'__{op}__'
    #     self.__dict__[operation] = lambda self, other: self.__set_op__(
    #         other, operation
    #     )

    def __or__(self, other): return self.__set_op__(other, '__or__')
    def __and__(self, other): return self.__set_op__(other, '__and__')
    def __ixor__(self, other): return self.__set_op__(other, '__ixor__')

    def __set_op__(self, other, op):
        """
        Perform the given operation (function) with `self` and `other`.
        """
        return {
            key : self.get(key, other.get(key, None))
            for key in getattr({*self}, op)({*other})
        }


if __name__ == '__main__':
    print(DictSet(name='Pebaz') | DictSet(age=24))
    print(DictSet(name='Pebaz', age=24) | DictSet(age=24))
    print(DictSet(name='Pebaz', age=24, addr='Foo') | DictSet(age=24))
