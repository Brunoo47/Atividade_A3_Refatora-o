class ServicoCoisa:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def criar_coisa(self, nome):
        return self.repositorio.criar(nome)

    def listar_coisas(self):
        return self.repositorio.listar()

    def buscar_coisa(self, id):
        return self.repositorio.buscar(id)

    def atualizar_coisa(self, id, nome):
        return self.repositorio.atualizar(id, nome)

    def remover_coisa(self, id):
        return self.repositorio.remover(id)