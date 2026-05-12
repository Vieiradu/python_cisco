'''
A diferença semática é mais importante:
 quando a condição é atendida, se executa suas instruções apenas uma vez;
  Enquanto repete a execução, enquanto a condição avalia como True.

Nota: todas as regras relacionadas à indentação também são aplicáveis aqui.
Mostraremos isso em breve.
'''
# while conditional_expression:
#     instruction_one
#     instruction_two
#     instruction_three
#     :
#     :
#     instruction_n

'''
Agora é importante lembrar que:

se você quiser executar mais de uma instrução dentro de um loop while,
 você deve (como no if) recuar todas as instruções da mesma maneira;
uma instrução ou um conjunto de instruções executadas dentro do loop while
 é chamado de corpo do loop;
se a condição for False (igual a zero) quando for testada pela primeira vez,
 o corpo não será executado uma única vez(
  observe a analogia de não ter que fazer nada se não houver nada a fazer
  );
o corpo deve ser capaz de alterar o valor da condição, porque se a condição for True no início,
 o corpo poderá ser executado continuamente até o infinito (
 observe que fazer algo geralmente diminui o número de coisas a fazer
 ).
'''
#Aqui está um exemplo de um loop que não é capaz de concluir sua execução:

# while True:
#     print("Estoiu dentro do Loop")

#Esse loop irá exebir infinitamente o print.
'''
Analise o programa com cuidado. Veja onde o loop começa (linha 8).
 Localize o corpo do loop e descubra como o corpo sai :
'''
# Armazene o maior número atual aqui.
largest_number = -999999999
 
# Insira o primeiro valor.
number = int(input("Digite um número ou digite -1 para parar: "))
 
# Se o número não for igual a -1, continue.
while number != -1:
    # O número é maior que o maior_número?
    if number > largest_number:
        # Sim, atualize o maior_número.
        largest_number = number
    # Insira o próximo número.
    number = int(input("Digite um número ou digite -1 para parar: "))
 
# Imprima o maior número.
print("O maior número é:", largest_number)

#Usando uma variável counter para sair do loop
counter = 5
while counter != 0:
    print("Dentro do laço.", counter)
    counter -= 1
print("Fora do circuito.", counter)
 
#ou de forma mais limpa:

counter = 5
while counter:
    print("Dentro do laço.", counter)
    counter -= 1
print("Fora do circuito.", counter)

#É mais compacto do que anteriormente? Um pouco.
# É mais legível? Isso é discutível.