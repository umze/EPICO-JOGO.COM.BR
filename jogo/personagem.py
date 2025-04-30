import curses
import os
import sys

def menu(stdscr):
    os.system("title Personagem - EPICO JOGO.COM.BR")
    curses.curs_set(0)  # Esconder o cursor
    stdscr.clear()
    
    # Definir cores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Azul para o título
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Branco normal
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)  # Vermelho para sair
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Invertido (seleção)
    
    titulo = "SELECIONE O PERSONAGEM"
    opcoes = [
        "Nasci (TUTORIAL)",
        "niveK (EM BREVE)",
        "Renan (EM BREVE)",
        "Ebu (EM BREVE)",
        "Voltar"
    ]
    selecionado = 0

    # Animação de entrada das opções
    for i in range(len(opcoes) + 1):
        stdscr.clear()

        # Exibir o título em azul
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(1, 2, titulo)
        stdscr.attroff(curses.color_pair(1))

        # Exibir opções gradualmente
        for j in range(i):
            cor = curses.color_pair(2)  # Branco por padrão
            if j == len(opcoes) - 1:  # Última opção (sair)
                cor = curses.color_pair(3)

            stdscr.attron(cor)
            stdscr.addstr(j + 3, 2, f"  {opcoes[j]} ")
            stdscr.attroff(cor)

        stdscr.refresh()
        curses.napms(200)  # Pequeno delay para animação (100ms)

    while True:
        stdscr.clear()

        # Exibir o título em azul
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(1, 2, titulo)
        stdscr.attroff(curses.color_pair(1))

        # Exibir opções do menu
        for i, opcao in enumerate(opcoes):
            cor = curses.color_pair(2)  # Branco por padrão
            if i == len(opcoes) - 1:  # Última opção (sair)
                cor = curses.color_pair(3)

            if i == selecionado:
                stdscr.attron(curses.color_pair(4))  # Inverter cores na opção selecionada
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
        elif tecla == 10:  # ENTER
            return selecionado  # Retorna a opção escolhida

def main():
    escolha = curses.wrapper(menu)  # Inicia a interface no terminal
    os.system("cls")
    if escolha == 0:
        curses.endwin()
        os.system("cd scripts && echo nasci.py > hist.txt")
        os.system("cd assets && tremor.py")
        os.system("cd scripts && reset.py")
    elif escolha == 1:
        curses.endwin()
        input("ainda n lançou meu mano")
    elif escolha == 2:
        curses.endwin()
        input("ainda n lançou meu mano")
    elif escolha == 3:
        curses.endwin()
        input("ainda n lançou meu mano")
    elif escolha == 4:
        curses.endwin()
        sys.exit()
        

while True:
    main()
