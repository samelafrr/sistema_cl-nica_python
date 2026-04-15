''''
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
media = (nota1 + nota2) / 2
if media >= 7 and media < 10:
       print("Aprovado!")
elif media < 7:
       print("Reprovado!")
elif media == 10:
       print("Aprovado com excelência!")
'''

#9
'''
numero1 = float(input("Digite o primeiro valor: "))
numero2 = float(input("Digite o segundo valor: "))
if numero1 > numero2:
       print("Numero 1 maior que numero 2")
elif numero1 < numero2:
       print("Numero 1 menor que numero 2")
'''

#10
'''
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valorUm = valor2
valorDois = valor1
print("Os valores invertidos são: valor 1 igual á", valorUm, "valor 2 igual á", valorDois)
'''

#11
'''
salario = float(input("Digite seu salário: R$"))
if salario <= 280:
       ajuste1 = salario * 1.20
       aumento1 = ajuste1 - salario
       print("Seu novo salário reajustado será", ajuste1, "seu ajuste foi de 20% e seu aumento foi de", aumento1)
elif salario > 280 and salario <= 700:
       ajuste2 = salario * 1.15
       aumento2 = ajuste2 - salario
       print("Seu novo salário reajustado será", ajuste2, "seu ajuste foi de 15% e seu aumento foi de", aumento2)
elif salario > 700 and salario <= 1500:
       ajuste3 = salario * 1.10
       aumento3 = ajuste3 - salario
       print("Seu novo salário reajustado será", ajuste3, "seu ajuste foi de 10% e seu aumento foi de", aumento3)
elif salario > 1500:
       ajuste4 = salario * 1.05
       aumento4 = ajuste4 - salario
       print("Seu novo salário reajustado será", ajuste4, "seu ajuste foi de 5% e seu aumento1 foi de", aumento4)
'''

#12
'''
media = float(input("Digite sua média: "))
media = round(media, 1)
if media > 9 and media <= 10:
       print("Conceito A!")
elif media >= 7.5 and media <= 9:
       print("Conceito B!")
elif media >= 6 and media < 7.5:
       print("Conceito C!")
elif media < 6 and media > 4:
       print("Conceito D!")
elif media <= 4 and media >= 0:
       print("Conceito E!")
'''
#lista 2
'''
raio = float(input("Digite o raio: "))
area = 3.14 * raio**2
print("A área é", area)
'''
#Q
'''
# valorHora = float(input("Digite o valor da hora trabalhada: R$"))
# hora = int(input("Digite a quantidade de horas: "))
# calculo = valorHora*hora
# print("Seu salário será", calculo)

'''
#Q
'''
F = float(input("Digite a temperatura em Fahrenheit: "))
C = 5 * (F - 32)/ 9
C = round(C, 1)
print("A temperatua em graus Celsius é", C)

'''

#Q
# altura = float(input("Digite sua altura: "))
# pesoIdeal = (72.7*altura) - 58
# print("Seu peso ideal é", pesoIdeal)

#Q
# altura = float(input("Digite sua altura: "))
# sexo = input("Qual seu sexo? M/F ")
# if sexo == "M":
#     pesoIdeal = (72.7 * altura) - 58
#     print("Seu peso ideal é", pesoIdeal)
# elif sexo == "F":
#     pesoIdeal = (62.1 * altura) - 44.7
#     print("Seu peso ideal é", pesoIdeal)
# print("Obrigado por usar o app!")

#Q
# numero1 = float(input("Digite um número: "))
# numero2 = float(input("Digite outro número: "))
# if numero1 > numero2:
#     print("O número 1 é maior que o número 2!")
# elif numero1 < numero2:
#     print("O número 2 é maior que o número 1!")
# elif numero1 == numero2:
#     print("Os valores são iguais!")

#Q
# num1 = float(input("Digite o primeiro valor: "))
# num2 = float(input("Digite o segundo valor: "))
# num3 = float(input("Digite o terceiro valor: "))
# if num1 > num2 and num1 > num3:
#     print("Número 1 maior que todos")
# if num1 < num2 and num1 < num3:
#     print("Número 1 menor que todos")
# if num2 > num1 and num2 > num3:
#     print("Número 2 maior que todos")
# if num2 < num1 and num2 < num3:
#     print("Número 2 menor que todos")
# if num3 > num1 and num3 > num2:
#     print ("Número 3 maior que todos")
# if num3 < num2 and num3 < num1:
#     print("Número 3 menor que todos")

#Q
# valor1 = float(input('Digite o valor do primeiro produto: R$'))
# valor2 = float(input("Digite o valor do segundo produto: R$"))
# valor3 = float(input("Digite o valor do terceiro produto: R$"))
# if valor1 < valor2 and valor1 < valor3:
#     print("Produto 1: melhor produto para compra!")
# if valor2 < valor1 and valor2 < valor3:
#     print("Produto 2: melhor produto para compra!")
# if valor3 < valor1 and valor3 < valor2:
#     print("Produto 3: melhor produto para compra!")

#Q
# turno = input("Em qual turno você estuda? ")
# if turno == "manhã":
#     print("Bom dia!")
# elif turno == "tarde":
#     print("Boa tarde!")
# elif turno == "noite":
#     print("Boa noite!")

