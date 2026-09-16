class PilhaEncadeada:
    def __init__(self):
        """Inicializa uma pilha encadeada vazia. Complexidade: O(1)."""
        self.top = None
        self.size = 0

    class _No:
        def __init__(self, item, next_node):
            """Inicializa um nó com o item armazenado e a referência para o próximo nó. Complexidade: O(1)."""
            self.item = item
            self.next_node = next_node

    def push(self, item):
        """Insere um item no topo da pilha. Complexidade: O(1)."""
        self.top = self._No(item, self.top)
        self.size += 1

    def pop(self):
        """Remove e retorna o item do topo da pilha. Levanta IndexError se vazia. Complexidade: O(1)."""
        if self.top is None:
            raise IndexError("A pilha está vazia")
        popped = self.top.item
        self.top = self.top.next_node
        self.size -= 1
        return popped

    def topo(self):
        """Retorna o item do topo da pilha sem removê-lo. Levanta IndexError se vazia. Complexidade: O(1)."""
        if self.top is None:
            raise IndexError("A pilha está vazia")
        return self.top.item

    def esta_vazia(self):
        """Retorna True se a pilha não contiver elementos, False caso contrário. Complexidade: O(1)."""
        return self.top is None

    def __iter__(self):
        """Itera sobre os elementos da pilha, do topo para a base. Complexidade: O(1) por passo / O(N) total."""
        current = self.top
        while current is not None:
            yield current.item
            current = current.next_node

    def __len__(self):
        """Retorna a quantidade de elementos armazenados na pilha. Complexidade: O(1)."""
        return self.size

    def __repr__(self):
        """Retorna uma representação textual da pilha, lida do topo para a base. Complexidade: O(N)."""
        string = f" -> ".join(str(item) for item in self)
        return f"| {string} |"