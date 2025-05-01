import os
import platform
import win10toast


node = platform.node()
toaster = win10toast.ToastNotifier()


os.system("cls")

print(f"Você achou {node}!")
print("Só falta mais um arquivo!")
print("Caso você fechou o outro terminal, parabéns, você não deveria ter feito isso, reinicie tudo de volta")
print("Mas agora vamos ao que interessa, o enigma para me liberar")
print()
input("Pressione ENTER para continuar")
os.system("cls")
print("Então, eu baixei o arquivo e instalei ele, mas não havia como eu podia executar ele sem este local, ele salvou muito eu algumas horas. A pasta correta está dentro desse ")
input("Pressione ENTER ao terminar de ler o texto")
toaster.show_toast("niveK", f"Só falta mais um! Você consegue {node}!.")

appdata_path = os.getenv("APPDATA")
caminho_arquivo = os.path.join(appdata_path, "EPICO JOGO.COM.BR", "ondeestouinstalado.txt")

# Verifica se o arquivo existe
if os.path.exists(caminho_arquivo):
    with open(caminho_arquivo, "r") as f:
        pastadojogo = f.read()
        f.close()
else:
    input("ERRO: Não foi possível encontrar a pasta raíz do jogo. Reinicie o jogo. Tente executar o jogo como administrador")

os.system(f"cd {pastadojogo} && desktop.py")

exit()