import sys
import time
import os

with open('hist.txt', 'r') as arquivo:
    historia = arquivo.read()

os.system(f"cd historias && {historia}")

reset = 0
def print_animated(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)  # Escreve o caractere sem pular linha
        sys.stdout.flush()      # Força a atualização do output
        time.sleep(delay)       # Pausa por um curto período
    print()  # Pula linha no final

while reset == 0:
    print_animated("Pressione ENTER para reiniciar", delay=0.07)
    print_animated("Pressione 2 para fechar o programa")
    resp = input("")
    if resp == "2":
        exit()
    else:
        reset = 1
        os.system(f"cd historias && {historia}")