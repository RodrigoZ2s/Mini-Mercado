import time

def menu_principal():
    while True:
        print("=" * 18)
        print("== MINI MERCADO ==")
        print("=" * 15)

        escrever_devagar("Bem vindo ao sistema", delay=0.08)
        escrever_devagar("...", delay=0.75)
        escolha_usuario = input("O que deseja fazer?\n")

        print("{1} Gerenciar produtos")
        print("{2} Gerenciar clientes")
        print("{3} Registrar vendas")
        print("{4} Relatórios")
        print("{0} Sair")



        










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
        

menu_principal()