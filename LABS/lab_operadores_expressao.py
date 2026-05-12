''' Sua tarefa é completar o código
 para avaliar a seguinte expressão:

   1/x+1/1/x+1/1/x


O resultado deve ser atribuído a y.
 Tenha cuidado - observe os operadores e mantenha suas prioridades em mente.
  Não hesite em usar quantos parênteses forem necessários.

 Teste seu código com cuidado.

 Ex de entradas: 1, 10, 100, -5
 Ex de saidas: 0.6000000000000001, 0.09901951266867294, 0.009999000199950014, -0.19258202567760344
'''

#entrada 1
x = float(input("Digite o valor para x: "))
y = 1. / (x + 1. / (x + 1. / (x + 1. / x)))

print("y =", y)

#entrada 10
x = float(input("Digite o valor para x: "))
y = 1. / (x + 1. / (x + 1. / (x + 1. / x)))

print("y =", y)

#entrada 100
x = float(input("Digite o valor para x: "))
y = 1. / (x + 1. / (x + 1. / (x + 1. / x)))

print("y =", y)

#entrada -5
x = float(input("Digite o valor para x: "))
y = 1. / (x + 1. / (x + 1. / (x + 1. / x)))

print("y =", y)
