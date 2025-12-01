import tkinter as tk
from tkinter import Tk, ttk, messagebox, Button, PhotoImage, Frame

class JanelaMovimentacao(Tk):
    def __init__(self):
        super().__init__()
    def __init__(self):
        super().__init__()
        self.configurar_janela()
        self.configurar_background()
        self.configurar_barra_lateral()
        self.configurar_botoes_laterais()
    
    def configurar_janela(self):
        self.title('Sistema Controle de Estoque')
        self.resizable(width=False, height=False)
        self.state('zoomed')
        
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
    
    def _criar_area_principal(self):
        self.main_frame = tk.Frame(self, bg="#1f1f1f")
        self.main_frame.pack(side="right", fill="both", expand=True)

        campos = [
            "Tipo de movimento (Ex: entrada, saída ou transferência): ",
            "Data e hora (Ex: data - hora): ",
            "Número de produtos movimentados: ",
            "Local de estoque: ",
            "Usuário responsável: "
        ]

        for titulo in campos:
            self._criar_secao_textbox(titulo)

    def _criar_secao_textbox(self, titulo):
        frame = tk.Frame(self.main_frame, bg="#1f1f1f")
        frame.pack(fill="x", pady=10, padx=20)

        
        title_label = tk.Label(
            frame,
            text=titulo,
            bg="#8c8c8c",
            fg="white",
            font=("Arial", 12, "bold"),
            anchor="w",
            padx=10,
            pady=5
        )
        title_label.pack(fill="x", pady=5)

        
        textbox = tk.Text(frame, height=4, bg="#c9c9c9", font=("Arial", 11))
        textbox.pack(fill="x")

    
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