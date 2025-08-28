import random

opcoes = ["pedra", "papel", "tesoura"]

print("=== JO-KEM-PO ===")
print("Digite 'sair' para encerrar o jogo.\n")

while True:
    jogador = input("Escolha entre: pedra, papel ou tesoura:  ").lower().strip()

    if jogador == "sair":
        print("Jogo encerrado")
        break

    if jogador not in opcoes:
        print("Escolha inválida\n")
        continue

    computador = random.choice(opcoes)

    print(f"\nVocê escolheu: {jogador}")
    print(f"O computador escolheu: {computador}\n")

    if jogador == computador:
        print("Empate\n")

    elif (jogador == "pedra" and computador == "tesoura") or\
        (jogador == "papel" and computador == "pedra")    or\
        (jogador == "tesoura" and computador == "papel"):
        print("Você ganhou!\n")

    else:
        print("Você perdeu!\n")
        