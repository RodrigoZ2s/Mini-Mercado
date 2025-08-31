import time
from tqdm import tqdm
import dados
import subfuncoes

# menu = "Bem vindo ao sistema"

# for letra in menu:
#     time.sleep(0.08)
#     print(letra, end="", flush=True)
# for ponto in "...":
#     time.sleep(0.75)
#     print(ponto, end="", flush= True)


# for i in tqdm(range(10)):
#     time.sleep(1)
# print(i)

# from submenus import adicionarProduto

# while True:
#     adicionarProduto()
#     print(dados.produtos)

#     if input("Deseja adicionar outro produto? [s/n]").lower() != "s":
#         break


print(subfuncoes.listarProduto())


print(subfuncoes.escolherCliente())