import P06_3472_pilha_encadeada as pilha

class FilaEncadeada:
    def __init__(self):
        self.outs = pilha.PilhaEncadeada()
        self.ins = pilha.PilhaEncadeada()
        self.size = 0

    def enfileirar(self, item):
        self.ins.push(item)
        self.size += 1

    def _transferir(self):
        while not self.ins.esta_vazia():
            self.outs.push(self.ins.pop())

    def desenfileirar(self):
        if self.size == 0:
            raise IndexError("Fila está vazia")
        
        if self.outs.esta_vazia():
            self._transferir()
            
        self.size -= 1
        return self.outs.pop()

    def frente(self):
        if self.size == 0:
            raise IndexError("Fila está vazia")
        
        if self.outs.esta_vazia():
            self._transferir()
            
        return self.outs.topo()

    def esta_vazia(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __repr__(self):
        queue_start = " <- ".join(str(item) for item in self.outs)
        queue_end = ""
        for item in self.ins:
            queue_end = " <- " + str(item) + queue_end

        return queue_start + queue_end if queue_start else queue_end.removeprefix(" <- ") 