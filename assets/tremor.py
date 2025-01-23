import ctypes
import time
import random
import threading
import os

# Obter o handle da janela ativa (o CMD)
hwnd = ctypes.windll.user32.GetForegroundWindow()

# Definir a estrutura RECT manualmente
class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_long),
                ("top", ctypes.c_long),
                ("right", ctypes.c_long),
                ("bottom", ctypes.c_long)]

# Função para mover a janela
def mover_janela(hwnd, x, y):
    ctypes.windll.user32.MoveWindow(hwnd, x, y, 1000, 600, True)  

# Obter a posição inicial da janela
rect = RECT()
ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
x_inicial, y_inicial = rect.left, rect.top

# Carregar as mensagens do arquivo .txt
def carregar_frases_txt(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        os.system(f"title '{arquivo}'")
        return arquivo.readlines()

# Carregar as frases
frases = carregar_frases_txt('frases.txt')

# Função para tremer a janela
def tremer_janela(duracao, passos):
    for passo in range(1, passos + 1):
        intensidade = passo // 100  # Intensidade aumenta gradualmente
        deslocamento_x = random.randint(-intensidade, intensidade)  # Deslocamento em X
        deslocamento_y = random.randint(-intensidade, intensidade)  # Deslocamento em Y
        mover_janela(hwnd, x_inicial + deslocamento_x, y_inicial + deslocamento_y)
        time.sleep(duracao / passos)

# Função para exibir as mensagens com delay
def exibir_mensagens(frases, duracao, passos):
    contador_mensagem = 0
    for passo in range(1, passos + 1):
        if contador_mensagem < len(frases) and passo % (passos // len(frases)) == 0:
            print(frases[contador_mensagem].strip())
            contador_mensagem += 1
        time.sleep(duracao / passos)

# Configurações
duracao = 8  # Duração total em segundos
passos = 3000  # Número total de movimentos (define a suavidade)

# Criar threads para tremor e exibição de mensagens
thread_tremor = threading.Thread(target=tremer_janela, args=(duracao, passos))
thread_mensagens = threading.Thread(target=exibir_mensagens, args=(frases, duracao, passos))

# Iniciar as threads
thread_tremor.start()
thread_mensagens.start()

# Esperar as threads terminarem
thread_tremor.join()
thread_mensagens.join()

# Mensagem final após o tremor
os.system("title 'Fim - EPICO JOGO.COM.BR'")
print("\nPRONTO PARA COMEÇAR!")
input("Pressione ENTER para começar")
os.system("")