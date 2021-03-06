from random import randint

print("[ 1 ] Pedra [ 2 ] Papel [ 3 ] Tesoura")

jogada_usuario = int(input("Digite sua escolha  "))

jogada_maquina = int(randint(1,3))

print(f"Jogada máquina:{jogada_maquina}")

if jogada_usuario == jogada_maquina:
    print(f"jogador: {jogada_usuario}, máquina {jogada_maquina}, portanto, Empate")

elif jogada_usuario == 1 and jogada_maquina == 2:
    print("Maquina venceu")

elif jogada_usuario == 1 and jogada_maquina == 3:
    print("Usuario venceu")

elif jogada_usuario == 2 and jogada_maquina == 1:
    print("Usuario venceu")

elif jogada_usuario == 2 and jogada_maquina == 3:
    print("Maquina venceu")

elif jogada_usuario == 3 and jogada_maquina == 1:
    print("Maquina venceu")

elif jogada_usuario == 3 and jogada_maquina == 2:
    print("Usuario venceu")
    
