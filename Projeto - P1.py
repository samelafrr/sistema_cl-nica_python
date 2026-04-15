#FASE 1: USUÁRIO ----------------------------
#BOAS VINDAS NO SISTEMA:
def usuario():
    usuario = str(input("Digite seu usuário: ")).strip()
    print(f"Olá {usuario}, bom trabalho!")
usuario()

#VARIÁVEIS E LISTAS USADAS NO DECORRER DO CÓDIGO:
filmes = []
opcao = -1

filmeEscolhido = []
numeroEscolhido = []
filme = 0

#FASE 2: ÍNDICE -------------------------------
def indice():
    print("""---- LOCADORA ----
[1] Cadastrar item
[2] Listar item
[3] Alugar item
[4] Devolver item
[5] Excluir item
[6] Sair do sistema
    """)

#FASE 3: ESCOLHA
def executar_sistema():
#EXECUÇÃO DO SISTEMA COMPLETO COM CADA OPÇÃO:
    while True:
        indice()

        opcao = int(input("Informe a opção desejada: \n"))

        if opcao == 1:
            print("Forneça as informações abaixo para cadastrar: ")
            titulo = str(input("Título: "))
            if titulo in filmes:
                print("Título já adicionado!")
            else:
                tipo = str(input("Tipo: "))
                status = str(input("Disponível ou alugado? ")).title()
                print("Adicionado com sucesso!")
                filme = [titulo, tipo, status]
                filmes.append(filme)
        if opcao == 2:
            if not filmes:
                print("Nenhum item cadastrado.")
            for i, item in enumerate(filmes, start=1):
                print(i, "-", item[0], "-", item[1], "-", item[2])
                print("-")
        if opcao == 3:
            if not filmes:
                print("Nenhum item cadastrado.")
            for i, item in enumerate(filmes, start=1):
                print(i, "-", item[0], "-", item[1], "-", item[2])
                print("-")
            escolha = int(input("Número do filme que deseja alugar: ")) - 1
            filmeEscolhido = filmes[escolha]
            status = filmeEscolhido[2]
            if status.lower() in ["disponível", "disponivel"]:
                print("Alugado com sucesso!")
                filmeEscolhido[2] = "Alugado"
            else:
                print("Item já está alugado.")
        if opcao == 4:
            for i, item in enumerate(filmes, start=1):
                print(i, "-", item[0], "-", item[1], "-", item[2])
                print("-")
            numero = int(input("Qual o número do item que deseja devolver? ")) - 1
            numeroEscolhido = filmes[numero]
            status = numeroEscolhido[2]
            if status == "Alugado":
                print("Devolvido com sucesso!")
                numeroEscolhido[2] = "Disponível"
            else:
                print("Item não estava alugado!")
        if opcao == 5:
            if not filmes:
                print("Nenhum item para excluir.")
            else:
                for i, item in enumerate(filmes, start=1):
                    print(i, "-", item[0], "-", item[1], "-", item[2])
                    print("-")
                excluir = int(input("Digite o número do item que deseja excluir: ")) - 1
                if 0 <= excluir < len(filmes):
                    filmes.pop(excluir)
                    print("Item removido!")
                else:
                    print("Número inválido!")
        if opcao == 6:
            print("Obrigado por usar o sistema!")
            break
executar_sistema()
#FIM DO CÓDIGO!



