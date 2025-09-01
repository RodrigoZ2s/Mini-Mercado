import dados
from decimal import Decimal, InvalidOperation
from validate_docbr import CPF

## Sub funções para cada chamar funções dentro de cada "Submenus"

# > Funções: adicionar, remover, atualizar e listar produtos

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

    if int(id_produto) not in dados.produtos:
        print("Esse produto não existe!")
        return
    
    del dados.produtos[int(id_produto)]
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

# > Funções: adicionar, remover e listar clientes

def adicionarCliente():
    
    nome_cliente = input("Nome e Sobrenome do cliente (Separados): ")

    nome_verificado = all(parte.isalpha() for parte in nome_cliente.split())
    # Verifica se o nome está dentro do alfabeto
    if not nome_verificado:
        print("Nome inválido")
        return

    cpf_cliente = input("CPF: ")
    # Verifica se o CPF do cliente é válido usando uma biblioteca (docbr)
    if not CPF(cpf_cliente):
        print("CPF inválido!")
        return 
    

    for info in dados.clientes.values():
        if info["cpf"] == cpf_cliente:
            print("Cliente já está cadastrado no sistema.")
            return
        
    id_cliente = max(dados.clientes.keys(), default=0) + 1

    dados.clientes[id_cliente] = {"nome": nome_cliente, "cpf": cpf_cliente}

    print(f"Cliente adicionado com sucesso | ID: {id_cliente} CPF: {cpf_cliente}")
        
def removerCliente():
    
    id_cliente = input("ID do cliente: ")
    try:
        id_cliente = int(id_cliente)
    except ValueError:
        print("ID inválido! Deve ser um número.")
        return

    if id_cliente not in dados.clientes:
        print("Cliente não existente no sistema.")
        return

    confirmar_exclusao = input(f"Digite o CPF do cliente para confirmar o exclusão: ")
    
    if confirmar_exclusao != dados.clientes[id_cliente]["cpf"]:
        print("CPF não condiz com o ID informado. Exclusão cancelada.")
        return

    del dados.clientes[id_cliente]
    print(f"Cliente ID: {id_cliente} foi removido com sucesso")

def listarCliente():

    
    lista_clientes = {**dados.clientes}

    for id_cliente, info in lista_clientes.items():
            print(f"[ID: {id_cliente} | Nome: {info['nome']} | CPF: {info['cpf']}]")
    
# > Funções: escolher cliente, escolher produto e qtd, verificar estoque, atualizar estoque e salvar venda na lista de vendas

def escolherCliente():
    total = 0

    # Listar clientes

    if not dados.clientes:
        return input("> Nenhum cliente cadastrado no sistema.\n[Pressione Enter para voltar] ")
    
    while True:
        print("- Lista de clientes ativos -")

        for numero_ID, cliente in dados.clientes.items():
            print(f"ID: {numero_ID} | Nome: {cliente['nome']}")

    # Escolher cliente

        cliente = input("ID do cliente: ")

        try:
            cliente = int(cliente)
        except ValueError:    
            print("Digite apenas números.")
            return

        for numero_ID in dados.clientes:
            if cliente == numero_ID:
                print(18*"=")
                print("Escolha um produto e sua quantidade")
                print(18*"=")

                produto_comprado = input("Produto (ID): ")
                
                # Verificações de produto e estoque
                if produto_comprado not in dados.produtos:
                    print("Produto não existe")
                    return
                
                if dados.produtos[produto_comprado]["quantidade"] == 0:
                    print("Produto fora de estoque")        
                    return

                quantidade = int(input("Qtd: "))
                
                # Verificações de quantidade

                if quantidade > dados.produtos[produto_comprado]["quantidade"]:
                    print("Indisponível a quantidade solicitada deste produto em estoque")
                    return
                
                if quantidade == 0:
                    print("Você não escolheu uma quantidade válida")
                    return 
                
                # Caso tenha estoque e não caia em nenhuma excessão

                dados.produtos[produto_comprado]["quantidade"] -= quantidade

                total += dados.produtos[produto_comprado]['preco'] * quantidade

                dados.vendas.append({"id": cliente, "produto_comprado": produto_comprado, "quantidade_comprada": quantidade})


                









                











   