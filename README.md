#📖 Sistema de Gestão de Vendas e Estoque

## 📌 Descrição
Este projeto é um **sistema de gerenciamento de vendas, clientes e produtos**, desenvolvido em **Python**.  
Ele utiliza conceitos de **POO (Programação Orientada a Objetos)**, estruturas de dados como **fila** e **pilha**, além de manipulação de **arquivos de texto** para salvar os produtos cadastrados.  

O sistema apresenta um **menu interativo** no terminal que permite cadastrar clientes e produtos, realizar vendas, desfazer operações, visualizar filas de vendas pendentes e calcular o valor total de vendas e estoque.  

---

## ⚙️ Tecnologias e recursos usados
- **Python 3**  
- **Módulos da biblioteca padrão:**
  - `os`: manipulação de arquivos e limpeza da tela.  
  - `time`: pausas temporárias entre operações.  
  - `collections.deque`: estrutura de **fila (FIFO)** eficiente.  
- **Módulo `funcoes` (customizado):**
  - `limpar_tela()`: limpa a tela do terminal.  
  - `sair()`: finaliza a execução de algumas rotinas.  
  - `continuar()`: pausa aguardando interação do usuário.  

---

## 🏗️ Estrutura principal do código

### 📦 Classe `Produto`
- Representa um produto com:
  - `id`, `nome`, `preco` e `quantidade`.  
- Possui método `atualizar_estoque()` que valida e atualiza o estoque após uma venda.  
- Produtos são **persistidos em arquivo (`produtos.txt`)**, através das funções:
  - `salvar_produtos()`: salva todos os produtos.  
  - `carregar_produtos()`: carrega produtos salvos no arquivo para memória.  

---

### 👤 Classe `Cliente`
- Representa um cliente com:
  - `id`, `nome`, histórico de compras e total gasto.  
- Método `adicionar_compra()` registra compras realizadas.  

---

### 💰 Classe `Venda`
- Representa uma venda de um produto para um cliente.  
- Contém:
  - Cliente, Produto, Quantidade, Valor total.  
- Método `processar_venda()`:
  - Atualiza o estoque.  
  - Registra a compra no cliente.  
  - Exibe mensagem de sucesso.  

---

### 🧰 Estruturas de apoio
- **Lista de clientes**: mantém todos os clientes ativos.  
- **Lista de produtos**: mantém todos os produtos cadastrados.  
- **Fila de vendas (`deque`)**: armazena vendas pendentes (FIFO).  
- **Pilha de operações (`list`)**: permite **desfazer** últimas ações realizadas.  

---

### 🔄 Funções principais
- `registrar_operacao(tipo, objeto)`: registra ações na pilha.  
- `desfazer_ultima_operacao()`: remove clientes/produtos/vendas e reverte alterações.  
- `visualizar_fila_vendas()`: exibe a fila de vendas pendentes.  

---

## 🖥️ Funcionalidades disponíveis no MENU
1. **Cadastrar Cliente**  
2. **Listar Clientes**  
3. **Realizar Venda**  
   - Venda direta ou adicionada à fila de vendas pendentes.  
4. **Visualizar fila de vendas (FIFO)**  
5. **Desfazer última operação (pilha)**  
6. **Mostrar valor total de vendas realizadas**  
7. **Cadastrar Produto**  
8. **Listar Produtos**  
9. **Mostrar valor total do estoque**  
10. **Buscar Produto (por ID ou nome)**  
0. **Sair do sistema**  

---

## 📂 Persistência de dados
- Os **clientes** existem apenas em memória (não são salvos em arquivo).  
- Os **produtos** são salvos no arquivo `produtos.txt` e carregados automaticamente na inicialização.  
- O histórico de vendas é controlado por objetos em memória, com suporte a desfazer operações.  

---

Nomes: 

Enio Muliterno Neto - 1138165
Murilo Trevisol Dalmolin - 1138129
Artur Machado Ibañez - 1137674
Naubert Piva - 1138130
Ricardo Pereira Drews - 1138128

Tino Navarro - 1138028
