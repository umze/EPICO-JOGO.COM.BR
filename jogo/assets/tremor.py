import ctypes
import time
import random
import threading
import os

os.system("title Carregando - EPICO JOGO.COM.BR")
hwnd = ctypes.windll.user32.GetForegroundWindow()

class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_long),
                ("top", ctypes.c_long),
                ("right", ctypes.c_long),
                ("bottom", ctypes.c_long)]

def mover_janela(hwnd, x, y):
    ctypes.windll.user32.MoveWindow(hwnd, x, y, 1000, 600, True)  

rect = RECT()
ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
x_inicial, y_inicial = rect.left, rect.top

def carregar_frases_txt(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        return arquivo.readlines()

frases = carregar_frases_txt('frases.txt')

def tremer_janela(duracao, passos):
    for passo in range(1, passos + 1):
        intensidade = passo // 100
        deslocamento_x = random.randint(-intensidade, intensidade)
        deslocamento_y = random.randint(-intensidade, intensidade)
        mover_janela(hwnd, x_inicial + deslocamento_x, y_inicial + deslocamento_y)
        time.sleep(duracao / passos)

def exibir_mensagens(frases, duracao, passos):
    contador_mensagem = 0
    for passo in range(1, passos + 1):
        if contador_mensagem < len(frases) and passo % (passos // len(frases)) == 0:
            print(frases[contador_mensagem].strip())
            contador_mensagem += 1
        time.sleep(duracao / passos)

duracao = 8
passos = 3000

thread_tremor = threading.Thread(target=tremer_janela, args=(duracao, passos))
thread_mensagens = threading.Thread(target=exibir_mensagens, args=(frases, duracao, passos))

thread_tremor.start()
thread_mensagens.start()

thread_tremor.join()
thread_mensagens.join()

os.system("title EPICO JOGO.COM.BR")
print("\nPRONTO PARA COMEÇAR!")
input("Pressione ENTER para começar")