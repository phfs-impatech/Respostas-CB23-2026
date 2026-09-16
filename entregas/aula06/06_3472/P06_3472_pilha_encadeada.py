class PilhaEncadeada:
    def __init__(self):
        self.top = None
        self.size = 0

    class _No:
        def __init__(self, item, next_node):
            self.item = item
            self.next_node = next_node

    def push(self, item):
        self.top = self._No(item, self.top)
        self.size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("A pilha está vazia")
        popped = self.top.item
        self.top = self.top.next_node
        self.size -= 1
        return popped

    def topo(self):
        if self.top is None:
            raise IndexError("A pilha está vazia")
        return self.top.item

    def esta_vazia(self):
        return self.top is None

    def __iter__(self):
        current = self.top
        while current is not None:
            yield current.item
            current = current.next_node

    def __len__(self):
        return self.size

    def __repr__(self):
        string = f" -> ".join(str(item) for item in self)
        return f"| {string} |"