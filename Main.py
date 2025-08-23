import time
import os
import dados
import subfuncoes
import submenus
from tqdm import tqdm
from dados import produtos, clientes


def menu_principal(): # Finalizado
    for i in tqdm(range(10), desc="Carregando"):
        time.sleep(0.5)

    escrever_devagar("\n✅ Sistema carregado com sucesso!\n", delay=0.06)
    escrever_devagar("🏪 Bem vindo!", delay=0.08)
    time.sleep(1)
    os.system('cls')

    while True:
        print("=" * 18)
        print("== MINI MERCADO ==")
        print("=" * 18)

        print("{1} Gerenciar produtos")
        print("{2} Gerenciar clientes")
        print("{3} Registrar vendas")
        print("{4} Relatórios")
        print("{0} Sair")
        print("\nO que deseja fazer?\n")
        escolha_usuario = input(">>")

        if escolha_usuario not in ["0","1","2","3","4"]:
            print("\n>> Opção inválida!\n")
            continue

        if escolha_usuario == "1":
            gerenciarProdutos()
        elif escolha_usuario == "2":
            gerenciarClientes()
        elif escolha_usuario == "3":
            registrarVenda()
        elif escolha_usuario == "4":
            relatorios()
        elif escolha_usuario == "0":
            break

def gerenciarProdutos():
    submenus.menu_produtos()

def gerenciarClientes():
    ...

def registrarVenda():
    ...

def relatorios():
    ...

def escrever_devagar(texto, delay): # Função para escrever devagar
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(delay)
        
