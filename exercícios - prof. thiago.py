#EXERCÍCIOS DIA 04/03 - Prof. Thiago

#EX - 1
"""
faturamentoInicial = 82500
percentual = 0.12
comissao = (faturamentoInicial * percentual)
faturamentoLiquido = (faturamentoInicial + comissao)
print("O faturamento total é: ", faturamentoLiquido)
"""
import time

#EX - 2
"""
estoqueInicial = 430
vendidos = 125
recebido = 90
totalFinal = (estoqueInicial - vendidos) + recebido
print("O total final foi: ", totalFinal)
"""

#EX - 3
"""
caixas = 2480
palete = 18
paletesCheio = (caixas//palete)
caixasFora = (caixas % palete)
print("Os paletes cheios são:", paletesCheio)
print("As caixas que sobrarão são:", caixasFora)
"""

#EX - 4
'''
faturamento = 28000
custos = 9500
imposto = 0.18
valorImposto = (faturamento * imposto)
lucroLiquido = (faturamento - custos - valorImposto)
margemLucro = (lucroLiquido/faturamento)
resultadoSaudavel = margemLucro >= 0.25
resultadoSaudavel = True
if resultadoSaudavel:
    print("Resultado saudável!")
print(valorImposto)
print(lucroLiquido)
print(margemLucro)
'''


#EX - 5
"""
duracaoEmMeses = 58
anos = (duracaoEmMeses//12)
meses = (duracaoEmMeses % anos)
print("O tempo é", anos, "anos e", meses, "meses.")
"""

#EX - 6
"""
aplicacao = 2000.00
rendimento = 0.05
tempoEmAnos = 4
montante = aplicacao * (1 + rendimento)** tempoEmAnos
montante = round(montante,2)
print("O montante é:", montante)
"""


#EX - 7
"""
usuariosInicial = 150
#crescimento = **2
tempoEmMeses = 6
calculo = usuariosInicial * (2 ** tempoEmMeses)
print("Os usuários finais após 6 meses são:", calculo)
"""

#EX - 8
"""
taxaDeReducao = 0.90
inicio = 1.0
ciclos = 5
capacidadeRestante = inicio * (taxaDeReducao ** ciclos)
capacidadeRestante = round(capacidadeRestante,2)
print(capacidadeRestante)
"""

#EX - 9
"""
lado = 35
area = (lado ** 2)
print('A área do terreno é', area)
"""

#EX - 10
"""
coloniaInicial = 80
horas = 5
totalFinal = (coloniaInicial*(3**horas))
print("O total final é", totalFinal)
"""
#EX - 4 CORREÇÃO
"""
print("-----------------------------------------------------------")
faturamento = 28000
custos = 9500
imposto = 0.18 # 18%
valor_imposto = faturamento * imposto
print(f"Valor imposto: {valor_imposto}") #"F" = format reduzido, relacionado com as chaves!
lucro_liquido =faturamento - custos - valor_imposto
print(f"Lucro líquido: {lucro_liquido}")
margem_lucro = round(lucro_liquido / faturamento,2)
print(f"Margem lucro: {margem_lucro}")
if margem_lucro > 0.25:
    print("Resultado Saudável")
else:
    print("Resultado Não Saudável")
"""

#EXERCÍCIOS DIA 05/03 - Prof. Thiago ----------------------------------------------------
#EX - 1
"""
faturamentoTotal = 78900.00
custoTotal = 41250.00
lucro = (faturamentoTotal - custoTotal)
margemDeLucro =  (lucro / faturamentoTotal)
print(f"O lucro será: R${lucro: .2f}")
print(f"A margem de lucro será:{margemDeLucro: .0%}")
"""

#EX - 2
"""
nome = "aNa cLaRa pErEiRa"
email = "ANACLARA.PEREIRA@OUTLOOK.COM"
novoNome = nome.title()
print(novoNome)
novoEmail = email.lower()
print(novoEmail)
"""

#EX - 3
"""
email = "carla.mendes@techsol.com.br"
novoEmail = email.replace("techsol.com.br", "innovatech.com.br")
print(novoEmail)
"""

#EX - 4
"""
email = "rodrigo.almeida@innovatech.com.br"
posicao = email.find("@")
print(posicao)
usuario = email[:posicao]
print(usuario)
"""

#EX - 5
'''
nome = "fernando henrique costa"
posicao = nome.find("h")
primeiroNome = nome[:posicao]
novoNome = primeiroNome.capitalize()
print(f"Olá, {novoNome}, é uma satisfação ter você conosco!")
'''

#EX - 6
"""
senha = " Seguranca123 "
senhaStrip = senha.strip()
print(senhaStrip)
senhaLen = len(senha)
if senhaLen < 8:
    print("Senha inválida!")
else:
    print("Senha válida!")
"""

#EX - 7
"""
nome = "Gabriel Monteiro Lima"
nomeLen = len(nome)
print(nomeLen)
nomeReplace = nome.replace(" ", "")
nomeReplaceLen = len(nomeReplace)
print(nomeReplaceLen)
"""

#EX - 8
"""
frase = "Nossa empresa é boa e barata!"
fraseReplace = frase.replace("barata", "acessível")
print(fraseReplace)
"""

#EX - 9
"""
email = input("Digite seu email: ")
emailDividido = email.split("@")
usuario = emailDividido[0]
dominio = emailDividido[1]
if dominio == "gmail.com":
    print("Email validado!")
else:
    print("Email invalido!")
"""

#EX - 10
"""
palavra = "python"
invertida = palavra[::-1]
print(invertida)
"""

#EX - 11
"""
codigo = "PROD-2025-XYZ"
codigoDividido = codigo.split("-")
numero = codigoDividido[1]
print(f"O número do produto é {numero}")
"""

#EX - 12
"""
frase = "Programar é transformar o mundo!"
frase = frase.lower()
vogais = "aeiou"
contador = 0

for letra in frase:
    if letra in vogais:
        contador +=1
print("Quantidade de vogais:", contador)
"""

#EX - 13
"""
nome = str("Juliana Alves Costa")
minuscula = nome.lower()
separar = minuscula.split(" ")
username = str(separar[0]+"."+ separar[2])
print("Seu username é", username)
"""

#EX - 14
"""
frase = "Banco de dados é essencial para sistemas!"
if "dados" in frase:
    print("palavra encontrada")
else:
    print("palavra não encontrada")
"""

#EXERCÍCIOS DIA 10/03 - Prof. Thiago ---------------------------------------------------

#EX - 1 -------------------------------------------------------------------------
"""
valor = float(input("Qual valor o valor será aplicado? R$"))
if valor < 2000.00:
    print("Perfil conservador: Indicamos CDB de liquidez diária.")
elif valor > 2000.00 and valor <= 8000.00:
    print("Perfil equilibrado: Indicamos Fundos Multimercado.")
elif valor > 8000.00:
    print("Perfil agressivo: Indicamos Renda Variável.")
"""

#EX - 2 --------------------------------------------------------------------------
"""
masters = ["carla@empresa.com", "roberto@empresa.com", "juliana@empresa.com"]
email = input("Digite seu email: ") .lower().strip()
if email in masters:
    print("Acesso autorizado ao sistema administrativo.")
else:
    print("Usuário sem privilégios de administrador.")
"""

#EX - 3 -----------------------------------------------------------------------------
"""
valor = float(input("Qual o valor da compra? R$"))
if valor >= 600:
    cashback = 0.20
elif valor >= 300 and valor <= 599.99:
    cashback = 0.12
elif valor < 300:
    cashback = 0.05
print(f"Seu cashback será {cashback: .0%}")
valorFinal = valor - (valor * cashback)
print(f"Seu valor final será {valorFinal}")
"""

#EX - 4 --------------------------------------------------------------------------------
"""
metaIndividual = float(input("Qual a sua meta como colaborador? R$"))
faturamentoIndividual = float(input("Qual seu faturamento como colaborador? R$"))
metaGeral = float(input("Qual a meta geral da empresa? R$"))
faturamentoGeral = float(input("Qual o faturamento geral da empresa? R$"))
if metaIndividual == faturamentoIndividual and metaGeral == faturamentoGeral:
    bonus = faturamentoIndividual * 0.25
    print(f"Você recebeu 25% de bônus sobre seu faturamento, seu lucro será {bonus}!")
else:
    print("Infelizmente você não recebeu nenhum bônus!")
"""

#EX - 5 ---------------------------------------------------------------------------
"""
frase = str(input("Qual o seu problema?")).lower()
if "login" in frase:
        print("Chamado direcionado ao suporte de acesso.")
elif "senha" in frase:
    print("Chamado direcionado ao suporte de acesso.")
elif "falha" in frase:
    print("Chamado direcionado ao suporte técnico.")
elif "erro" in frase:
    print("Chamado direcionado ao suporte técnico.")
else:
    print("Chamado direcionado ao atendimento geral.")
"""

#EX - 6 ---------------------------------------------------------------------------
"""
score = float(input("Qual seu score?"))
if score < 400:
    print("Crédito negado!")
elif score >= 400 and score <= 699:
    print("Crédito em análise manual!")
elif score >= 700:
    print("Crédito pré aprovado!")
"""

#EX - 7 -------------------------------------------------------------------------------
"""
peso = float(input("Qual o peso do produto? "))
if peso < 5:
    print("O frete é R$15,00.")
elif peso > 5 and peso < 20:
    print("O frete é R$35,00.")
elif peso > 20:
    print("O frete é R$70,00.")
"""

#EX - 8 -------------------------------------------------------------------------
"""
nome = str(input("Qual o nome do funcionário? "))
faltas = int(input("Qual o número de faltas do mês atual? "))
if faltas <= 2:
    print("Elegível para prêmio de assiduidade.")
elif faltas >= 3 and faltas <= 5:
    print("Atenção à frequência.")
elif faltas > 5:
    print("Não elegível para benefícios.")
"""

#EX - 9 -------------------------------------------------------------------------
"""
temperatura = float(input("Qual a temperatura atual? "))
if temperatura <= 18:
    print("Clima frio.")
elif temperatura > 18 and temperatura < 28:
    print("Clima agradável.")
else:
    print("Clima quente.")
"""

#EX - 10 ---------------------------------------------------------------------
"""
comentario = input("Qual seu comentário a ser analisado? ")
if "excelente" in comentario:
    print("Comentário positivo!")
elif "ótimo" in comentario:
    print("Comentário positivo!")
elif "ruim" in comentario:
    print("Comentário negativo!")
elif "péssimo" in comentario:
    print("Comentário negativo!")
else:
    print("Comentário neutro!")
"""

#EX - 11 ----------------------------------------------------------------------
"""
numero = int(input("Digite um número de 1 a 3: "))
if numero == 1:
    print("Hoje é segunda feira!")
elif numero == 2:
    print("Hoje é terça feira!")
elif numero == 3:
    print("Hoje é quarta feita!")
else:
    print("Dia inválido!")
"""

#EX - 12 ------------------------------------------------------------------------
"""
opcao = -1
opcoes = ["1) A - admin | 2) U - usuário comum | 3) V - visitante"]
while opcao != 3:
    print(opcoes)
    escolha = int(input("Digite sua escolha: "))
    if escolha == 1:
        print("Acesso total liberado!")
    elif escolha == 2:
        print("Acesso parcial liberado!")
    elif escolha == 3:
        print("Acesso somente leitura!")
    else:
        print("Perfil inválido!")
"""
#FIM -------------------------------------------------------------------------------

#EXERCÍCIOS DIA 11/03 - Prof. Thiago

#EX - 1
"""
frutas = ["maçã", "banana", "laranja", "uva"]
print(frutas)
"""
#-----------------------------------------------------------

#EX - 2
"""
frutas = ["maçã", "banana", "laranja", "uva"]
print(frutas[0])
"""
#-----------------------------------------------------

#EX - 3
"""
frutas = ["maçã", "banana", "laranja", "uva"]
frutas.append("manga")
print(frutas)
"""
#----------------------------------------------------

#EX - 4
"""
frutas = ["maçã", "banana", "laranja", "uva"]
frutas.remove("banana")
print(frutas)
"""
#---------------------------------------------------------

#EX - 5
"""
numeros = [1, 2, 3, 4, 5]
numeros = sum(numeros)
print(numeros)
"""
#--------------------------------------

#EX - 6
"""
nomes = ["Ana", "Carlos", "João", "Maria"]
for item in nomes:
    print(item)
"""
#-----------------------------------------

#EX - 7
"""
numeros = []
numeros = input("Digite 5 números: ")
print(numeros)
"""
#------------------------------------------------

#EX - 8
"""
idades = [12, 18, 25, 30, 15]
idadesC = len(idades)
print(idadesC)
"""
#---------------------------------------------

#EXERCÍCIOS DIA 12/03 - Prof. Thiago

#EX - 1
"""
numero = 10
for numero in range (11):
    print(numero)
"""
#------------------------------------

#EX - 2
"""
def pares():
    numero = 20
    for numero in range (20, 0, -2):
        print(numero)
pares()]
"""
#----------------------------------------------

#EX - 3
"""
numeros = 10
for numeros in range(11):
    numeros2 = sum(range(11))
print(numeros2)
"""
#-----------------------------------------

#EX - 4
"""
def tabuada():
    numero = int(input("Digite um número de 1 a 10: "))
    for num in range(1, 11):
        print(f"{numero} x {num} = {numero*num}")
tabuada()
"""
#------------------------------------------------

#EX - 5
"""
def contagem_regressiva():
    for seg in range (10, 0, -1):
        print(seg)
        time.sleep(1)
contagem_regressiva()
"""
#-------------------------------------------

#EX - 6
"""
def potência():
    for numero in range (1,11):
        print(f"{numero} ^ 2 = {numero ** 2}")
potência()
"""
#------------------------------------------

#EX - 7
"""
def numeros_impares():
    for numero in range(1, 21):
        if numero % 2 != 0:
            print(numero)
numeros_impares()
"""
#------------------------------------------

#EX - 8
"""
def pares_50():
    soma = 0
    for numero in range(0, 51, 2):
        if numero % 2 == 0:
            soma += numero
    print(soma)
pares_50()
"""
#-------------------------------------------

#EX - 9
"""
def sequencia_com_while():
    numero = 1
    while numero <= 10:
        print(numero)
        numero = numero + 1
sequencia_com_while()
"""
#-----------------------------------------------

#EX - 10
"""
def contagem_while():
    segundos = 10
    while segundos >= 0:
        time.sleep(1)
        print(segundos)
        segundos = segundos - 1
contagem_while()
"""
#--------------------------------------------------------------

#EX - 11
"""
def soma_com_while():
    soma = 0
    numeros = 1
    while numeros <= 100:
        soma = soma + numeros
        numeros += 1
    print(soma)
soma_com_while()
"""
#---------------------------------------------

#EX - 12

