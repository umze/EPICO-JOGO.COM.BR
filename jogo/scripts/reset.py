import sys
import os

with open('hist.txt', 'r') as arquivo:
    historia = arquivo.read()

os.system(f"cd historias && {historia}")


while True:
    print("Pressione ENTER para reiniciar")
    print("Pressione 2 para fechar o programa")
    resp = input("")
    if resp == "2":
        sys.exit()
    else:
        os.system(f"cd historias && {historia}")