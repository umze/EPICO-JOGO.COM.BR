import random
import time
import sys
import os
import platform

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
    "reset": "\033[0m"  # Para resetar a cor
}

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
    print_animated("Parabéns, você concluiu a história principal do Nasci! Em breve lançarei a história dos outros personagens.")
    print_animated(f"Obrigado por jogar {node} :)")
    print("-----------------------------------------")
    exit()

def print_animated(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)  # Escreve o caractere sem pular linha
        sys.stdout.flush()      # Força a atualização do output
        time.sleep(delay)       # Pausa por um curto período
    print()  # Pula linha no final

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
    print_animated("primeiro,")
    print_animated("como q tu vai pro posto sem o carro?", delay=0.1)
    time.sleep(3.0)
    print_animated("Então...", delay=0.4)
    time.sleep(3.0)
    print_animated("Esse é o fim")
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
print("Carregando...")
local = random.randint(1,3)
usuario = os.getlogin()
senha = str(random.randint(1000,9999))
if local == 1:
    local = "Downloads"
elif local == 2:
    local = "Documents"
elif local == 3:
    local = "Desktop"
pasta = f"C:/Users/{usuario}/{local}"
os.system(f"""cd {pasta} && echo Senha do celular: >> "senha do celular.txt" && echo {senha} >> "senha do celular.txt" """)

os.system("cls")

print_animated("Você procura nas pastas principais do computador")
time.sleep(1.0)
print()
print("Digite a senha do celular aqui")
senhaU = input("R:")

for i in range(3):
    print(f"Verificando senha{'.' * (i % 3 + 1)}", end="\r")
    time.sleep(1.0)

os.system(f"""cd C:/Users/{usuario}/{local} && del "senha do celular.txt" """)

if senhaU == senha:
    print_animated(f"{color['green']}Senha correta!       {color['reset']} ")
    time.sleep(3.0)
else:
    print_animated(f"{color['red']}Senha incorreta!       {color['reset']}")
    final(f"VOCÊ NÃO SABE PROCURAR NOS SEUS ARQUIVOS DIREITO {node}?", f"Você não viu na pasta {pasta}? Já deletei kkk, não vai ver n kkk")

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
