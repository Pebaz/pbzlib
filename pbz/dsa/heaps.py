from collections import deque


class Heap:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            insert(self.root, value)
    
    def pop(self):
        return delete(self.root)

class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


def show_node(node):
    left = str(node.left.value if node.left else None)
    right = str(node.right.value if node.right else None)
    center = str(node.value)
    ll = len(left)
    lr = len(right)
    lc = len(center)

    print(
        (' ' * ll) + center
    )
    print(
        (' ' * (ll - 1)) + '/' + (' ' * lc) + '\\'
    )
    print(
        left + (' ' * (lc)) + right
    )


def insert(root, value):
    first = find_first(root)
    node = Node(value, parent=first)
    if not first.left:
        first.left = node
    elif not first.right:
        first.right = node
    while node.parent:
        if node.value < node.parent.value:
            # tmp = node.parent
            # swap(node, node.parent)
            # node = tmp
            node.value, node.parent.value = node.parent.value, node.value
            node = node.parent
        else:
            break


def delete(root):
    result = root.value
    first = find_rightmost(root)

    # show_node(node)

    # if node == root:
    #     node.value = None
    #     node.left = None
    #     node.right = None
    #     node.parent = None
    #     return result

    # if first == node:
    #     pass

    if not root.left and not root.right:
        root.value = None
        return result

    if first.right:
        node = first.right
        root.value = node.value
        first.right = None

    else:
        node = first.left
        root.value = node.value
        first.left = None

    if node == root:
        node.value = None
        node.left = None
        node.right = None
        return result
    
    root.value = node.value

    node = root

    # Bubble down
    while True:
        if node.left and node.left.value < node.value:
            node.left.value, node.value = node.value, node.left.value
            # node = node.parent
            # node = node.left.parent
            node = node.left
        elif node.right and node.right.value < node.value:
            node.right.value, node.value = node.value, node.right.value
            # node = node.right.parent
            node = node.right
        else:
            break
    return result


def find_rightmost(node):
    queue = deque([node])
    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return node.parent if node.parent else node


def find_first(node):
    queue = deque([node])
    while queue:
        node = queue.popleft()
        if not node.left or not node.right:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def print_nodes(node):
    queue = deque([node])
    while queue:
        node = queue.popleft()
        print(node.value, end=', ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2, parent=root)
    root.right = Node(3, parent=root)

    # show_node(root)

    # print_nodes(root)
    # insert(root, 0)

    # show_node(root)
    # print()
    # print_nodes(root)

    # show_node(root)
    # print('DELETED:', delete(root))
    # show_node(root)
    # print_nodes(root)

    # print('DELETED:', delete(root))
    # show_node(root)
    # print_nodes(root)

    # print('DELETED:', delete(root))
    # show_node(root)
    # print_nodes(root)

    # Heap sort
    heap = Heap()
    
    nums = [5, 4, 3, 2, 1]
    for i in nums:
        heap.insert(i)
    new = [heap.pop() for i in nums]
    print(nums)
    print(new)
