import time
from tqdm import tqdm
import os
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
    ...

def gerenciarClientes():
    ...

def registrarVenda():
    ...

def relatorios():
    ...

def escrever_devagar(texto, delay):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(delay)
        
def menu_produtos():
    os.system("cls")

    print("=" * 18)
    print("Gerenciar produtos")
    print("=" * 18)

    print("{1} Adicionar produto")
    print("{2} Remover Produto")
    print("{3} Atualizar Produto")
    print("{4} Listar Produtos")
    print("{0} Voltar")

    print("\nO que deseja fazer?\n")
    

menu_principal()