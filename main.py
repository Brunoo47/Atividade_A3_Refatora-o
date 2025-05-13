from infra.repositorio_memoria import RepositorioMemoria
from usecases.servico import ServicoCoisa
from interface_terminal import menu

if __name__ == "__main__":
    repo = RepositorioMemoria()
    servico = ServicoCoisa(repo)
    menu(servico)