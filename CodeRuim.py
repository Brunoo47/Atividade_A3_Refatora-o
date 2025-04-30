dados = []

def criar():
    nome = input("Nome da coisa: ")
    id_novo = len(dados) + 1
    dados.append({'id': id_novo, 'nome': nome})
    print(f"Coisa {nome} criada com sucesso!")

def listar():
    for coisa in dados:
        print(f"ID: {coisa['id']}, Nome: {coisa['nome']}")

def buscar():
    id_buscar = int(input("Informe o ID da coisa: "))
    for coisa in dados:
        if coisa['id'] == id_buscar:
            print(f"Coisa encontrada: {coisa['id']} - {coisa['nome']}")
            return
    print("Coisa não encontrada.")

def atualizar():
    id_atualizar = int(input("Informe o ID da coisa para atualizar: "))
    novo_nome = input("Informe o novo nome: ")
    for coisa in dados:
        if coisa['id'] == id_atualizar:
            coisa['nome'] = novo_nome
            print("Coisa atualizada com sucesso!")
            return
    print("Coisa não encontrada.")

def remover():
    id_remover = int(input("Informe o ID da coisa para remover: "))
    for i, coisa in enumerate(dados):
        if coisa['id'] == id_remover:
            dados.pop(i)
            print("Coisa removida com sucesso!")
            return
    print("Coisa não encontrada.")

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Criar coisa")
        print("2. Listar coisas")
        print("3. Buscar coisa")
        print("4. Atualizar coisa")
        print("5. Remover coisa")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            buscar()
        elif opcao == '4':
            atualizar()
        elif opcao == '5':
            remover()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida")

menu()
