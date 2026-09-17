### Escolha do Algoritmo: BFS vs. DFS

Tanto um algoritmo **BFS** quanto um **DFS** seriam apropriados para esse problema, visto que o labirinto gerado é perfeito, isto é, sempre haverá exatamente uma solução para o problema. Se houvesse múltiplas soluções o bfs seria mais apropriado, pois ele sempre retornaria uma solução com o menor número de passos. Como esse não é o caso, o retorno dos dois algoritmos é indistinguível.

Em termos de eficiência temporal, ambos também apresentariam um desempenho similar. O pior caso de ambos seria sempre testar todos os caminhos possíveis da árvore antes de chegar no resultado.

A vantagem que o dfs tem em relação ao bfs nesse caso é que ele é um algoritmo que exige muito menos espaço na memória, já que ele só precisa lembrar um caminho por vez, enquanto que o bfs precisa armazenar todos os estados de cada nível de profundidade. Além disso, o dfs já estava meio pronto por causa da questão 1...