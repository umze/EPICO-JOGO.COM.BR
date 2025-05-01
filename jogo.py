import time
import platform
import subprocess
import os
import sys
import webbrowser
so = platform.system()

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

def caminho_relativo(relativo):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relativo)

if "Darwin" in so or "Linux" in so:
    print("SISTEMA OPERACIONAL NÃO SUPORTADO")
    print("Sinto muito, mas EPICO JOGO.COM.BR não tem suporte ao macOS e Linux. Caso queira jogar, instale Windows no seu computador e inicie o jogo")
    input("Pressione ENTER para fechar o programa")
    exit()

def check_package(package_name):
    print(f"Verificando dependencia: {package_name}")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "show", package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{package_name} está instalado.")
    except subprocess.CalledProcessError:
        print(f"{package_name} não está instalado.")
        print("Deseja instalar a dependencia? Sem ela o jogo não irá funcionar")
        resp = input("[Y/S: Sim | N: Não]: ")
        if resp == "y" or resp == "Y" or resp == "s" or resp == "S":
            print("Instalando dependencia")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            exit()

os.system("cls")
print("AVISO:")
print("Esse jogo utiliza elementos de quebra de quarta parede, ele é capaz de manipular a janela do jogo, criar arquivos, enviar noticações, usar informações do seu computador e abrir arquivos de forma inesperada. Algumas alterações podem não se reverter sozinho. Isso não é um malware ou um programa mal-intenciado")
print("Eu (Leonardo) não irei receber nenhuma infomação sua, seus dados são usados apenas no jogo.")
print("")
print("Pressione CTRL + C para fechar o programa")
print("Pressione ENTER para iniciar a verificação de dependências e iniciar o jogo")
input()
os.system("cls")
check_package("windows-curses")
check_package("win10toast")
check_package("pygame")
import curses
os.system("cls")
print("Jogo feito por")
os.system("title esse cara é bom")
time.sleep(2.0)
os.system("title odranoeL?")
for i in range(100):
    print("um_ze")
    time.sleep(0.01)
os.system("cls")
print("Apresento o INCRÍVEL:", end="\r")
os.system("title MEU DEUSS")
time.sleep(1.0)
os.system("cd jogo/assets/videos && start abertura.mp4")
os.system("cls")

def menu(stdscr):
    os.system("title Menu - EPICO JOGO.COM.BR")
    curses.curs_set(0)
    stdscr.clear()
    
    # Definir cores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Azul para o título
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Branco normal
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)  # Vermelho para sair
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Invertido (seleção)
    
    titulo = "EPICO JOGO.COM.BR"
    opcoes = [
        "Jogar",
        "Ver outros jogos (github.com/umze)",
        "Deixar o desenvolvedor triste porque essa opção serve para fechar o jogo :("
    ]
    selecionado = 0

    for i in range(len(opcoes) + 1):
        stdscr.clear()

        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(1, 2, titulo)
        stdscr.attroff(curses.color_pair(1))

        for j in range(i):
            cor = curses.color_pair(2)
            if j == len(opcoes) - 1:
                cor = curses.color_pair(3)

            stdscr.attron(cor)
            stdscr.addstr(j + 3, 2, f"  {opcoes[j]} ")
            stdscr.attroff(cor)

        stdscr.refresh()
        curses.napms(200)

    while True:
        stdscr.clear()

        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(1, 2, titulo)
        stdscr.attroff(curses.color_pair(1))

        for i, opcao in enumerate(opcoes):
            cor = curses.color_pair(2) 
            if i == len(opcoes) - 1:
                cor = curses.color_pair(3)

            if i == selecionado:
                stdscr.attron(curses.color_pair(4))
                stdscr.addstr(i + 3, 2, f"> {opcao} ")
                stdscr.attroff(curses.color_pair(4))
            else:
                stdscr.attron(cor)
                stdscr.addstr(i + 3, 2, f"  {opcao} ")
                stdscr.attroff(cor)

        stdscr.refresh()
        
        tecla = stdscr.getch()

        if tecla == curses.KEY_UP and selecionado > 0:
            selecionado -= 1
        elif tecla == curses.KEY_DOWN and selecionado < len(opcoes) - 1:
            selecionado += 1
        elif tecla == 10:
            return selecionado

def main():
    escolha = curses.wrapper(menu)
    
    if escolha == 0:
        os.system("cd jogo && personagem.py")
    elif escolha == 1:
        webbrowser.open("https://github.com/umze")
    elif escolha == 2:
        os.system("title :(")
        for i in range(999):
            print(":(")
        os.system('powershell -command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show(\':(\', \'você saiu do jogo\')"')
        curses.endwin()
        sys.exit()

while True:
    main()
