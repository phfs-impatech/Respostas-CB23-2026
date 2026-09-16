import unittest
from P06_3472_pilha_encadeada import PilhaEncadeada
from P06_3472_fila_encadeada import FilaEncadeada

class TestPilhaEncadeada(unittest.TestCase):
    def setUp(self):
        """Inicializa uma nova pilha vazia antes de cada teste."""
        self.pilha = PilhaEncadeada()

    def test_ordem_lifo(self):
        """Teste de ordem LIFO em sequência de push/pop."""
        self.pilha.push(1)
        self.pilha.push(2)
        self.pilha.push(3)
        self.assertEqual(self.pilha.pop(), 3)
        self.assertEqual(self.pilha.pop(), 2)
        self.assertEqual(self.pilha.pop(), 1)

    def test_excecoes_pilha_vazia(self):
        """Teste de pop e topo em pilha vazia."""
        with self.assertRaises(IndexError):
            self.pilha.pop()
        with self.assertRaises(IndexError):
            self.pilha.topo()

    def test_coerencia_len(self):
        """Teste de coerência de len após inserções e remoções."""
        self.assertEqual(len(self.pilha), 0)
        self.pilha.push("A")
        self.assertEqual(len(self.pilha), 1)
        self.pilha.push("B")
        self.assertEqual(len(self.pilha), 2)
        self.pilha.pop()
        self.assertEqual(len(self.pilha), 1)

    def test_alternancia_operacoes(self):
        """Teste de alternância de operações."""
        self.pilha.push(10)
        self.assertEqual(self.pilha.pop(), 10)
        self.pilha.push(20)
        self.pilha.push(30)
        self.assertEqual(self.pilha.pop(), 30)
        self.assertEqual(self.pilha.topo(), 20)

    def test_tipos_diferentes(self):
        """Teste de armazenamento de itens de tipos diferentes, incluindo valores repetidos e None."""
        self.pilha.push(None)
        self.pilha.push("texto")
        self.pilha.push(3.14)
        self.pilha.push(100)
        self.pilha.push(100)
        
        self.assertEqual(self.pilha.pop(), 100)
        self.assertEqual(self.pilha.pop(), 100)
        self.assertEqual(self.pilha.pop(), 3.14)
        self.assertEqual(self.pilha.pop(), "texto")
        self.assertIsNone(self.pilha.pop())


class TestFilaEncadeada(unittest.TestCase):
    def setUp(self):
        """Inicializa uma nova fila vazia antes de cada teste."""
        self.fila = FilaEncadeada()

    def test_ordem_fifo(self):
        """Teste de ordem FIFO."""
        self.fila.enfileirar("A")
        self.fila.enfileirar("B")
        self.fila.enfileirar("C")
        self.assertEqual(self.fila.desenfileirar(), "A")
        self.assertEqual(self.fila.desenfileirar(), "B")
        self.assertEqual(self.fila.desenfileirar(), "C")

    def test_intercalacao_operacoes(self):
        """Teste de intercalação de enfileirar e desenfileirar."""
        self.fila.enfileirar(1)
        self.fila.enfileirar(2)
        self.assertEqual(self.fila.desenfileirar(), 1)
        self.fila.enfileirar(3)
        self.assertEqual(self.fila.desenfileirar(), 2)
        self.assertEqual(self.fila.frente(), 3)
        self.assertEqual(self.fila.desenfileirar(), 3)

    def test_esvaziar_e_reutilizar(self):
        """Teste de esvaziar e voltar a usar a mesma instância."""
        self.fila.enfileirar(99)
        self.assertEqual(self.fila.desenfileirar(), 99)
        self.assertTrue(self.fila.esta_vazia())
        self.fila.enfileirar(42)
        self.assertEqual(self.fila.frente(), 42)
        self.assertEqual(len(self.fila), 1)

    def test_excecoes_fila_vazia(self):
        """Teste de desenfileirar e frente em fila vazia."""
        with self.assertRaises(IndexError):
            self.fila.desenfileirar()
        with self.assertRaises(IndexError):
            self.fila.frente()

    def test_coerencia_len(self):
        """Teste de coerência de len."""
        self.assertEqual(len(self.fila), 0)
        self.fila.enfileirar(10)
        self.assertEqual(len(self.fila), 1)
        self.fila.enfileirar(20)
        self.assertEqual(len(self.fila), 2)
        self.fila.desenfileirar()
        self.assertEqual(len(self.fila), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)