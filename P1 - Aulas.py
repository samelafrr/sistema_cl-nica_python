#AULA DIA 10/03 - Prof. Thiago -----------------------------------------------------------
#Forma para vários if´s:
"""
numero = 1
match numero:
    case 1:
        print(numero)
    case 2:
        print(numero)
    case _: #é tipo o else
        print(numero)
"""

#AULA DIA 11/03 - Prof. Thiago -----------------------------------------------------------------
""" LISTAS:
numeros = [1, 5, 20, 30]
numeros2 = [2, 6, 7]
#for numero in numeros:
    #print(numeros)
numeros.append(33)
print(numeros)
#for = usado em listas
#numeros.insert(0, 56) #substituir = (posição, número novo)
#numeros.remove(56) #remover
#numeros.pop #remove o último item
#numeros.pop(2) #remove o item na posição dita
#numeros.extend(numeros2) #junta todas as listas
#print(numeros)
"""

#AULA DIA 12/03 - Prof. Thiago -----------------------------------------------------------------
"""FOR, WHILE E RANGE: ESTRUTURAS DE REPETIÇÃO!
FOR = Repete a quantidade de itens que tem na lista #utiliza em uma lista (só tem uma dimensão),
dicionario (vários valores), tupla (usa em gps, latitude e longitude) e (não pode ser alterado), 
conjuntos (insere um novo item em um lugar aleatorio), utiliza o for quanto sei a qntd de itens
que vai repetir! CUIDADO PRA NÃO FICAR EM LOOP: 
COMO USAR: FOR NOME IN (LISTA) 
Range =
While = quando não sei a quantidade de vezes (break para sair do loop) """
"""
numero = 1
while numero < 6:
    print(numero)
    numero = numero + 1
print("Terminou o loop!")"""
""" RANGE = for 20 in range
mostra todos os numeros de 20 até 0 
se quiser em intervalo: for (var) in range (20, 0, -2)
    print = 1
    print = 2
    print = 3
           ... """
#ORGANIZANDO:
"""
numero1 = 10
numero2 = 5
soma = numero1 + numero2

def soma(numero1,numero2):
    print(numero1+numero2)
soma(10,5)
"""

#AULA CURSO EM VÍDEO --------------------------
"""FOR, WHILE E RANGE(intervalo)"""
#FOR como usar:
"""
for (var.) in range(intervalo x,y):
    if tal tal...
    x...
print("fim")
"""
"""
for c in range(0, 6, 2):
    print(c)
print("FIM!")
"""
#SOMA COM FOR
"""
soma = 0
for c in range(0, 3):
    numero = int(input("Digite um número: "))
    soma = soma + numero
print("A soma é:", soma)
"""
#WHILE: não sabe o número final
"""
enquanto não ... = while not:
    tal                 tal comando
tal                 tal comando
"""
"""
c = 1
while c < 10:
    print(c)
    c += 1
print("fim")
"""
