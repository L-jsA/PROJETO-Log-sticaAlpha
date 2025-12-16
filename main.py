import tkinter as tk # tk inter é uma biblioteca de interface gráfica para Python
from tkinter import ttk # o ttk é os widgets do Python (coisas que posso interagir)
from funcoes import *

# Vamos criar a nossa tela
root = tk.Tk() # cria a tela principal do sistema
root.title("Projeto srcrum - logistíca")

# Criar o tamanho da tela (largura x altura)
root.geometry("400x300")

# ---- CABEÇALHO ----
cabecalho = ttk.Label(
    # Qual tela ele vai?
    root,
    # Qual a informação
    text = "Logistica Alpha",
    # Qual a font
    font=("Arial", 20, "bold"),
    # Subtítulo
)
# Atribuir na tela
cabecalho.pack(pady=20)

subtitle = ttk.Label(
    root,
    text = "Frete mais rápido aqui",
    font=("Arial", 10, "italic")
)
subtitle.pack(pady=5)

# ---- FIM DO CABEÇALHO ----

# CRIAR ÁREA DOS BOTÒES (é tipo uma Div do Html)

tabela_btn = ttk.Frame(root)
# Criei um espaço para os botões e coloquei na tela principal (root)
tabela_btn.pack(pady=20)

# Criar os botòes 
btn_ver_frete = ttk.Button(tabela_btn, text="Ver fretes",command=exibir_fretes)
btn_add_frete = ttk.Button(tabela_btn, text="Add fretes", command=abrir_formulario_frete)
btn_ver_cliente = ttk.Button(tabela_btn, text="Ver clientes", command=exibir_cliente)
btn_add_cliente = ttk.Button(tabela_btn, text="Add cliente", command=abrir_formulario_cliente)

# Exibir os btns
# Para ver os botòes, eu crio uma tabela e falo qual linha e qual coluna vai exibir
btn_ver_frete.grid(row = 0, column= 0, pady= 10, padx= 10)
btn_add_frete.grid(row = 1, column = 0, pady = 10, padx= 10)
btn_ver_cliente.grid(row = 0, column = 1, pady = 10, padx= 10)
btn_add_cliente.grid(row = 1, column = 1, pady = 10, padx= 10)

# Para ver a tela
root.mainloop()