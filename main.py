import random
import time

opcoes = ["pedra", "papel", "tesoura"]

#dicionario de emoji
emojis = {
    "pedra": "✊",
    "papel": "✋",
    "tesoura": "✌"
    }

#placar
vitorias = 0
empates  = 0
derrotas = 0

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

    # suspense antes de mostrar resultados
    print("\nJO...")
    time.sleep(0.7)
    print("KEN...")
    time.sleep(0.7)
    print("PO!!!\n")
    time.sleep(0.5)

    #mostrando jogadas
    print(f"\nVocê escolheu: {jogador} {emojis[jogador]}")
    print(f"O computador escolheu: {computador}{emojis[computador]}\n")

    if jogador == computador:
        print("Empate\n")
        empates += 1

    elif (jogador == "pedra" and computador == "tesoura") or\
        (jogador == "papel" and computador == "pedra")    or\
        (jogador == "tesoura" and computador == "papel"):
        print("Você ganhou!\n")
        vitorias += 1

    else:
        print("Você perdeu!\n")
        derrotas +=1

    #contador do pontos
    print(f"VITORIAS: {vitorias} | EMPATES: {empates} | DERROTAS: {derrotas}")
    print("---------------------------------------------")
        