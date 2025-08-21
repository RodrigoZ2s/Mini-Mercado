import time
from tqdm import tqdm

menu = "Bem vindo ao sistema"

for letra in menu:
    time.sleep(0.08)
    print(letra, end="", flush=True)
for ponto in "...":
    time.sleep(0.75)
    print(ponto, end="", flush= True)


for i in tqdm(range(10)):
    time.sleep(1)
print(i)