
class StackUnderflowException(Exception):
    "Nothing to pop"


class StackOverflowException(Exception):
    "No more room on stack"


class Stack:
    def __init__(self, stack_size: int):
        self.items = [None] * stack_size
        self.capacity = stack_size
        self.length = 0
    
    def insert(self, item):
        if len(self) >= self.capacity:
            raise StackOverflowException(str(self.capacity))

        self.items[self.length] = item
        self.length += 1
    
    def remove(self):
        if not self.length:
            raise StackUnderflowException()

        self.length -= 1
        item = self.items[self.length]
        self.items[self.length] = None
        return item
    
    def __len__(self):
        return self.length

    def __str__(self):
        result = []
        for i in self.items:
            if i is None:
                break
            else:
                result.append(i)
        stringified = str(result)
        return stringified[:-1] + f'; {self.length}/{self.capacity}]'
    
    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    stack = Stack(3)
    stack.insert(1)
    stack.insert(2)
    stack.insert(3)
    assert len(stack) == 3
    assert stack.remove() == 3
    assert stack.remove() == 2
    assert stack.remove() == 1

    stack = Stack(300)
    for i in range(10):
        stack.insert(i)
    print(stack)

