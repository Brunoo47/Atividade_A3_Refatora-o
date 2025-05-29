import unittest
from domain.entidade import Coisa
from repositorio_memoria import RepositorioMemoria
from servico import ServicoCoisa

class TestServicoCoisa(unittest.TestCase):
    def setUp(self):
        self.repositorio = RepositorioMemoria()
        self.servico = ServicoCoisa(self.repositorio)

    def test_criar_coisa(self):
        coisa = self.servico.criar_coisa("Coisa A")
        self.assertEqual(coisa.id, 1)
        self.assertEqual(coisa.nome, "Coisa A")

    def test_listar_coisas(self):
        self.servico.criar_coisa("Coisa A")
        self.servico.criar_coisa("Coisa B")
        lista = self.servico.listar_coisas()
        self.assertEqual(len(lista), 2)

    def test_buscar_coisa(self):
        self.servico.criar_coisa("Coisa A")
        coisa = self.servico.buscar_coisa(1)
        self.assertIsNotNone(coisa)
        self.assertEqual(coisa.nome, "Coisa A")

    def test_atualizar_coisa(self):
        self.servico.criar_coisa("Coisa A")
        coisa = self.servico.atualizar_coisa(1, "Coisa A Atualizada")
        self.assertIsNotNone(coisa)
        self.assertEqual(coisa.nome, "Coisa A Atualizada")

    def test_remover_coisa(self):
        self.servico.criar_coisa("Coisa A")
        coisa = self.servico.remover_coisa(1)
        self.assertIsNotNone(coisa)
        self.assertEqual(coisa.id, 1)
        self.assertEqual(len(self.servico.listar_coisas()), 0)

if __name__ == '__main__':
    unittest.main()
