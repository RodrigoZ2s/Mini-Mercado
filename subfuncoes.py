import dados
from decimal import Decimal, InvalidOperation

## Sub funções para cada chamar funções dentro de cada "Submenus"

# > Funções de adicionar, remover, atualizar e listar produtos

def adicionarProduto():
    produto_adicionado = input("Nome do produto: ").lower()
    preco_produto = input("Preço: ")
    quantidade_produto = int(input("Quantidade (mínimo 1): "))

    try:
        preco_convertido = Decimal(preco_produto)
    except InvalidOperation:
        print("Valor inválido")
        return


    for info in dados.produtos.values():
        if info["nome"] == produto_adicionado:
            print("Esse produto já foi adicionado.")
            return
    
    if quantidade_produto < 1:
        return "Você não adicionou a quantidade mínima de produtos"
    
    id_produto = max(dados.produtos.keys(), default=0) + 1

    dados.produtos[id_produto] = {"nome": produto_adicionado, "preco": preco_convertido, "quantidade": quantidade_produto}

    print(f"Produto '{produto_adicionado}' adicionado com sucesso! ID: {id_produto}")

def removerProduto():
    id_produto = input("Informe o ID do produto: ")

    if id_produto not in dados.produtos:
        print("Esse produto não existe!")
        return
    
    del dados.produtos[id_produto]
    print(f"Produto ID: {id_produto} foi removido com sucesso")

def atualizarProduto():
    id_produto = input("Produto que deseja atualizar [ID]: ")

    if id_produto not in dados.produtos:
        print("Esse produto não está listado no sistema")
        return

    atualizacao = input("Qual informação deseja atualizar? \n [(1) nome | (2) preço | (3) quantidade] \n >> ")

    if atualizacao == "1":
        novo_nome = input("Novo nome: ")
        dados.produtos[id_produto].update({'nome': novo_nome})
        print(f"Produto [{id_produto}] foi atualizado. Nome: {novo_nome}")

    elif atualizacao == "2":
        novo_preco = input("Novo preço: ")

        try:
            preco_decimal = Decimal(novo_preco)
        except InvalidOperation:
            print("valor inválido")
            return

        dados.produtos[id_produto].update({'preco': preco_decimal})
        print(f"Produto [{id_produto}] foi atualizado. Preço: {novo_preco}")

    elif atualizacao == "3":
        try:
            nova_quantidade = int(input("Nova quantidade: "))
            dados.produtos[id_produto].update({'quantidade': nova_quantidade})
            print(f"Produto [{id_produto}] foi atualizado. Quantidade: {nova_quantidade}")
        except ValueError:
            print("Quantidade inválida! Deve ser um número inteiro.")

    else:
        print("Escolha inválida")
        return

def listarProduto():
    produtos_completos = {**dados.produtos}
    for produtos in produtos_completos.values():
        print(produtos)






   