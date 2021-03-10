import struct


class String:
    def __init__(self, length):
        self.length = length
    
    def __str__(self):
        return f'<{self.__class__.__name__}[{self.length}]>'
    
    def __repr__(self):
        return str(self)


class Struct:
    def __init__(self, **kwargs):
        struct_def = self.__annotations__
        valid = {k: kwargs[k] for k in kwargs if k in struct_def}

        for (name, type_), value in zip(struct_def.items(), valid.values()):
            if isinstance(type_, String):
                assert isinstance(value, str), (
                    f'TypeError: {name} should be of type {str}'
                )
                assert len(value) <= type_.length, (
                    f'String too long: {len(value)}/{type_.length}'
                )

                setattr(self, name, value)
                continue

            assert isinstance(value, type_), (
                f'TypeError: {name} should be of type {type_}'
            )
            setattr(self, name, value)
    
    def padded_string(self, name):
        type_, value = self.__annotations__[name], getattr(self, name)

        if len(value) < type_.length:
            value += '\0' * (type_.length - len(value))
        
        return [c.encode('ascii') for c in value]


    def to(self):
        args = []
        for name in self.__annotations__:
            value = getattr(self, name)
            if isinstance(value, str):
                args.extend(self.padded_string(name))
            else:
                args.append(value)

        result = struct.pack(self.get_struct_def(), *args)
        return int.from_bytes(result, byteorder='big')
    
    @classmethod
    def total_bytes(cls):
        return struct.calcsize(cls.get_struct_def())


    @classmethod
    def from_(cls, bytes_):
        int_to_bytes = bytes_.to_bytes(cls.total_bytes(), byteorder='big')
        values = iter(struct.unpack(cls.get_struct_def(), int_to_bytes))
        kwargs = {}

        for name, type_ in cls.__annotations__.items():
            if isinstance(type_, String):
                string = b''.join(next(values) for _ in range(type_.length))
                kwargs[name] = string.decode('ascii').replace('\0', '')
            else:
                kwargs[name] = type_(next(values))

        return cls(**kwargs)
    
    @classmethod
    def get_struct_def(cls):
        types = {
            str: 'c',  # 1-byte
            int: 'i',  # 4-byte
            float: 'f',  # 4-byte
            bool: 'b'  # 1-byte
        }
        struct_def = cls.__annotations__
        result = ''

        for type_ in struct_def.values():
            if isinstance(type_, String):  # Since str is a collection, have to convert
                result += 'c' * type_.length
            
            else:  # Since all other types are single, can lookup directly
                result += types[type_]

        return result
    
    def __str__(self):
        return str({k: getattr(self, k) for k in self.__annotations__})

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    class Planet(Struct):
        name: String(10)
        terrestrial: bool
        orbit_radius_miles_in_millions: float


    a = Planet(
        name='Earth',
        terrestrial=True,
        orbit_radius_miles_in_millions=39.0
    )

    print(a.name)
    print(a.get_struct_def())
    print(a.to())

    planet = Planet.from_(a.to())
    print(planet)

    assert planet.name == 'Earth'
    assert planet.terrestrial == True
    assert planet.orbit_radius_miles_in_millions == 39.0

    class Planet2(Struct):
        name: String(10)
        name2: String(10)
        terrestrial: bool
        orbit_radius_miles_in_millions: float
    
    a = Planet2(
        name='Earth',
        name2='!',
        terrestrial=True,
        orbit_radius_miles_in_millions=39.0
    )

    print(Planet2.from_(a.to()))
