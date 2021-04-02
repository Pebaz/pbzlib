

class Node:
    def __init__(self, value):
        self.value = value
        self.links = []


class Trie:
    def __init__(self):
        self.root = None

    def insert(self, word):
        node = self.root
        prev = ''

        for c in word.lower():
            if not self.root:
                self.root = Node(c)
                node = self.root
                prev = c
                continue

            # Only add a repeated char if we've already encountered it
            if node.value == c and prev != c:
                prev = c
                continue
    
            prev = c

            for n in node.links:
                if n.value == c:
                    node = n
                    break
            else:
                new = Node(c)
                node.links.append(new)
                node = new
    
    def show(self, node=None, indent=0):
        node = node or self.root
        if not node:
            return
        print('  ' * indent, node.value)
        for n in node.links:
            self.show(n, indent + 1)


if __name__ == '__main__':
    trie = Trie()
    trie.insert('Hello')
    trie.insert('Helium')
    trie.show()
