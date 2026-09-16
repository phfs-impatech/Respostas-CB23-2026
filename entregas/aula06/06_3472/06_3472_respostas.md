### 1. Classe `PilhaEncadeada`

*   **Tempo das Operações Básicas (`push`, `pop`, `topo`, `esta_vazia`, `__len__`):** $O(1)$. 
    *  A classe mantém um ponteiro direto para o `top` (topo) e um contador atualizado `size`, o não precisamos percorrer a estrutura.
*   **Tempo de Iteração e Leitura (`__iter__`, `__repr__`):** $O(N)$.
    *   Para transformar a pilha em texto ou iterar sobre ela, é fisicmente obrigatório visitar cada nó sequencialmente.

---

### 2. Classe `FilaEncadeada`

*   **Tempo de Inserção (`enfileirar`):** $O(1)$.
    *   O elemento é simplesmente empurrado para o topo da pilha de entrada (`ins`).
*   **Tempo de Remoção e Consulta (`desenfileirar`, `frente`):** $O(1)$ Amortizada.
    *    No melhor caso, a pilha de saída (`outs`) já tem elementos, e a remoção custa um imediato $O(1)$. No pior caso, a saída está vazia e custa $O(N)$ para mover tudo. No entanto, como cada elemento inserido na fila só pode ser transferido de uma pilha para a outra uma vez, o custo do $O(N)$ é diluído.
*   **Tempo de Representação (`__repr__`):** $O(N)$.
    *   Ele exige percorrer as duas pilhas inteiras e realizar concatenações de strings no processo.
