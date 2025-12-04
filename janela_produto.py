import tkinter as tk
from tkinter import Tk, Button, Frame, PhotoImage, Label, Entry, messagebox
from cadastro import Produto  
from persistencia import PersistenciaProduto, ProdutoRepetidoException

class JanelaProduto(Tk):
    def __init__(self):
        super().__init__()
        self.configurar_janela()
        self.configurar_background()
        self.configurar_barra_lateral()
        self.configurar_botoes_laterais()
        self.configurar_titulo()
        self.configurar_entry_cadastro()
        self.configurar_botao_salvar()
        
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
        
        self.icon_inicio = PhotoImage(file='icons/home.png')
        self.icon_produtos = PhotoImage(file='icons/bag.png')
        self.icon_fornecedores = PhotoImage(file='icons/3_user.png')
        self.icon_estoque = PhotoImage(file='icons/folder.png')
        self.icon_movimentacao = PhotoImage(file='icons/chart.png')
        self.icon_relatorio = PhotoImage(file='icons/paper.png')
        
        estilo_template = {
            "relief": "flat",
            "bg": "#444444",
            "activebackground": "#555555",
            "bd": 0,
            "fg": "#FFFFFF",
            "activeforeground": "#FFFFFF",
            "font": ("Inter", 17, "bold"),
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
            image=self.icon_produtos
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

    def configurar_titulo(self):
        lb_titulo = Label(
            self,
            text='Cadastro de Produtos',
            bg='#838181',
            fg='#FFFFFF',
            font=('Inter', 50, 'bold'),
            anchor='center'
        )
        lb_titulo.place(relx=0.40,rely=0.05, height=150)

    def configurar_entry_cadastro(self):
        self.campos = [
            'Nome', 'Categoria', 'Preço Compra', 'Preço Venda',
            'Quantidade', 'Fornecedor', 'Estoque mínimo'
        ]
        self.entries = {}

        for i, campo in enumerate(self.campos):
            frame = Frame(self, bg='#161515')
            frame.place(relx=0.18, rely=0.22 + i * 0.095)

            Label(frame, text=campo, font=("Inter", 16), fg="white", bg="#161515", anchor='w').pack()
            entry = Entry(frame, font=("Inter", 14), bg="#222", fg="white", width=28, relief="solid", bd=1, insertbackground="cyan")
            entry.pack(pady=(2, 5))

            self.entries[campo] = entry
            
    def configurar_botao_salvar(self):
        self.bt_salvar = Button(
            self, text="Salvar Cadastro", font=("Inter", 18, "bold"),
            bg="#00aaff", fg="black", cursor="hand2",
            command=self.salvar_cadastro
        )
        self.bt_salvar.place(relx=0.5, rely=0.9, anchor='center', width=280, height=50)
                   
    def salvar_cadastro(self):
        try:
            nome = self.entries["Nome"].get().strip().capitalize()
            categoria = self.entries["Categoria"].get().strip().capitalize()
            preco_compra = float(self.entries["Preço Compra"].get().replace(",", "."))
            preco_venda = float(self.entries["Preço Venda"].get().replace(",", "."))
            qtd = int(self.entries["Quantidade"].get())
            fornecedor = self.entries["Fornecedor"].get().strip().capitalize()
            estoque_minimo = int(self.entries["Estoque mínimo"].get())

            produto = Produto(nome, categoria, preco_compra, preco_venda, qtd, fornecedor, estoque_minimo)

            persist = PersistenciaProduto()
            persist.adicionar(produto)

            messagebox.showinfo("Sucesso", "Produto salvo no JSON!")
            print(produto.para_dict())

        except ProdutoRepetidoException as e:
            messagebox.showwarning("Produto repetido", str(e))

        except ValueError:
            messagebox.showerror("Erro", "Preencha corretamente os campos numéricos!")
            try:
                nome = self.entries["Nome"].get().strip().capitalize()
                categoria = self.entries["Categoria"].get().strip().capitalize()
                preco_compra = float(self.entries["Preço Compra"].get().replace(",", "."))
                preco_venda = float(self.entries["Preço Venda"].get().replace(",", "."))
                qtd = int(self.entries["Quantidade"].get())
                fornecedor = self.entries["Fornecedor"].get().strip().capitalize()
                estoque_minimo = int(self.entries["Estoque mínimo"].get())

                produto = Produto(
                    nome=nome,
                    categoria=categoria,
                    preco_compra=preco_compra,
                    preco_venda=preco_venda,
                    qtd=qtd,
                    fornecedor=fornecedor,
                    estoque_minimo=estoque_minimo
                )

                persist = PersistenciaProduto()
                persist.adicionar(produto)

                messagebox.showinfo("Sucesso", "Produto cadastrado no JSON!")
                print("Salvo:", produto.para_dict())
                                    
                for ent in self.entries.values():
                    ent.delete(0, tk.END)


            except ProdutoRepetidoException as e:
                messagebox.showwarning("Produto repetido", str(e))

            except ValueError:
                messagebox.showerror("Erro", "Verifique os campos numéricos (preços, quantidade e estoque mínimo)!")
                
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
        
    def janela_movimentacao(self):
        from janela_movimentacao import JanelaMovimentacao
        self.destroy()
        j = JanelaMovimentacao()

    def janela_relatorios(self):
        from janela_relatorios import JanelaRelatorios
        self.destroy()
        j = JanelaRelatorios()
