#listas:
# frutas = [ "uva", "kiwi", "maca" ] #0, 1 e 2
# print(frutas)
# print(frutas[0])
# print(frutas[1])
# print(frutas[2])
#len contar caracteres [normal], em listas: conta a qntd de elementos
# frutas.append("banana")
# print(frutas[3])
#append.adicionar no final dps da lista
# frutas = [ ]
# novaFruta = input("Digite uma fruta: ")
# if len(novaFruta) > 0:
#     frutas.append(novaFruta)
#     print("Fruta adicionada com sucesso!")
# else:
#     print("Adicione pelo menos un caractere")

# frutas = []
# frutas = ["daw", ""]
#
# estados = ["SP", "RJ", "PB", "PE", "RN"]
# print(estados[0]) #imprime SP
# estados[0] = "São Paulo"
# print(estados[0])
# print(len(estados))

# notas = [8, 10, 3]
# media = sum(notas) / len(notas)
# novaNota = 5
# notas.append(novaNota)
# print("A menor nota é", min(notas))
# print("A maior nota é", max(notas))
# print(media)

# frutas = [ "uva", "maça", "kiwi", "banana"]
# #item = frutas[0]
# print("Lista de frutas:")
# for item in frutas:
#      print("-", item)
# print("vlw")

#WHILE: serve para fazer menu
#1. lista de frutas 2. adiciona fruta 3. sai do app
# opcao = -1
# frutas = [ ]
# while opcao != 3:
#     print("1) Listar, 2) Adicionar, 3) Sair do app")
#     opcao = int(input("Digite sua opção: "))
#
# print("Obrigado!")

#WHILE
#1. adicionar item 2. listar itens 3. sair do app
# listaDeFeira = [ ]
# novoItem = input("Digite um novo item para sua lista: ")
# if len (novoItem) > 0:
#     listaDeFeira.append(novoItem)
#     print("Item adicionado com sucesso!")
# else:
#     print("Adicione ao menos un caractere!")
# print("-", listaDeFeira)

#LISTA DE FEIRA BONITINHA E PODENDO ADICIONAR ITEM!!!!!!!!!!!
'''
listaDeFeira = ["pão", "queijo", "ovo", "leite"]
novoItem = input("Digite um novo item: ")
listaDeFeira.append(novoItem)
print("Lista de feira: ")
for item in listaDeFeira:
     print("-", item)
len(listaDeFeira)
print("Temos", (len(listaDeFeira), "itens"))
'''

#TESTE: WHILE
#FOR:
'''
opcao = -1
frutas = []
while opcao != 3:
     print("1) Listar frutas 2) Adicionar frutas 3) Sair do app")
     opcao = int(input("Digite sua opção: "))
     if opcao == 1:
         print(frutas)
         for item in frutas:
             print("-", item)
     elif opcao == 2:
         novaFruta = input("Digite a nova fruta: ")
         frutas.append(novaFruta)
         print("Fruta adicionada com sucesso!")
         for item in frutas:
                 print("-", item)
'''
#UPPER = maiusculo
#lower = minusculo
#len = contar
#title = letras iniciais maiusculas
#split = separa
#capitalize = apenas a 1 letra maiuscula
#find = buscar caractere
#strip = separar
#replace = trocar caracteres