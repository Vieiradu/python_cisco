# # #Como encontrar o maior de dois números

# # #ler dois numeros
# # number1 = int(input("digite o primeiro número: "))
# # number2 = int(input("digite o seguindo número: "))

# # #escolha o mamior numero

# # if number1 > number2:
# #     large_number = number1
# # else:
# #     large_number = number2

# # #imprimir o maior numero
# # print("o maior número é: ", large_number)



# # #Comparativo entre 3 números
# number1 = int(input("digite o primeiro número: "))
# number2 = int(input("digite o seguindo número: "))
# number3 = int(input("digite o terceiro número: "))

# # largest_number = number1

# # if number2 > largest_number:
# #     largest_number = number2

# # if number3 > largest_number:
# #     largest_number = number3

# # print(f"O maior numéro é {largest_number}")


# largest_number = max(number1, number2, number3)
# smaller_number = min(number1, number2, number3)
# print(smaller_number)
'''Spathiphyllum, mais conhecido como um lírio da paz ou planta de vela branca, é um dos mais populares plantas de interior que filtra as toxinas nocivas do ar. Alguns dos efeitos tóxicos que ele neutraliza incluem o benzeno, o formaldeído e a amônia.

Imagine que seu programa de computador adora essas fábricas. Sempre que recebe uma entrada na forma da palavra Spathiphyllum, involuntariamente grita para o console a seguinte string: "Spathiphyllum é a melhor fábrica de todos os tempos!"

Escreva um programa que utilize o conceito de execução condicional, use uma string como entrada e:

imprime a frase "Sim - Spathiphyllum é a melhor
 fábrica de todos os tempos!" para a tela se a sequência inserida for "Spathiphyllum" (maiúscula)
imprime "Não, eu quero um grande Spathiphyllum!" se a sequência inserida for "spathiphyllum" (letra minúscula)
imprime "Spathiphyllum! Not[input]!", Caso contrário. Nota: [input] é a string usada como entrada.
Teste seu código usando os dados que fornecemos para você. E compre um Spathiphyllum também!
'''
# factory = input("Digite o nome da frabrica: ")

# if factory == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif factory == "pelargonium":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathiphyllum! Não", factory + "!")

'''Cenário
Era uma vez uma terra - uma terra de leite e mel, habitada por pessoas felizes e prósperas. As pessoas pagavam impostos, é claro - a felicidade tinha limites. O imposto mais importante, chamado de imposto de renda pessoal (PIT) tinha que ser pago uma vez por ano e foi avaliado usando a seguinte regra:

se a renda do cidadão não era superior a 85.528 talões, o imposto era igual a 18% da renda, menos 556 taller e 2 centavos (isso era o que eles chamavam de isenção de imposto)
se a receita fosse superior a esse valor, o imposto seria igual a 14.839 talões e 2 centavos, mais 32% do excedente em mais de 85.528 taller.
Sua tarefa é escrever uma calculadora de impostos.

Ela deve aceitar um valor de ponto flutuante: a receita.
Em seguida, ele deve imprimir o imposto calculado, arredondado para inteiro. Há uma função chamada round() que fará o arredondamento para você - você a encontrará no código do esqueleto no editor.
Nota: esse país feliz nunca devolveu dinheiro para seus cidadãos. Se o imposto calculado for menor que zero, isso significaria apenas nenhum imposto (o imposto foi igual a zero). Leve isso em consideração durante os cálculos.

Observe o código no editor: ele só lê um valor de entrada e gera um resultado, então você precisa concluí-lo com alguns cálculos inteligentes.
'''

income = float(input("Entre com os rendimentos "))

if income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax = (income - 85528) * 0.32 + 14839.02
 
tax = round(tax, 0)

tax = max(0, tax)

print(
 "A taxa é:", tax, "thalers"
 )
