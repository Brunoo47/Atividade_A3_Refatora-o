from domain.entidade import Coisa

class RepositorioMemoria:
    def __init__(self):
        self.dados = []
        self.id_atual = 1

    def criar(self, nome):
        coisa = Coisa(self.id_atual, nome)
        self.dados.append(coisa)
        self.id_atual += 1
        return coisa

    def listar(self):
        return self.dados

    def buscar(self, id):
        return next((c for c in self.dados if c.id == id), None)

    def atualizar(self, id, nome):
        coisa = self.buscar(id)
        if coisa:
            coisa.nome = nome
        return coisa

    def remover(self, id):
        coisa = self.buscar(id)
        if coisa:
            self.dados.remove(coisa)
        return coisa