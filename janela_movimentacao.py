import tkinter as tk
from tkinter import Tk, ttk, Label, Button, PhotoImage, Frame
from persistencia import PersistenciaMovimentacao 

class JanelaMovimentacao(Tk):
    def __init__(self):
        super().__init__()
    def __init__(self):
        super().__init__()
        self.configurar_janela()
        self.configurar_background()
        self.configurar_barra_lateral()
        self.configurar_botoes_laterais()
        self.configurar_tabela()
        self.carregar_movimentacoes_na_tabela()
    
    def configurar_janela(self):
        self.title('Sistema Controle de Estoque')
        self.resizable(width=False, height=False)
        self.state('zoomed')
        self.iconbitmap('icon.ico')
        
    def configurar_background(self):
        self.configure(bg='#161515')
        
    def configurar_barra_lateral(self):
        self.quadro1 = Frame(self, borderwidth=1,relief='flat',background='#444444')
        self.quadro1.place(relwidth=0.135,relheight=1)
    
    def configurar_botoes_laterais(self):
        
        self.icon_inicio = PhotoImage(file="icons/home.png")
        self.icon_produtos = PhotoImage(file="icons/bag.png")
        self.icon_fornecedores = PhotoImage(file="icons/3_user.png")
        self.icon_estoque = PhotoImage(file="icons/folder.png")
        self.icon_movimentacao = PhotoImage(file="icons/chart.png")
        self.icon_relatorio = PhotoImage(file="icons/paper.png")
        
        estilo_template = {
            "relief": "flat",
            "bg": "#444444",
            "activebackground": "#555555",
            "bd": 0,
            "fg": "#FFFFFF",
            "activeforeground": "#FFFFFF",
            "font": ("Inter", 14, "bold"),
            "compound":'left'
        }
        
        self.button_inicio = Button(
            self.quadro1,
            text='Início',
            **estilo_template,
            image=self.icon_inicio,
            command=self.voltar_janela_inicio
        )
        self.button_inicio.pack(padx=50, pady=5,anchor='w')
        
        self.button_produto = Button(
            self.quadro1,
            text='Produtos',
            **estilo_template,
            image=self.icon_produtos,
            command=self.janela_produto
        )
        
        self.button_produto.pack(padx=50, pady=5,anchor='w')
        
        
        self.button_fornecedores = Button(
            self.quadro1,
            text='Fornecedores',
            **estilo_template,
            image=self.icon_fornecedores,
            command=self.janela_fornecedores
        )
        self.button_fornecedores.pack(pady=5, padx=50,anchor='w')
        
        
        self.button_estoque = Button(
            self.quadro1,
            text='Estoque',
            **estilo_template,
            image=self.icon_estoque,
            command=self.janela_estoque
        )
        self.button_estoque.pack(padx=50, pady=5,anchor='w')
        
        
        self.button_movimentacao = Button(
            self.quadro1,
            text='Movimentação',
            **estilo_template,
            image=self.icon_movimentacao
        )
        self.button_movimentacao.pack(padx=50, pady=5,anchor='w')
        
        
        self.button_relatorio = Button(
            self.quadro1,
            text='Relatórios',
            **estilo_template,
            image=self.icon_relatorio,
            command=self.janela_relatorios
        )
        self.button_relatorio.pack(padx=50, pady=5,anchor='w')
    
    def configurar_tabela(self):
        Label(
            self, text="Histórico de Movimentações", bg="#838181",
            fg="white", font=("Inter", 35, "bold"), anchor="center"
        ).place(relx=0.5, rely=0.08, anchor="center", height=90)


        self.quadro2 = Frame(self, background="#FDFDFD")
        self.quadro2.place(relx=0.143, rely=0.16, relwidth=0.848, relheight=0.8)

        self.tree = ttk.Treeview(self.quadro2, show='headings', selectmode='browse')
        colunas = ('id_produto', 'tipo', 'quantidade', 'data')
        self.tree['columns'] = colunas

        self.tree.heading('id_produto', text='ID do Produto', anchor='center')
        self.tree.heading('tipo', text='Tipo', anchor='center')
        self.tree.heading('quantidade', text='Quantidade', anchor='center')
        self.tree.heading('data', text='Data', anchor='center')

        scroll_y = ttk.Scrollbar(self.quadro2, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll_y.set)

        self.tree.column('id_produto', width=300, anchor='center', stretch=False)
        self.tree.column('tipo', width=200, anchor='center', stretch=False)
        self.tree.column('quantidade', width=200, anchor='center', stretch=False)
        self.tree.column('data', width=350, anchor='center', stretch=False)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")

        self.quadro2.rowconfigure(0, weight=1)
        self.quadro2.columnconfigure(0, weight=1)
    
    def carregar_movimentacoes_na_tabela(self):
        persist = PersistenciaMovimentacao()
        movimentacoes = persist.ler()

        for mov in movimentacoes:
            self.tree.insert("", "end", values=(
                mov["id_produto"],
                mov["tipo"],
                mov["quantidade"],
                mov["data"]
            ))

    def carregar_movimentacoes_na_tabela(self):
        persist = PersistenciaMovimentacao()
        movimentacoes = persist.ler()

        for mov in movimentacoes:
            self.tree.insert("", "end", values=(
                mov["id_produto"],
                mov["tipo"],
                mov["quantidade"],
                mov["data"]
            ))

    def carregar_movimentacoes_na_tabela(self):
            persist = PersistenciaMovimentacao()
            movimentacoes = persist.ler()

            for mov in movimentacoes:
                self.tree.insert("", "end", values=(
                    mov["id_produto"],
                    mov["tipo"],
                    mov["quantidade"],
                    mov["data"]
                ))    
    
    def voltar_janela_inicio(self):
        from janela_inico import JanelaInicio
        self.destroy()
        j = JanelaInicio()
    
    def janela_estoque(self):
        from janela_estoque import JanelaEstoque
        self.destroy()
        j = JanelaEstoque()
    
    def janela_fornecedores(self):
        from janela_fornecedores import JanelaFornecedores
        self.destroy()
        j = JanelaFornecedores()
        
    def janela_produto(self):
        from janela_produto import JanelaProduto
        self.destroy()
        j = JanelaProduto()
            
    def janela_relatorios(self):
        from janela_relatorios import JanelaRelatorios
        self.destroy()
        j = JanelaRelatorios()