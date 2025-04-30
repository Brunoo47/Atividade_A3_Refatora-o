def menu(servico):
    while True:
        print("\n=== MENU CRUD ===")
        print("1. Criar")
        print("2. Listar")
        print("3. Buscar por ID")
        print("4. Atualizar")
        print("5. Remover")
        print("0. Sair")
        opcao = input("Escolha: ")

        match opcao:
            case "1":
                nome = input("Digite o nome: ")
                coisa = servico.criar_coisa(nome)
                print(f"Criado: ID {coisa.id}, Nome: {coisa.nome}")
            case "2":
                coisas = servico.listar_coisas()
                for c in coisas:
                    print(f"{c.id} - {c.nome}")
            case "3":
                id = int(input("ID: "))
                coisa = servico.buscar_coisa(id)
                if coisa:
                    print(f"Encontrado: {coisa.id} - {coisa.nome}")
                else:
                    print("Não encontrado")
            case "4":
                id = int(input("ID: "))
                nome = input("Novo nome: ")
                coisa = servico.atualizar_coisa(id, nome)
                if coisa:
                    print("Atualizado com sucesso")
                else:
                    print("Não encontrado")
            case "5":
                id = int(input("ID: "))
                coisa = servico.remover_coisa(id)
                if coisa:
                    print("Removido com sucesso")
                else:
                    print("Não encontrado")
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opção inválida")
