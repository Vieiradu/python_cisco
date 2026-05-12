'''
Cenário

Sua tarefa é preparar um código simples capaz de avaliar
 a hora de término de um período,
 dado como um número de minutos (pode ser arbitrariamente grande).
  A hora de início é fornecida como um par de horas (0..23)
   e minutos (0..59). O resultado deve ser impresso no console.

Por exemplo, se um evento começa às 12:17 e dura 59 minutos,
 termina às 13:16.

Não se preocupe com imperfeições no código - 
tudo bem se ele aceitar um tempo inválido - 
o mais importante é que o código produz resultados 
válidos para dados de entrada válidos.

Teste seu código com cuidado.
 Dica: usar o operador % pode ser a chave para o sucesso.
'''
#entrada 12, 17 e 59
hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))

# Cálculo dos minutos totais e transporte para as horas
mins = mins + dura
hour = hour + mins // 60
# Ajuste para os intervalos corretos (0-59 para minutos e 0-23 para horas)
mins = mins % 60
hour = hour % 24
# Saída no formato solicitado
print(hour, ":", mins, sep='')

