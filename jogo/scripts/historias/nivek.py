import time
import sys
import os
import platform
from win10toast import ToastNotifier
import random
import string

toaster = ToastNotifier()
os.system("title niveK - EPICO JOGO.COM.BR")
node = platform.node()

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
    "reset": "\033[0m"
}


def gerar_caracteres_aleatorios(tamanho):
    todos = string.ascii_letters + string.digits + string.punctuation + ' ' * 5
    return ''.join(random.choice(todos) for _ in range(tamanho))

def desintegrar_nivek():
    frase_original = "niveK: Eu acho que estou sendo desintegrado."
    tamanho = len(frase_original)

    print(frase_original)
    time.sleep(2)  # Espera dramática

    velocidade = 0.1  # Começa mais lenta
    velocidade_minima = 0.005
    aceleracao = 0.95  # Quanto menor, mais rápido acelera

    for _ in range(60):
        texto_bugado = gerar_caracteres_aleatorios(tamanho)
        print(texto_bugado)
        time.sleep(velocidade)
        velocidade = max(velocidade * aceleracao, velocidade_minima)

    # Fim com desaparecimento dramático
    for i in range(tamanho, 0, -2):
        print(gerar_caracteres_aleatorios(i))
        time.sleep(0.01)




def print_spam(frase, letra_spam, delay=0.1, spam_time=2):
    print(frase, end='', flush=True)
    time.sleep(1)
    
    start_time = time.time()
    while time.time() - start_time < spam_time:
        sys.stdout.write(letra_spam)
        sys.stdout.flush()
        time.sleep(delay) 

def finaldesintegrado(titulo, descricao):
    os.system("cls")
    time.sleep(1)
    print_animated(f"FINAL: {titulo}", delay=0.09)
    time.sleep(0.5)
    print_animated(descricao, delay=0.09)
    print("-----------------------------------------")
    exit()

def final(titulo, descricao):
    time.sleep(3.0)
    os.system("cls")
    time.sleep(1)
    print_animated(f"FINAL: {titulo}", delay=0.09)
    time.sleep(0.5)
    print_animated(descricao, delay=0.09)
    print("-----------------------------------------")
    exit()

def finalHist(titulo, descricao):
    time.sleep(3.0)
    os.system("cls")
    time.sleep(1)
    print_animated(f"FINAL: {titulo}", delay=0.09)
    time.sleep(0.5)
    print_animated(descricao, delay=0.09)
    print("")
    print_animated("Parabéns, você concluiu a história principal do niveK!")
    print_animated(f"Obrigado por jogar {node} :)")
    print("-----------------------------------------")
    exit()



def print_animated(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

os.system("cls")
print("Vamos começar uma nova história, onde tudo começou.")
time.sleep(1.5)
print()
time.sleep(1.5)
print_animated("Um dia, niveK estava explorando uma floresta", delay=0.09)
print_animated("Até que achou a INCRÍVEL", delay=0.05)
os.system("cd .. && cd .. && cd assets && uva.png")
print_animated("uva", delay=0.05)
time.sleep(1.0)
input("Pressione ENTER para continuar")
os.system("cls")
print_animated("niveK queria muito essas uvas", delay=0.09)
print_animated("""Pareciam muito boas para "comi" """)
print_animated("Mas o problema é que elas estão num galho de uma árvore bem grande")
time.sleep(1.0)
os.system("cls")
print_animated("E agora? O que você irá fazer?", delay=0.05)
print_animated("1: Pegar uma escada", delay=0.01)
print_animated("2: Ligar para a polícia", delay=0.01)
print_animated("3: Coletar um trampolim", delay=0.01)
print_animated("4: Serra Elétrica de Última Gen. Feita a Laser ", delay=0.01)
print_animated("5: Desistir da missão", delay=0.01)
print()
arvore = input("R: ")
os.system("cls")
if arvore == "1":
    print_animated("Você pega do seu inventário uma escada.", delay=0.09)
    print_animated("Mas percebe uma grande problema", delay=0.09)
    time.sleep(1.0)
    print_animated("A escada não chega nas uvas", delay=0.05)
    print_animated("Então você sobe na escada e pula", delay=0.05)
    time.sleep(3.0)
    final(f"AI, ESSA DOEU!", f"Você pulou da escada, por que {node}?")
if arvore == "2":
    print("Você liga para a polícia.")
    print("")
    input("Pressione ENTER para avançar as falas")
    time.sleep(3.0)
    input("Polícia: Alô?")
    input("niveK: Oi, eu... queria pegar uma uva mas ela está em cima de uma árvore")
    input("Polícia: Pera.")
    input("Polícia: Você ligou para a polícia para isso?")
    for i in range(4):
        print("\rniveK: É" + "." * (i % 3 + 1), end='', flush=True)
        time.sleep(0.7)
    print("")
    print("Polícia: Mas que MERDA")
    time.sleep(0.5)
    input("você me ligou por conta de uma uva, meu deus")
    input("niveK: Eu amo uvas, mas elas estão sendo sequestradas pela árvore, por isso que eu liguei")
    print("Polícia: Eu me demito, meu deus")
    time.sleep(1.0)
    print("Polícia: *sai da cadeira*")
    time.sleep(1.0)
    print_spam("Polícia: *grita na sala* PIOR EMPREGO DE TODOS", "S", delay=0.01, spam_time=1.5)
    final("FUI PRESO!", "Ligação rastreada slk, foi preso em 4K")
elif arvore == "3":
    final("VOCÊ NÃO TEM UM TRAMPOLIM", f"Tá achando que isso é um jogo mesmo {node}? Pois não, você não vai tirar um trampolim do bolso")
elif arvore == "4":
    print_animated("Você remove do seu inventário uma serra elétrica de última geração com laser.")
    time.sleep(1.0)
elif arvore == "5":
    final("DESISTO!", "Não vai pegar uva porque não quer né?")
else:
    final("DESISTO 2!", "Desisto")
print_animated("Ao cortar a árvore")
print_animated("A árvore grita de dor")
print_spam("Árvore: AI QUE DOR", "R", 0.01, 1.3)
os.system("cls")
print("Você foi preso 💀")
time.sleep(3)
input("Pressione ENTER para continuar")
os.system("cls")
print_animated("""Na prisão você recebe uma ligação de uma tal de "Mafê".""")
print_animated("mas quem é ela?")
time.sleep(1)
print_animated("""Você atende o telefone, e ela começa a cantar uma música chamada "Jogos divertidos" de Pedro Neto.""", delay=0.01)
print("niveK: Que música é essa?")
time.sleep(2)
print("Você desliga imediatamente o telefone.")
time.sleep(3)
os.system("cls")
os.system('powershell -command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show(\'Por favor.\', \'niveK\')"')
os.system("cls")
os.system('powershell -command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show(\'Me tire desse lugar\', \'niveK\')"')
os.system("cls")
os.system('powershell -command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show(\'Eu...\', \'niveK\')"')
os.system("cls")
os.system('powershell -command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show(\'Só sou um ursinho.\', \'niveK\')"')
os.system("cls")
os.system('powershell -command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show(\'Me ajude, por favor.\', \'niveK\')"')
os.system("cls")
os.system("cd quest && porfavor.txt")
toaster.show_toast("niveK", "Boa sorte!")

caminho_da_pasta = os.path.dirname(os.path.abspath(__file__))
appdata_path = os.getenv("APPDATA")
ondeestou = os.path.join(appdata_path, "EPICO JOGO.COM.BR", "ondeestouinstalado.txt")
terminei = os.path.join(appdata_path, "EPICO JOGO.COM.BR", "termineionivek.txt")
os.makedirs(os.path.dirname(ondeestou), exist_ok=True)
os.makedirs(os.path.dirname(terminei), exist_ok=True)
fiz = "nah"
with open(terminei, "w") as f:
    f.write("nah")

with open(ondeestou, "w") as f:
    f.write(caminho_da_pasta) 
os.system("doc.py")
os.system("cls")
input("Leias os arquivos corretamente, cada um tem uma pista de onde fica eles")

appdata_path = os.getenv("APPDATA")
terminei = os.path.join(appdata_path, "EPICO JOGO.COM.BR", "termineionivek.txt")
os.makedirs(os.path.dirname(terminei), exist_ok=True)

with open(terminei, "r") as f:
    fiz = f.read()
os.system("cls")
if fiz == "yeah":
    print("niveK: Mano você realmente conseguiu, parabéns cara.")
    time.sleep(3)
    print("niveK: Eu penso o quão difícil deve ser isso, parabéns")
    time.sleep(3)
    finalHist("TO FORAAA", "Você conseguiu libertar niveK de sua prisão, agora ele conseguirá comer mais uvas")
else:
    print("niveK: Mano, o que está acontecendo comigo?")
    time.sleep(3)
    desintegrar_nivek()
    finaldesintegrado("", "")