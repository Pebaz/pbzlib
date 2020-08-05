"""
Implementations for several Chemicals that I wished I had on several projects.
"""

from chemical import it

@trait
class first_items(it):
    """
    Returns the first `N` items from an iterator.
    If the provided number of elements is larger than what the iterator contains
    it will only return the number that it actually can provide.

    **Examples**

        :::python

        assert it(range(5)).take(2).collect() == [0, 1]
        assert it(range(5)).rev().take(3).collect() == [4, 3, 2]
    """

    def __init__(self, items, num_items):
        it.__init__(
            self,
            (next(items) for _ in range(num_items)),
            True  # NOTE(pebaz): Must be truthy so `__get_reversed__` is called
        )
        self.num_items = num_items

    def __get_next__(self):
        if self.num_items:
            self.num_items -= 1
            return next(self.items)
        else:
            raise StopIteration()

    def __get_reversed__(self):
        """
        This is overridden so that forward iteration can be lazily computed.
        Reverse iteration has no recourse but to collect first and then iterate.
        """
        res = []
        for _ in range(self.num_items):
            try:
                res.append(next(self))
            except StopIteration:
                break
        return it(reversed(res), self.items)


@trait
def last_items(self, num_items):
    """
    it('asdf12').first_items(30).collect() == ['a', 's', 'd', 'f', '1', '2']
    """
    def lazy(items, count):
        buf = []
        for each in items:
            if len(buf) >= count:
                buf.pop(0)
            buf.append(each)
        return buf
    return it(lazy(self, num_items))
