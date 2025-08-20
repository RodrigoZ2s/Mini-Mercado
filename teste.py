import time

menu = "Bem vindo ao sistema"

for letra in menu:
    time.sleep(0.08)
    print(letra, end="", flush=True)
for ponto in "...":
    time.sleep(0.75)
    print(ponto, end="", flush= True)
