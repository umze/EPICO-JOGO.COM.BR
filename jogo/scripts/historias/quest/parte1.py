import os
import platform
import win10toast


node = platform.node()
toaster = win10toast.ToastNotifier()


os.system("cls")

print(f"Você achou {node}!")
print("Então, para achar os outros 2 arquivos eles estarão em outros lugares.")
print("Caso você fechou o outro terminal, parabéns, você não deveria ter feito isso, reinicie tudo de volta")
print("Mas agora vamos ao que interessa, o enigma para me liberar.")
print()
input("Pressione ENTER para continuar")
os.system("cls")
print("Eu estava navegando na internet até que vi muitas coisas, diversas coisas legais, vídeos sobre uma coisa que eu amo! Capinar lotes e moer grões, mas eu não sabia como podia jogar esses jogos. A pasta onde está o próximo documento está nesse textinho.")
input("Pressione ENTER ao terminar de ler o texto")
toaster.show_toast("niveK", "Você consegue! Não desista, você deve saber onde fica esse arquivo.")

appdata_path = os.getenv("APPDATA")
caminho_arquivo = os.path.join(appdata_path, "EPICO JOGO.COM.BR", "ondeestouinstalado.txt")

# Verifica se o arquivo existe
if os.path.exists(caminho_arquivo):
    with open(caminho_arquivo, "r") as f:
        pastadojogo = f.read()
        f.close()
else:
    input("ERRO: Não foi possível encontrar a pasta raíz do jogo. Reinicie o jogo. Tente executar o jogo como administrador")

os.system(f"cd {pastadojogo} && down.py")

exit()