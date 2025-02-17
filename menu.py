import os
import platform
import sys
import subprocess
import time
import webbrowser
import pyautogui

color = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cian": "\033[36m",
    "white": "\033[97m",
    "gray": "\033[37m",
    "bold": "\033[1m",
    "underlined": "\033[4m",
    "reset": "\033[0m"  # Para resetar a cor
}

so = platform.system()

if "Darwin" in so or "Linux" in so:
    print("SISTEMA OPERACIONAL NÃO SUPORTADO")
    print("Sinto muito, mas EPICO JOGO.COM.BR não tem suporte ao macOS e Linux. Caso queira jogar, instale Windows no seu computador e inicie o jogo")
    input("Pressione ENTER para fechar o programa")
    exit()

# Verificador de dependencia
def check_package(package_name):
    print(f"Verificando dependencia: {package_name}")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "show", package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{package_name} está instalado.")
    except subprocess.CalledProcessError:
        print(f"{package_name} não está instalado.")
        print("Deseja instalar a dependencia? Sem ela o jogo não irá funcionar")
        resp = input("[Y: Sim | N: Não]: ")
        if resp == "y" or resp == "y":
            os.system(f"pip install {package_name}")
        else:
            exit()

def print_animated(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)  # Escreve o caractere sem pular linha
        sys.stdout.flush()      # Força a atualização do output
        time.sleep(delay)       # Pausa por um curto período
    print()  # Pula linha no final

check_package("pyautogui")

os.system("cls")
print("Dos mesmos criadores de")
os.system("title é deles msm")
time.sleep(2.0)
os.system("title JOGO EPICOOOOOO.COM")
for i in range(100):
    print("EPICO JOGO.COM")
    time.sleep(0.01)

os.system("cls")
print("Apresentamos o INCRÍVEL:", end="\r")
os.system("title MEU DEUSS")
time.sleep(1.0)
os.system("cd assets/videos && abertura.mp4")

while True:
    os.system("cls")
    print(f"{color['cian']}EPICO JOGO.COM.BR         {color['reset']}")
    os.system("title Menu - EPICO JOGO.COM.BR")
    time.sleep(1)
    print("-----------------")
    time.sleep(0.2)
    print("1: Jogar")
    time.sleep(0.2)
    print("2: Como jogar")
    time.sleep(0.2)
    print("3: Ver outros jogos (navegador)")
    time.sleep(0.2)
    print("4: Deixar o desenvolvedor triste porque essa opção serve para fechar o jogo :(")
    opcao = input("R: ")

    if opcao == "1":
        escolhido = 1
        while escolhido == 1:
            os.system("title Personagem - EPICO JOGO.COM.BR")
            os.system("cls")
            print(f"{color['cian']}Selecione o personagem:{color['reset']}")
            time.sleep(1)
            print("-----------------------")
            time.sleep(0.2)
            print("1: Nasci (TUTORIAL)")
            time.sleep(0.2)
            print("2: niveK (EM BREVE)")
            time.sleep(0.2)
            print("3: Renan (EM BREVE)")
            time.sleep(0.2)
            print("5: Voltar")
            personagem = input("R: ")
            
            if personagem == "1":
                os.system("cd scripts && echo nasci.py > hist.txt")
                os.system("cd assets && tremor.py")
                os.system("cd scripts && reset.py")
                escolhido = 2
            elif personagem == "5":
                escolhido = 2
            else:
                print("Resposta inválida")
                time.sleep(1)
    if opcao == "2":
        os.system("cls")
        os.system("title Tutorial - EPICO JOGO.COM.BR")
        print("")
        print(f"Como jogar {color['cian']}EPICO JOGO.COM.BR{color['reset']}")
        print("")
        input("Pressione ENTER para avançar cada frase")
        input("O jogo irá avançar algumas frases sozinho.")
        input(f"""Quando o jogo falar para você escrever alguma coisa, escreva após "{color['red']}R:{color['reset']}". """)
        input("O jogo foi feito para ser jogado em modo janela (sem maximizar ou tela cheia).")
        input("Algumas partes do jogo requer que você faça tarefas fora do jogo para continuar.")
        input("acabou ;------;")
    if opcao == "3":
        webbrowser.open("https://github.com/umze")
    if opcao == "4":
        os.system("title :(")
        for i in range(999):
            print(":(")
        os.system('powershell -command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show(\':(\', \'você saiu do jogo\')"')
        exit()
