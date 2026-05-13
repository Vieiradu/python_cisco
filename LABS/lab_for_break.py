secret_word = "chupacabra"

while True:
    word = input("Digite uma palavra: ")
    if word == secret_word:
        break

print("Você saiu do loop")