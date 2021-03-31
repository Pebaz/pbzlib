from collections import deque


class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


def show_node(node):
    left = str(node.left.value)
    right = str(node.right.value)
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

    show_node(root)

    print_nodes(root)
    insert(root, 0)

    show_node(root)
    print()
    print_nodes(root)

