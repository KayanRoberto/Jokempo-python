import random
import time

opcoes = ["pedra", "papel", "tesoura"]


# Códigos ANSI para cores
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
RESET = "\033[0m"

# dicionário de emoji
emojis = {
    "pedra": "✊",
    "papel": "✋",
    "tesoura": "✌"
}

# placar
vitorias = 0
empates = 0
derrotas = 0

print("=== JO-KEM-PO ===")
print("Digite 'sair' para encerrar o jogo.\n")

while True:
    jogador = input("Escolha entre: pedra, papel ou tesoura: ").lower().strip()

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

    # mostrando jogadas
    print(f"\nVocê escolheu: {jogador} {emojis[jogador]}")
    print(f"O computador escolheu: {computador} {emojis[computador]}\n")

    if jogador == computador:
        print(f"{AMARELO}EMPATE!!! {RESET}\n")
        empates += 1

    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print(f"{VERDE}VOCÊ GANHOU!!! {RESET}\n")
        vitorias += 1

    else:
        print(f"{VERMELHO}VOCÊ PERDEU!!! {RESET}\n")
        derrotas += 1

    # contador de pontos
    print(f"VITÓRIAS: {vitorias} | EMPATES: {empates} | DERROTAS: {derrotas}")
    print("---------------------------------------------")
