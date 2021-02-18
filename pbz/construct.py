"""
https://docs.python.org/3/library/struct.html
https://docs.python.org/3/library/array.html#module-array
"""

# ? Move all globally scoped names into construct()?

import struct

TYPE_MAP = {
    'Pad': 'x',
    'UnsignedInt': 'I'
}


class CharacterString:
    def __getitem__(self, string_length):
        return ('c', string_length)

Char = CharacterString()  # string: Char[100] == ('c', 100)

for type_ in TYPE_MAP:
    globals()[type_] = type(type_, tuple(), {})

class Construct:
    def __init__(self, **kwargs):
        "Construct fields from annotations+kwargs"
        print(self.__class__.__annotations__)
    
    def __len__(self):
        return struct.calcsize(self.__struct_format__)
    
    def pack(self) -> bytes:
        return bytes(len(self))

def construct(class_):
    assert hasattr(class_, '__annotations__')
    fmt = ''
    for field_name, field_type in class_.__annotations__.items():
        fmt += TYPE_MAP[field_type]
    return type(
        class_.__name__,
        (class_, Construct),
        {'__struct_format__': fmt}
    )


if __name__ == '__main__':
    @construct
    class A:
        a: 'pad'
    
    print(A)
    print(dir(A))
    print(A.__struct_format__)
    a = A()
    print(len(a))
    print(a.pack())
