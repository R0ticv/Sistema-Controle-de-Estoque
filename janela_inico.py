from tkinter import * 
from tkinter import ttk, Button, Label, Entry

class JanelaInicio(Tk):
    def __init__(self):
        super().__init__()
        self.configurar_janela()
        self.configurar_background()
        self.configurar_barra_lateral()
        self.configurar_botoes_laterais()
        self.configurar_botao_criar()
        self.configurar_botao_fornecedor()
        self.configurar_botao_bemvindo()
    
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
            image=self.icon_inicio
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
            image=self.icon_movimentacao,
            command=self.janela_movimentacao
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
        
    def configurar_botao_criar(self):
        bt_criar = Button(self, text='Clique aqui',font=('Arial Bold',55), bg='#FF991c', fg='black', command=self.janela_produto)
        bt_criar.place(relx=0.65, rely = 0.4, width = 450, heigh= 200)
        
        lb_criar = Label(
            self,
            text='Cadastre\nUm Produto',
            bg='#838181',
            fg='#FFFFFF',
            font=('Inter', 40, 'bold'),
            anchor='center'
                         )
        lb_criar.place(relx=0.65,rely=0.25,width = 450, heigh= 150)

    def configurar_botao_fornecedor(self):
        bt_fornecedor = Button(self, text='Clique aqui',font=('Arial Bold',55), bg='#FF991c', fg='black', command=self.janela_fornecedores)
        bt_fornecedor.place(relx=0.25, rely = 0.4, width = 450, heigh= 200)
        
        lb_fornecedor = Label(
            self,
            text='Cadastre\nUm Fornecedor',
            bg='#838181',
            fg='#FFFFFF',
            font=('Inter', 40, 'bold'),
            anchor='center'
                         )
        lb_fornecedor.place(relx=0.25,rely=0.25,width = 450, heigh= 150)
        
    def configurar_botao_bemvindo(self):
        
        lb_titulo = Label(
            self,
            text='Bem Vindo',
            bg='#838181',
            fg='#FFFFFF',
            font=('Inter', 50, 'bold'),
            anchor='center'
                         )
        lb_titulo.place(relx=0.45,rely=0.05,width = 450, heigh= 150)
        
    def janela_estoque(self):
        from janela_estoque import JanelaEstoque
        self.destroy()
        j = JanelaEstoque()

    def janela_fornecedores(self):
        from janela_fornecedores import JanelaFornecedores
        self.destroy()
        j = JanelaFornecedores()
        
    def janela_movimentacao(self):
        from janela_movimentacao import JanelaMovimentacao
        self.destroy()
        j = JanelaMovimentacao()
        
    def janela_produto(self):
        from janela_produto import JanelaProduto
        self.destroy()
        j = JanelaProduto()
            
    def janela_relatorios(self):
        from janela_relatorios import JanelaRelatorios
        self.destroy()
        j = JanelaRelatorios()
