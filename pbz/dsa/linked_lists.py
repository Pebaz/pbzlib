class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.length = 2 if head and tail else (1 if head or tail else 0)
        self.head = head
        self.tail = tail

    def extend(self, iterable):
        for i in iterable:
            self.insert(i)

    def insert(self, node):  # O(1) time | O(1) space
        if self.head and self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.length += 1

    def search(self, value):  # O(N) time | O(1) space
        node = self.head
        while node:
            if node.value == value:
                return node
            else:
                node = node.next

    def delete(self, value):  # O(N) time | O(1) space
        removed = None

        if self.length == 0:
            return

        elif self.length == 1:
            if self.head.value == value:
                removed = self.head
                self.head = None
                self.tail = None

        elif self.length > 1:
            if self.head.value == value:
                removed = self.head
                self.head = self.head.next
                self.length -= 1
                return removed

            prev = self.head
            node = self.head.next

            while node:
                if node.value == value:
                    removed = node
                    prev.next = node.next
                    break
                else:
                    prev = node
                    node = node.next

            if removed == self.tail:
                self.tail = prev

        if removed:
            self.length -= 1
            return removed

    def reverse(self):  # O(N) time | O(1) space
        if self.length > 1:
            prev = None
            node = self.head
            self.head, self.tail = self.tail, self.head
            while node:
                save = node.next
                node.next = prev
                prev = node
                node = save
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def __reversed__(self):
        self.reverse()
        node = self.head
        while node:
            yield node
            node = node.next
        self.reverse()

    def __str__(self):
        l = []
        node = self.head
        while node:
            l.append(node.value)
            node = node.next
        return str(l)

    def __repr__(self):
        return str(self)
    
    def __len__(self):
        return self.length
