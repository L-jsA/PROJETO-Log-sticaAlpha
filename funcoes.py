import csv
import os # é as funções do sitema operacional (operational system)
from tkinter import ttk

dados_fretes = "dados_fretes.csv"
# dizendo o nome do arquivo

campo_fretes = ["Registro_frete","Origem","Destino","Cliente","Produto","Status"]
# Informar todos os campos do frete

# FUNÇÕES

# adicionar_registro_frete - segurança para o sistema
# abrir_o_formulario do frete - criar uma tela para add as infos
# salvar_o_frete - atualizar o csv

import tkinter as tk
def abrir_formulario_frete():
    popup_frete = tk.Toplevel()
    popup_frete.title("Adicionar Fretes")
    popup_frete.geometry("350x350")

    labels_fretes = ["Registro_frete","Origem","Destino","Cliente","Produto","Status"]
    fretes = {}

    # Vou sequenciar campo com dados
    for campo_dados in labels_fretes: 
        # para cada campo que o usuário digita, ele vai fazer alguma coisa
        tk.Label(popup_frete, text=campo_dados).pack(pady=5)
        # essa linha cria todos os textos para o usuário 
        entrada_fretes = tk.Entry(popup_frete)
        # Entry é o input(caixa de texto)
        entrada_fretes.pack()
        fretes[campo_dados] = entrada_fretes
    
    def salvar():
        dados = {campo_dados:fretes[campo_dados].get() for campo_dados in fretes}
        add_fretes(dados)
        # Fechar automático uma jenela
        popup_frete.destroy()

    def limpar():
        for campo_fretes in fretes:
            fretes[campo_fretes].delete(0, tk.END)
        
    tk.Button(popup_frete, text= "Salvar", command=salvar).pack(pady=20)
    tk.Button(popup_frete, text="Limpar", command=limpar, pady=20).pack()

def add_fretes(registro):
    # Para manipular o arquivo
    arquivo = os.path.isfile(dados_fretes)

    # Adicionar valores
    # Sempre que usamos o with open informamos
    # ! - arquivo, 2 - modo, 3 - novas linhas, 4 - utf-8
    with open(dados_fretes, "a", newline="", encoding="utf-8") as arquivo_fretes:
        escrever = csv.DictWriter(arquivo_fretes, fieldnames=campo_fretes)
        
        # Para adicionar os dados no CSV
        escrever.writerow(registro)

# ---------------------- ADD CLIENTE --------------------------------
dados_clientes = "dados_clientes.csv"


campo_clientes = ["Registro","Cliente","Nome","Sobrenome","Cidade","Bairro"]


import tkinter as tk
def abrir_formulario_cliente():
    popup_clientes = tk.Toplevel()
    popup_clientes.title("Adicionar Clientes")
    popup_clientes.geometry("350x350")

    labels_clientes = ["Registro","Cliente","Nome","Sobrenome","Cidade","Bairro"]
    clientes = {}

    for campo_clientes in labels_clientes: 
        tk.Label(popup_clientes, text=campo_clientes).pack(pady=5)
        entrada = tk.Entry(popup_clientes)
        entrada.pack()
        clientes[campo_clientes] = entrada
    
    def salvar():
        dados = {campo_clientes: clientes[campo_clientes].get() for campo_clientes in clientes}
        add_clientes(dados)
        popup_clientes.destroy()

    def limpar():
        for campo_clientes in clientes: # Ele percorre todas as chaves do dicionário clientes
            # pega o Entry daquela chave
            # apaga todo o texto, do início (0) ao final (END)
            clientes[campo_clientes].delete(0, tk.END)
        
    tk.Button(popup_clientes, text= "Salvar", command=salvar).pack(pady=20)
    tk.Button(popup_clientes, text="Limpar", command=limpar, pady=20).pack()

def add_clientes(registro):
    arquivo = os.path.isfile(dados_clientes)

    with open(dados_clientes, "a", newline="", encoding="utf-8") as arquivo_clientes:
        escrever = csv.DictWriter(arquivo_clientes, fieldnames=campo_clientes)
        
        escrever.writerow(registro)
    
# -------------- VER FRETES ---------------------------------------
def exibir_fretes():
    # Sempre que exibir dados, colocar fator correção
    if not os.path.isfile(dados_fretes):
        tk.Message.showerror("Erro", "Arquivo não encontrado")
        return 
    
    # Criar a janela da tabela de fretes
    tabela_fretes = tk.Toplevel()
    tabela_fretes.title("Fretes")
    tabela_fretes.geometry("750x500")

    # Dizer a tabela os campos que ela tem (em colunas)
    colunas_fretes = campo_fretes

    # Vamos juntar a tabela com as colunas (modo árvore)
    tabela = ttk.Treeview(tabela_fretes,columns=colunas_fretes, show="headings")
    # o Treeview é o comano para mostrar os dados
    # nele tenho que colocar 1 - onde, 2 - colunas, 3 - cabeçalhos
    # ficando ttk.Treeview(NOME DA JANELA, columns=COLUNAS, SHOW="headings")
    tabela.pack(fill="both")

    # Configuração colunas
    for colunas in colunas_fretes:
        # chamo o campo cabeçaalho para escrever o cabeçalho das colunas
        tabela.heading(colunas, text=colunas)
        # chamo o campo column para configurar o tamanho de cada uma
        tabela.column(colunas, width=100)

    # Ler os dados do Csv
    with open(dados_fretes,"r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        # ler o Csv

        # mostrar o csv
        for linha in leitor:
            # para cada linha do Csv que o leitor leu
            # vou criar um campo com valor
            valor = [linha.get(colunas, "") for colunas in colunas_fretes]
            # o comando insert é para colocar os valores nas linhas e nas colunas 
            tabela.insert("", "end", values=valor)

# -------------------- VER CLIENTE ------------------------------
def exibir_cliente():
    # Sempre que exibir dados, colocar fator correção
    if not os.path.isfile(dados_clientes):
        tk.Message.showerror("Erro", "Arquivo não encontrado")
        return 
    
    # Criar a janela da tabela de fretes
    tabela_clientes = tk.Toplevel()
    tabela_clientes.title("Clientes")
    tabela_clientes.geometry("750x500")

    # Dizer a tabela os campos que ela tem (em colunas)
    colunas_clientes = campo_clientes

    # Vamos juntar a tabela com as colunas (modo árvore)
    tabela = ttk.Treeview(tabela_clientes,columns=colunas_clientes, show="headings")
    # o Treeview é o comano para mostrar os dados
    # nele tenho que colocar 1 - onde, 2 - colunas, 3 - cabeçalhos
    # ficando ttk.Treeview(NOME DA JANELA, columns=COLUNAS, SHOW="headings")
    tabela.pack(fill="both")

    # Configuração colunas
    for colunas in colunas_clientes:
        # chamo o campo cabeçaalho para escrever o cabeçalho das colunas
        tabela.heading(colunas, text=colunas)
        # chamo o campo column para configurar o tamanho de cada uma
        tabela.column(colunas, width=100)

    # Ler os dados do Csv
    with open(dados_clientes,"r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        # ler o Csv

        # mostrar o csv
        for linha in leitor:
            # para cada linha do Csv que o leitor leu
            # vou criar um campo com valor
            valor = [linha.get(colunas, "") for colunas in colunas_clientes]
            # o comando insert é para colocar os valores nas linhas e nas colunas 
            tabela.insert("", "end", values=valor)