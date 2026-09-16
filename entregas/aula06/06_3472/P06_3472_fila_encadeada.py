import P06_3472_pilha_encadeada as pilha

class FilaEncadeada:
    def __init__(self):
        """Inicializa uma fila encadeada vazia baseada em duas pilhas. Complexidade: O(1)."""
        self.outs = pilha.PilhaEncadeada()
        self.ins = pilha.PilhaEncadeada()
        self.size = 0

    def enfileirar(self, item):
        """Insere um item no fim da fila. Complexidade: O(1)."""
        self.ins.push(item)
        self.size += 1

    def _transferir(self):
        """Transfere todos os elementos da pilha de entrada para a pilha de saída. Complexidade: O(N)."""
        while not self.ins.esta_vazia():
            self.outs.push(self.ins.pop())

    def desenfileirar(self):
        """Remove e retorna o item da frente da fila. Levanta IndexError se vazia. Complexidade: O(1) amortizada (caso médio)."""
        if self.size == 0:
            raise IndexError("Fila está vazia")
        
        if self.outs.esta_vazia():
            self._transferir()
            
        self.size -= 1
        return self.outs.pop()

    def frente(self):
        """Retorna o item da frente da fila sem removê-lo. Levanta IndexError se vazia. Complexidade: O(1) amortizada (caso médio)."""
        if self.size == 0:
            raise IndexError("Fila está vazia")
        
        if self.outs.esta_vazia():
            self._transferir()
            
        return self.outs.topo()

    def esta_vazia(self):
        """Retorna True se a fila não contiver elementos, False caso contrário. Complexidade: O(1)."""
        return self.size == 0

    def __len__(self):
        """Retorna a quantidade de elementos armazenados na fila. Complexidade: O(1)."""
        return self.size

    def __repr__(self):
        """Retorna uma representação textual da fila, lida da frente para o fim. Complexidade: O(N)."""
        queue_start = " <- ".join(str(item) for item in self.outs)
        queue_end = ""
        for item in self.ins:
            queue_end = " <- " + str(item) + queue_end

        return queue_start + queue_end if queue_start else queue_end.removeprefix(" <- ")