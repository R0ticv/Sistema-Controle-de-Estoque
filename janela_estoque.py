import tkinter as tk
from tkinter import Tk, Frame, PhotoImage, Button, messagebox, ttk, Label, Toplevel
from persistencia import *
from cadastro import *


class JanelaEstoque(Tk):
    def __init__(self):
        super().__init__()
        self.configurar_janela()
        self.configurar_background()
        self.configurar_barra_lateral()
        self.configurar_botoes_laterais()
        self.configurar_tabela()
        self.configurar_menu_contexto()
        self.atualizar_status_todos()
        self.carregar_produtos_na_tabela()
      
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
        self.button_inicio.pack(padx=30, pady=5,anchor='w')
        
        self.button_produto = Button(
            self.quadro1,
            text='Produtos',
            **estilo_template,
            image=self.icon_produtos,
            command=self.janela_produto
        )
        
        self.button_produto.pack(padx=30, pady=5,anchor='w')
        
        
        self.button_fornecedores = Button(
            self.quadro1,
            text='Fornecedores',
            **estilo_template,
            image=self.icon_fornecedores,
            command=self.janela_fornecedores
        )
        self.button_fornecedores.pack(pady=5, padx=30,anchor='w')
        
        
        self.button_estoque = Button(
            self.quadro1,
            text='Estoque',
            **estilo_template,
            image=self.icon_estoque
        )
        self.button_estoque.pack(padx=30, pady=5,anchor='w')
        
        
        self.button_movimentacao = Button(
            self.quadro1,
            text='Movimentação',
            **estilo_template,
            image=self.icon_movimentacao,
            command=self.janela_movimentacao
        )
        self.button_movimentacao.pack(padx=30, pady=5,anchor='w')
        
        
        self.button_relatorio = Button(
            self.quadro1,
            text='Relatórios',
            **estilo_template,
            image=self.icon_relatorio,
            command=self.janela_relatorio
        )
        self.button_relatorio.pack(padx=30, pady=5,anchor='w')

    def configurar_menu_contexto(self):
        self.menu = tk.Menu(self, tearoff=False)
        self.menu.add_command(label="Editar produto", command=self.update_produto_contexto)
        self.menu.add_command(label="Deletar produto", command=self.deletar_produto_contexto)

        self.tree.bind("<Button-3>", self.abrir_menu) 
  
    def abrir_menu(self, event):
        row_id = self.tree.identify_row(event.y)
        if row_id:
            self.tree.selection_set(row_id)
            self.tree.focus(row_id)
            self.row_clicada = row_id 
            self.menu.tk_popup(event.x_root, event.y_root)
            
    def abrir_edicao_contexto(self):
        if not hasattr(self, "row_clicada"):
            return

        item = self.tree.item(self.row_clicada)["values"]
        self.abrir_edicao(item[0])
            
    def configurar_tabela(self):
        self.quadro2 = Frame(self, borderwidth=1, relief='flat', background="#FDFDFD")
        self.quadro2.place(relx=0.143, rely=0.19,relwidth=0.848, relheight=0.8)
        self.tree = ttk.Treeview(self.quadro2,show='headings', selectmode='browse')
        colunas = ('id', 'nome do produto', 'quantidade', 'preço', 'status')
        self.tree['columns'] = colunas
        
        for col in colunas:
            self.tree.heading(col, text=col.capitalize(), anchor='center', )
            
        scroll_y = ttk.Scrollbar(self.quadro2, orient="vertical", command=self.tree.yview)
        
        self.tree.configure(yscrollcommand=scroll_y.set)
            
        self.tree.column('id', width=230, minwidth=230, anchor='center', stretch=False)
        self.tree.column('nome do produto', width=693, minwidth=693,anchor='center',stretch=False)
        self.tree.column('quantidade', width=200, minwidth=200, anchor='center', stretch=False)
        self.tree.column('preço', width=200, minwidth=200, anchor='center', stretch=False)
        self.tree.column('status', width=300, minwidth=300, anchor='center', stretch=False)
        
        self.tree.column('#0', width=0, stretch=False)
        
        self.tree.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")

        self.quadro2.rowconfigure(0, weight=1)
        self.quadro2.columnconfigure(0, weight=1)
        
    def carregar_produtos_na_tabela(self):
        persist = PersistenciaProduto()
        produtos = persist.ler()  
        for produto in produtos:
            status = 'Disponível' if int(produto['qtd']) > int(produto['estoque_minimo']) else 'Baixo estoque'

            self.tree.insert('', 'end', iid=produto['id'], values=(
                produto["id"],
                produto["nome"],
                produto["qtd"],
                f'R${produto["preco_venda"]:.2f}',
                status
            ))
            
    def obter_selecionado(self):
        selecionado = self.tree.focus()
        if not selecionado:
            return None
        valores = self.tree.item(selecionado)["values"]
        return {
            "id": valores[0],
            "nome": valores[1],
            "categoria": valores[2],
            "qtd": valores[3],
            "preco_compra": float(valores[4].replace("R$","")),
            "preco_venda": float(valores[5].replace("R$",""))
        }
    
    def adicionar_produto(self):
        try:
            p = Produto(
                self.e_nome.get(),
                self.e_cat.get(),
                float(self.e_pc.get()),
                float(self.e_pv.get()),
                int(self.e_qtd.get()),
                self.e_forn.get(),
                int(self.e_min.get())
            )

            persist = PersistenciaProduto()
            persist.adicionar(p) 

            status = 'Disponível' if int(p.qtd) > int(p.estoque_minimo) else 'Baixo estoque'

            self.tree.insert("", "end", iid=p.id, values=(
                p.id,
                p.nome,
                p.qtd,
                f"R$ {p.preco_venda:.2f}",
                status
            ))

            messagebox.showinfo("Sucesso", "Produto salvo e inserido na tabela!")

        except Exception as e:
            messagebox.showerror("Erro ao adicionar", str(e))
    
    def deletar_produto_contexto(self):
        if not hasattr(self, "row_clicada"):
            messagebox.showwarning("Atenção", "Selecione um item primeiro!")
            return

        certeza = messagebox.askyesno("Confirmar exclusão", "Tem certeza que deseja excluir este produto?")
        if not certeza:
            return

        persist = PersistenciaProduto()
        produtos = persist.ler()

        nova_lista = [p for p in produtos if p["id"] != self.row_clicada]
        persist.salvar(nova_lista)

        self.tree.delete(self.row_clicada)

        messagebox.showinfo("Sucesso", "Produto excluído com sucesso!") 
        
    def update_produto_contexto(self):
        if not hasattr(self, "row_clicada"):
            messagebox.showwarning("Atenção","Selecione um item primeiro!")
            return

        valores = self.tree.item(self.row_clicada)["values"]

        self.jan_edit = Toplevel(self)
        self.jan_edit.title("Editar produto")
        self.jan_edit.configure(bg="#222")
        self.jan_edit.geometry("350x300")
        self.jan_edit.resizable(False, False)

        Label(self.jan_edit, text="Nome", bg="#222", fg="white").pack(pady=5)
        self.ed_nome = ttk.Entry(self.jan_edit)
        self.ed_nome.pack()
        self.ed_nome.insert(0, valores[1])

        Label(self.jan_edit, text="Quantidade", bg="#222", fg="white").pack(pady=5)
        self.ed_cat = ttk.Entry(self.jan_edit)
        self.ed_cat.pack()
        self.ed_cat.insert(0, valores[2])

        Label(self.jan_edit, text="Preço Venda", bg="#222", fg="white").pack(pady=5)
        self.ed_qtd = ttk.Entry(self.jan_edit)
        self.ed_qtd.pack()
        self.ed_qtd.insert(0, valores[3])


        Button(self.jan_edit, text="Salvar alterações", bg="#555", fg="white", relief="flat",
            command=self.salvar_update).pack(pady=15)
        
    def salvar_update(self):
        id_prod = self.row_clicada 
        nome = self.ed_nome.get().strip()
        qtd = self.ed_cat.get().strip()
        preco_venda = self.ed_qtd.get().strip()

        if not nome or not qtd.isdigit():
            messagebox.showerror("Erro", "Nome ou quantidade inválidos!")
            return

        try:
            preco_venda = float(preco_venda)
        except:
            messagebox.showerror("Erro", "Preço de venda precisa ser um número!")
            return

        persist = PersistenciaProduto()
        produtos = persist.ler()

        produto_atualizado = None

        for i, p in enumerate(produtos):
            if p["id"] == id_prod:
                produtos[i]["nome"] = nome
                produtos[i]["qtd"] = int(qtd)
                produtos[i]["preco_venda"] = preco_venda

                minimo = produtos[i]["estoque_minimo"]
                status = "Disponível" if produtos[i]["qtd"] > minimo else "Baixo estoque"
                produtos[i]["status"] = status

                produto_atualizado = produtos[i]
                break

        persist.salvar(produtos)

        self.tree.item(id_prod, values=(
            id_prod,
            produto_atualizado["nome"],
            produto_atualizado["qtd"],
            f"R$ {produto_atualizado['preco_venda']:.2f}",
        ))

        self.jan_edit.title(f"Editar produto - {produto_atualizado['status']}")

        messagebox.showinfo("Sucesso", "Produto atualizado e salvo no JSON!")
        self.jan_edit.destroy()
        
    def atualizar_status_todos(self):
        persist = PersistenciaProduto()
        produtos = persist.ler()

        for p in produtos:
            minimo = p["estoque_minimo"]
            status = "Disponível" if p["qtd"] > minimo else "Baixo estoque"
            p["status"] = status
            persist.atualizar_todos = True

        persist.salvar(produtos) 
        
    def voltar_janela_inicio(self):
        from janela_inico import JanelaInicio
        self.destroy()
        j = JanelaInicio()
        
    def janela_fornecedores(self):
        from janela_fornecedores import JanelaFornecedores
        self.destroy()
        j = JanelaFornecedores()
        
    def janela_produto(self):
        from janela_produto import JanelaProduto
        self.destroy()
        j = JanelaProduto()
    
    def janela_movimentacao(self):
        from janela_movimentacao import JanelaMovimentacao
        self.destroy()
        j = JanelaMovimentacao()
    
    def janela_relatorio(self):
        from janela_relatorios import JanelaRelatorios
        self.destroy()
        j = JanelaRelatorios()