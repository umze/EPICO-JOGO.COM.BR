import os
import platform
import win10toast


node = platform.node()
toaster = win10toast.ToastNotifier()


os.system("cls")

print(f"Você achou {node}!")
print("Pronto, só falta uma coisa mesmo, mas agora não é achar outro arquivo!")
print("Caso você fechou o outro terminal, parabéns, você não deveria ter feito isso, reinicie tudo de volta")
print()
input("Pressione ENTER para continuar")
toaster.show_toast("niveK", f"Pressione ENTER no terminal em que você está jogando o jogo {node}")

appdata_path = os.getenv("APPDATA")
terminei = os.path.join(appdata_path, "EPICO JOGO.COM.BR", "termineionivek.txt")
os.makedirs(os.path.dirname(terminei), exist_ok=True)

with open(terminei, "w") as f:
    f.write("yeah")

exit()