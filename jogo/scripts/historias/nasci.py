import random
import time
import sys
import os
import platform
import ctypes
from pathlib import Path

os.system("title Nasci - EPICO JOGO.COM.BR")
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

class GUID(ctypes.Structure):
    _fields_ = [
        ("Data1", ctypes.c_ulong),
        ("Data2", ctypes.c_ushort),
        ("Data3", ctypes.c_ushort),
        ("Data4", ctypes.c_ubyte * 8)
    ]

def string_to_guid(guid_string):
    guid = GUID()
    ctypes.windll.ole32.CLSIDFromString(ctypes.c_wchar_p(guid_string), ctypes.byref(guid))
    return guid

def get_known_folder(folder_id_str):
    folder_id = string_to_guid(folder_id_str)

    SHGetKnownFolderPath = ctypes.windll.shell32.SHGetKnownFolderPath
    SHGetKnownFolderPath.argtypes = [
        ctypes.POINTER(GUID), ctypes.c_uint32, ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_wchar_p)
    ]
    SHGetKnownFolderPath.restype = ctypes.HRESULT

    path_ptr = ctypes.c_wchar_p()
    result = SHGetKnownFolderPath(ctypes.byref(folder_id), 0, None, ctypes.byref(path_ptr))

    if result != 0:
        raise OSError(f"Erro fodido no SHGetKnownFolderPath: {result}")

    return path_ptr.value

FOLDERIDS = {
    "Downloads": "{374DE290-123F-4565-9164-39C4925E467B}",
    "Documents": "{FDD39AD0-238F-46AF-ADB4-6C85480369C7}",
    "Desktop": "{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}",
}

local = random.choice(["Downloads", "Documents", "Desktop"])

try:
    pasta = get_known_folder(FOLDERIDS[local])
except Exception as e:

    pasta = get_known_folder(FOLDERIDS["Desktop"])

if not os.path.exists(pasta):

    pasta = get_known_folder(FOLDERIDS["Desktop"])

senha = str(random.randint(1000, 9999))

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
    print("Parabéns, você concluiu a história principal do Nasci!")
    print(f"Obrigado por jogar {node} :)")
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

print_animated(f"Era uma vez, um pequeno Nasci (você)... Que queria apenas ir ", delay=0.05)
os.system("cd .. && cd .. && cd assets && leite.png")
print_animated("comprar leite condensado", delay=0.05)
time.sleep(1.0)
input("Pressione ENTER para avançar")
os.system("cls")
print_animated("Então ele pega o elevador", delay=0.05)
print_animated("Desce para a garagem", delay=0.05)
print_animated("Vai entrar no carro", delay=0.05)
print_animated("Mas tá sem gasolina", delay=0.05)
time.sleep(1.0)
print("")
print_animated("E agora? O que você irá fazer?", delay=0.05)
print_animated("1: Cagar no motor", delay=0.01)
print_animated("2: Ir pro posto de gasolina", delay=0.01)
print_animated("3: Desistir da missão", delay=0.01)
print()
gasolina = input("R: ")
if gasolina == "1":
    os.system("cls")
    print("Você caga no motor")
    time.sleep(1)
    print_animated("Por conta disso...", delay=0.05)
    print_animated("o carro liga.", delay=0.05)
    time.sleep(1.0)
elif gasolina == "2":
    os.system("cls")
    time.sleep(1.0)
    print("primeiro")
    time.sleep(1)
    print("como q tu vai pro posto sem o carro?")
    time.sleep(3.0)
    final("NÃO FUI", "Não tinha gasolina, nem para ir no posto :(")
else:
    final("DESISTO!", "Não quero mais comprar leite condensado, cancei")

print_animated("Mas antes de você ir...", delay=0.1)
time.sleep(1)
print_animated("Você precisava do caminho para chegar no mercado")
time.sleep(1)
os.system("cls")
print_animated("Ele volta pro AP", delay=0.05)
print_animated("Pega o seu celular", delay=0.05)
print_animated("E vê um grande problema", delay=0.05)
time.sleep(3)
print_animated("Nasci: Qual é a senha do meu celular?")
print_animated("Você lembra que a senha de seu celular em algum lugar do seu computador", delay=0.05)
time.sleep(2.0)
arquivo = Path(pasta) / "senha do celular.txt"
with open(arquivo, "a", encoding="utf-8") as f:
    f.write(f"Senha do celular:\n{senha}\n")
os.system("cls")
print_animated("Você procura nas pastas principais do computador")
time.sleep(1.0)
print()
print("Digite a senha do celular aqui")
senhaU = input("R:")

for i in range(3):
    print(f"Verificando senha{'.' * (i % 3 + 1)}", end="\r")
    time.sleep(1.0)

if senhaU == senha:
    print_animated(f"{color['green']}Senha correta!       {color['reset']} ")
    time.sleep(3.0)
else:
    print_animated(f"{color['red']}Senha incorreta!       {color['reset']}")
    final(f"VOCÊ NÃO SABE PROCURAR NOS SEUS ARQUIVOS DIREITO {node}?", f"Você não viu na pasta {local}? Já deletei kkk, não vai ver n kkk")

os.system("cls")
print_animated("Ele desbloqueia o celular", delay=0.05)
print_animated("Baixa o GPS", delay=0.05)
print_animated("Mas sem querer pega um Malware (vírus)", delay=0.05)
print()
print_animated("E agora você não tem mais o caminho :(", delay=0.05)
print_animated("Então você sai de casa sem saber o caminho mesmo...", delay=0.05)
time.sleep(2.6)
os.system("cls")
print_animated("Quando você começa a andar, magicamente você encontra o Pão de Comida.", delay=0.05)
print_animated("UHUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU", delay=0.01)
time.sleep(3.0)
print_animated("Então você compra o leite condensado...", delay=0.05)
print_animated("E volta pra casa feliz!")
finalHist("DEU CERTO!", "Parabéns, você comprou o leite condensado e chegou em casa com segurança!")
