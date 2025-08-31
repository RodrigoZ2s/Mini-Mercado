from subfuncoes import adicionarProduto
import subfuncoes
import os


## Sub menus para o mini mercado

# > Menu de produtos

def menu_produtos():
    

    os.system("cls")

    while True:
        print("=" * 18)
        print("Gerenciar produtos")
        print("=" * 18)

        print("{1} Adicionar produto")
        print("{2} Remover Produto")
        print("{3} Atualizar Produto")
        print("{4} Listar Produtos")
        print("{0} Voltar")

        print("\nO que deseja fazer?\n")
        escolha_produtos = input(">> ")
        
        if escolha_produtos not in ["1", "2", "3", "4", "0"]: # Função que verifica se a opção escolhida existe
            print("Opção inválida")
            continue

        if escolha_produtos == "1":
            while True:
                subfuncoes.adicionarProduto()
                if input("Deseja adicionar outro produto? [s/n]").lower() != "s":
                    break

        elif escolha_produtos == "2":
            while True:
                subfuncoes.removerProduto()
                if input("Deseja remover outro produto? [s/n]").lower() != "s":
                    break

        elif escolha_produtos == "3":    
            while True:
                subfuncoes.atualizarProduto()
                if input("Deseja atualizar outro produto? [s/n]").lower != "s":
                    break

        elif escolha_produtos == "4":
            while True:
                subfuncoes.atualizarProduto()
                if input("Deseja listar os produtos novamente? [s/n]").lower != "s":
                    break
        else:
            break

def menu_cliente():
    os.system("cls")

    while True:
        print("=" * 18)
        print("Gerenciar clientes")
        print("=" * 18)

        print("{1} Adicionar Cliente")
        print("{2} Remover Cliente")
        print("{3} Listar Clientes")
        print("{0} Voltar")

        print("\nO que deseja fazer?\n")
        escolha_clientes = input(">> ")

        if escolha_clientes not in ["1", "2", "3", "0"]:
            print("Opção inválida!")
            continue

        if escolha_clientes == "1":
            while True:
                subfuncoes.adicionarCliente()
                if input("Deseja adicionar outro cliente? [s/n]").lower() != "s":
                    break
        elif escolha_clientes == "2":
            while True:
                subfuncoes.removerCliente()
                if input("Deseja remover outro cliente? [s/n]").lower() != "s":
                    break
        elif escolha_clientes == "3":
            while True:
                subfuncoes.listarCliente()
                if input("Deseja listar os clientes novamente?").lower() != "s":
                    break
        else:
            break

def menu_registrarVendas():
    os.system("cls")

    while True:
        print("=" * 18)
        print("Registrar Vendas")
        print("=" * 18)

        print("{1} Escolher cliente")
        print("{2} Escolher produto(s) e quantidade")
        print("{3} Verificar estoque")
        print("{4} Atualizar estoque")  
        print("{5} Salvar venda na lista de vendas")
        print("{0} Voltar")

        print("\nO que deseja fazer?\n")
        escolha_clientes = input(">> ")

        if escolha_clientes not in ["1", "2", "3", "4", "5", "0"]:
            print("Opção inválida!")
            continue

        if escolha_clientes == "1":
            while True:
                subfuncoes.
                if input("Deseja adicionar outro cliente? [s/n]").lower() != "s":
                    break
        elif escolha_clientes == "2":
            while True:
                subfuncoes.
                if input("Deseja remover outro cliente? [s/n]").lower() != "s":
                    break
        elif escolha_clientes == "3":
            while True:
                subfuncoes.
                if input("Deseja listar os clientes novamente?").lower() != "s":
                    break

        elif escolha_clientes == "4":
            while True:
                subfuncoes.
                if input("Deseja listar os clientes novamente?").lower() != "s":
                    break

        elif escolha_clientes == "5":
            while True:
                subfuncoes.
                if input("Deseja listar os clientes novamente?").lower() != "s":
                    break
        else:
            break    
        