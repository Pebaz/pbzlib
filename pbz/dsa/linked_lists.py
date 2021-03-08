class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)


class LinkedList:
    """
    Singly Linked List.

    NOTE: Does not even touch Node.prev as that is DoublelyLinkedList's purpose.
    """
    def __init__(self, head=None, tail=None):
        self.length = sum((bool(head), bool(tail)))
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

    def remove(self, value):  # O(N) time | O(1) space
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



class DoublelyLinkedList:
    def __init__(self, head=None, tail=None):
        self.length = sum((bool(head), bool(tail)))
        self.head = head
        self.tail = tail
    
    def insert(self, node):
        if self.tail:  # At least 1 node
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        else:  # 0 nodes in list
            self.head = node
            self.tail = node

        self.length += 1
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def __reversed__(self):
        node = self.tail
        while node:
            yield node
            node = node.prev

    def search(self, value):
        for node in self:
            if node.value == value:
                return node
    
    def extend(self, nodes):
        for n in nodes:
            self.insert(n)
    
    def __str__(self):
        return str([n for n in self])

    def __repr__(self):
        return str(self)
    
    def __len__(self):
        return self.length

    def remove(self, value):
        if not len(self):
            return
        
        elif len(self) == 1:
            if self.head.value == value:
                tmp = self.head
                self.head = None
                self.tail = None
                self.length -= 1
                return tmp
        
        else:  # Find & remove node
            node = self.head
            while node:
                print(node)
                if node.value == value:
                    node.prev.next = node.next

                    if node is self.tail:
                        self.tail = node.prev
                    else:
                        node.next.prev = node.prev

                    self.length -= 1
                    return node

                node = node.next


