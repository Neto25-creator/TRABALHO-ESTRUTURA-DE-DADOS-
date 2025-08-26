import os, time
from funcoes import limpar_tela, sair, continuar, parar_operacao
from collections import deque
os.system("cls" if os.name == "nt" else "clear") #para testar no mac

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizar_estoque(self, quantidade_vendida):
        if quantidade_vendida > self.quantidade:
            print(f"Estoque insuficiente para {self.nome}.")
            return False
        self.quantidade -= quantidade_vendida
        print(f"Estoque de {self.nome} atualizado. Quantidade restante: {self.quantidade}.")
        salvar_produtos(lista_produtos)  # salva sempre que mexe no estoque
        return True


def salvar_produtos(produtos, arquivo="produtos.txt"):
    with open(arquivo, "w", encoding="utf-8") as f:
        for p in produtos:
            f.write(f"{p.nome};{p.preco};{p.quantidade}\n")

def carregar_produtos(arquivo="produtos.txt"):
    produtos = []
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                nome, preco, quantidade = linha.strip().split(";")
                produtos.append(Produto(nome, float(preco), int(quantidade)))
    return produtos


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.historico_compras = []
        self.total_gasto = 0.0

    def adicionar_compra(self, produto, valor):
        self.historico_compras.append((produto, valor))
        self.total_gasto += valor
        print(f"Compra de {produto} no valor de R${valor:.2f} adicionada ao histórico de {self.nome}.")
        continuar()
        limpar_tela()


class Venda:
    def __init__(self, cliente, produto, quantidade):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.valor_total = produto.preco * quantidade

    def processar_venda(self):
        if self.produto.atualizar_estoque(self.quantidade):
            self.cliente.adicionar_compra(self.produto.nome, self.valor_total)
            print(f"Venda de {self.quantidade} unidades de {self.produto.nome} para {self.cliente.nome} processada com sucesso. Valor total: R${self.valor_total:.2f}. Voltando...")
            continuar()
            limpar_tela()
        else:
            print("Venda não processada devido a problemas no estoque. Voltando...")
            continuar()
            limpar_tela()



opcoes = {
    1: "Cadastrar Cliente",
    2: "Listar Clientes",
    3: "Realizar Venda",
    4: "Vizualizar fila de vendas",
    5: "Desfazer última operação",
    6: "Valor total de vendas realizadas",
    7: "Cadastrar Produto",
    8: "Listar Produtos",
    9: "Valor total do estoque",
    10: "Buscar Produto",
    0: "Sair do sistema"
}

lista_clientes = [
    Cliente("João"),
    Cliente("Maria"),
    Cliente("Carlos")
]

lista_produtos = carregar_produtos()  # carrega os produtos do arquivo
fila_vendas = deque()
pilha_operacoes = []


def registrar_operacao(tipo, objeto):
    pilha_operacoes.append((tipo, objeto))

def desfazer_ultima_operacao():
    if not pilha_operacoes:
        print("Nenhuma operação para desfazer.\n")
        continuar()
        limpar_tela()
        return

    tipo, objeto = pilha_operacoes.pop()

    if tipo == "cliente":
        lista_clientes.remove(objeto)
        print(f"Desfeito: cliente {objeto.nome} removido.")

    elif tipo == "produto":
        lista_produtos.remove(objeto)
        salvar_produtos(lista_produtos)  # atualiza o arquivo
        print(f"Desfeito: produto {objeto.nome} removido.")

    elif tipo == "venda_fila":
        fila_vendas.remove(objeto)
        print(f"Desfeito: venda de {objeto.produto.nome} para {objeto.cliente.nome} removida da fila.")

    elif tipo == "venda_realizada":
        objeto.produto.quantidade += objeto.quantidade
        objeto.cliente.total_gasto -= objeto.valor_total
        if objeto.cliente.historico_compras:
            objeto.cliente.historico_compras.pop()
        salvar_produtos(lista_produtos)  # atualiza o estoque no arquivo
        print(f"Desfeito: venda de {objeto.produto.nome} para {objeto.cliente.nome} revertida.")

    continuar()
    limpar_tela()



def visualizar_fila_vendas(fila):
    if not fila_vendas:
        print("não há nenhuma venda na fila.\n")
        return
    print(f"{'Pos':<4}{'Cliente':<20}{'Produto':<20}{'Qtd':<5}{'Total (R$)':>12}")
    print("-" * 65)
    for i, v in enumerate(fila, 1):
        print(f"{i:<4}{v.cliente.nome:<20}{v.produto.nome:<20}{v.quantidade:<5}{v.valor_total:>12.2f}")



tam = 55
while True:
    print(f"+{'-' * tam}+")
    print(f"|{'MENU':^{tam}}|")
    print(f"+{'-' * tam}+")
    for k, v in opcoes.items():
        print(f"| {k} - {v:<{50}}|")
    print(f"+{'-' * tam}+")
    try:
        operacao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida, digite apenas números.")
        time.sleep(3)
        limpar_tela()
        continue

    if operacao == 0:
        salvar_produtos(lista_produtos)  
        limpar_tela()
        break

   
    if operacao == 1:
        limpar_tela()
        while True:
            nome = input("Digite o nome do cliente: ")
            # Verifica se já existe um cliente com esse nome
            if any(cliente.nome == nome for cliente in lista_clientes):
                print("Este cliente já está cadastrado!\n")
                continuar()
                opcao = input("Pressione Enter para tentar novamente ou 0 para sair: ")
                limpar_tela()
                if opcao == "0":
                    sair()
                    break
                continue  # Volta para cadastrar outro nome 
            novo_cliente = Cliente(nome)
            lista_clientes.append(novo_cliente)
            registrar_operacao("cliente", novo_cliente)
            print("O cliente foi cadastrado com sucesso!\n")
            time.sleep(1)
            opcao = input("Pressione Enter para cadastrar mais clientes e 0 para sair:")
            limpar_tela()
            if opcao == "0":
                sair()
                break
    
    if operacao == 2:
            limpar_tela()
            for cliente in lista_clientes:
                print(f"Nome: {cliente.nome}, Total Gasto: R${cliente.total_gasto:.2f}")
            print("\n")
            if not lista_clientes:
                print("Nenhum cliente cadastrado.\n")
            continuar()
            limpar_tela()
            sair()
    
    if operacao == 3:
        while True:
            if not lista_clientes:
                print("Nenhum cliente cadastrado. Cadastre um cliente antes de realizar uma venda.\n")
                continuar()
                limpar_tela()
                break
            if not lista_produtos:
                print("Nenhum produto cadastrado. Cadastre um produto antes de realizar uma venda.\n")
                continuar()
                limpar_tela()
                break

            print("Clientes Disponíveis:")
            for idx, cliente in enumerate(lista_clientes):
                print(f"{idx + 1}. {cliente.nome}")
            cliente_idx = int(input("Selecione o número do cliente (0 para voltar): ")) - 1
            if cliente_idx == -1:  # usuário digitou 0
                limpar_tela()
                break
            if cliente_idx < 0 or cliente_idx >= len(lista_clientes):
                print("Cliente inválido.\n")
                time.sleep(3)
                limpar_tela()
                continue
            cliente_selecionado = lista_clientes[cliente_idx]

            print("\nProdutos Disponíveis:")
            for idx, produto in enumerate(lista_produtos):
                print(f"{idx + 1}. {produto.nome} - Preço: R${produto.preco:.2f}, Quantidade em Estoque: {produto.quantidade}")
            produto_idx = int(input("Selecione o número do produto (0 para voltar): ")) - 1
            if produto_idx == -1:
                limpar_tela()
                break
            if produto_idx < 0 or produto_idx >= len(lista_produtos):
                print("Produto inválido.\n")
                time.sleep(3)
                limpar_tela()
                continue
            produto_selecionado = lista_produtos[produto_idx]

            try:
                quantidade = int(input(f"Digite a quantidade de {produto_selecionado.nome} a ser vendida: "))
            except ValueError:
                print("Digite apenas números válidos.\n")
                time.sleep(3)
                limpar_tela()
                continue

            if quantidade <= 0:
                print("Quantidade inválida.\n")
                time.sleep(3)
                limpar_tela()
                continue

            venda = Venda(cliente_selecionado, produto_selecionado, quantidade)

            destino = input("Digite 'f' para adicionar à FILA ou pressione Enter para processar agora: ").strip().lower()
            if destino == 'f':
                fila_vendas.append(venda)
                registrar_operacao("venda_fila", venda) 
                print("Venda adicionada à fila de vendas pendentes.")
                continuar()
                limpar_tela()
            else:
                venda.processar_venda()
                registrar_operacao("venda_realizada" , venda)

            opcao = input("Deseja realizar outra venda? (s/n): ").lower()
            if opcao != "s":
                limpar_tela()
                break


    if operacao == 4:
        while True:
            limpar_tela()
            print("Fila de vendas pendentes\n")
            visualizar_fila_vendas(fila_vendas)
            print("\nOpções:")
            print("1 - Processar PRÓXIMA venda (FIFO)")
            print("2 - Processar TODAS as vendas")
            print("0 - Voltar")
            escolha = input("Escolha: ").strip()

            if escolha == "1":
                if fila_vendas:
                    venda_pendente = fila_vendas.popleft()
                    venda_pendente.processar_venda()
                else:
                    print("Fila vazia.")
                    time.sleep(2)
                    limpar_tela()

            elif escolha == "2":
                if not fila_vendas:
                    print("Fila vazia.")
                    time.sleep(2)
                    limpar_tela()
                    continue
                
                while fila_vendas:
                    venda_pendente = fila_vendas.popleft()
                    venda_pendente.processar_venda()
                print("Todas as vendas da fila foram processadas.")
                time.sleep(2)
                limpar_tela()

            elif escolha == "0":
                limpar_tela()
                sair()
                break

            else:
                print("Opção inválida.")
                time.sleep(2)
                limpar_tela()

   
    if operacao == 5:    
        desfazer_ultima_operacao()
                

    if operacao == 6:
        limpar_tela()
        total_vendas = sum(cliente.total_gasto for cliente in lista_clientes)
        print(f"Valor total de vendas realizadas: R${total_vendas:.2f}\n")
        continuar()
        limpar_tela()
        sair()

    if operacao == 7:
        while True:
            limpar_tela()
            nome = input("Digite o nome do produto: ")
            if any(produto.nome == nome for produto in lista_produtos):
                print("Este produto já está cadastrado!\n")
                time.sleep(1)
                continue
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            novo_produto = Produto(nome, preco, quantidade)
            lista_produtos.append(novo_produto)
            registrar_operacao("produto", novo_produto)
            print("O produto foi cadastrado com sucesso!\n")
            opcao = input("Pressione Enter para tentar novamente ou 0 para sair: ")
            limpar_tela()
            if opcao == "0":
                limpar_tela()
                sair()
                break
        
    if operacao == 8:
        limpar_tela()
        for produto in lista_produtos:
            print(f"Nome: {produto.nome}, Preço: R${produto.preco:.2f}, Quantidade: {produto.quantidade}")
        print("\n")
        continuar()
        limpar_tela()
        sair()
        
    if operacao == 9:
        limpar_tela()
        valor_total_estoque = sum(produto.preco * produto.quantidade for produto in lista_produtos)
        print(f"Valor total do estoque: R${valor_total_estoque:.2f}\n")
        continuar()
        limpar_tela()
        sair()
    if operacao not in opcoes:
        print("Opção Inválida")
        continue
    print(f"{opcoes.get(operacao)}\n")


    if operacao == 10:
        while True:
            limpar_tela()
            termo_busca = input("Digite o nome do produto para buscar ou 0 para sair: ").strip().lower()
            if termo_busca == "0":
                limpar_tela()
                sair()
                break     
            produtos_encontrados = [p for p in lista_produtos if termo_busca in p.nome.lower()]
            if produtos_encontrados:
                print(f"{'Nome':<20}{'Preço (R$)':<15}{'Quantidade':<10}")
                print("-" * 45)
                for produto in produtos_encontrados:
                    print(f"{produto.nome:<20}{produto.preco:<15.2f}{produto.quantidade:<10}")
            else:
                print("Nenhum produto encontrado com esse nome.\n")
                continuar()
                continue 
            continuar()
            limpar_tela()
            sair()