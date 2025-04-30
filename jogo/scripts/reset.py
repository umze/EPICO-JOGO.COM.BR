import sys
import os

with open('hist.txt', 'r') as arquivo:
    historia = arquivo.read()

os.system(f"cd historias && {historia}")

reset = 0

while reset == 0:
    print("Pressione ENTER para reiniciar")
    print("Pressione 2 para fechar o programa")
    resp = input("")
    if resp == "2":
        sys.exit()
    else:
        reset = 1
        os.system(f"cd historias && {historia}")