import tkinter as tk
from tkinter import messagebox

class InterfaceGrafica:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("Agenda de Contatos")

        self.controller = controller

        self.nome_var = tk.StringVar()
        self.sobrenome_var = tk.StringVar()
        self.aniversario_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.telefone_var = tk.StringVar()
        self.descricao_var = tk.StringVar()

        tk.Label(root, text="Nome:").pack()
        self.nome_entry = tk.Entry(root, textvariable=self.nome_var)
        self.nome_entry.pack()

        tk.Label(root, text="Sobrenome:").pack()
        self.sobrenome_entry = tk.Entry(root, textvariable=self.sobrenome_var)
        self.sobrenome_entry.pack()

        tk.Label(root, text="Aniversário:").pack()
        self.aniversario_entry = tk.Entry(root, textvariable=self.aniversario_var)
        self.aniversario_entry.pack()

        tk.Label(root, text="Email:").pack()
        self.email_entry = tk.Entry(root, textvariable=self.email_var)
        self.email_entry.pack()

        tk.Label(root, text="Telefone:").pack()
        self.telefone_entry = tk.Entry(root, textvariable=self.telefone_var)
        self.telefone_entry.pack()

        tk.Label(root, text="Descrição:").pack()
        self.descricao_entry = tk.Entry(root, textvariable=self.descricao_var)
        self.descricao_entry.pack()

        self.contatos_listbox = tk.Listbox(root, font='Times 24')
        self.contatos_listbox.pack(pady=10)

        self.adicionar_button = tk.Button(root, text="Adicionar", relief='groove', fg='white', bg='green', command=self.adicionar_contato)
        self.adicionar_button.pack(side='left')

        self.atualizar_button = tk.Button(root, text="Atualizar", relief='groove', fg='black', bg='yellow', command=self.atualizar_contato)
        self.atualizar_button.pack(side='left')

        self.excluir_button = tk.Button(root, text="Excluir", relief='groove', fg='black', bg='red', command=self.excluir_contato)
        self.excluir_button.pack(side='left')

        self.carregar_contatos()

        self.contatos_listbox.bind('<Double-Button-1>', self.carregar_detalhes_contato)

    def carregar_contatos(self):
        self.contatos_listbox.delete(0, tk.END)
        contatos = self.controller.obter_contatos()
        for contato in contatos:
            self.contatos_listbox.insert(tk.END, f"{contato[1]} {contato[2]}")

    def adicionar_contato(self):
        nome = self.nome_var.get()
        sobrenome = self.sobrenome_var.get()
        aniversario = self.aniversario_var.get()
        email = self.email_var.get()
        telefone = self.telefone_var.get()
        descricao = self.descricao_var.get()

        if not nome or not sobrenome:
            print("Nome e Sobrenome são campos obrigatórios.")
            messagebox.showinfo("Alerta", "Nome e Sobrenome são campos obrigatórios.")
            return

        self.controller.adicionar_contato(nome, sobrenome, aniversario, email, telefone, descricao)
        self.carregar_contatos()

    def atualizar_contato(self):
        index = self.contatos_listbox.curselection()
        if index:
            contato_id = self.controller.obter_contatos()[index[0]][0]
            nome = self.nome_var.get()
            sobrenome = self.sobrenome_var.get()
            aniversario = self.aniversario_var.get()
            email = self.email_var.get()
            telefone = self.telefone_var.get()
            descricao = self.descricao_var.get()

            self.controller.atualizar_contato(contato_id, nome, sobrenome, aniversario, email, telefone, descricao)
            self.limpar_entradas()
            self.carregar_contatos()

    def excluir_contato(self):
        index = self.contatos_listbox.curselection()
        if index:
            contato_id = self.controller.obter_contatos()[index[0]][0]
            self.controller.excluir_contato(contato_id)
            self.limpar_entradas()
            self.carregar_contatos()

    def carregar_detalhes_contato(self, event):
        index = self.contatos_listbox.curselection()
        if index:
            contato_id = self.controller.obter_contatos()[index[0]][0]
            self.preencher_entradas(contato_id)

    def preencher_entradas(self, contato_id):
        contato = self.controller.obter_contato_por_id(contato_id)
        self.nome_var.set(contato.nome)
        self.sobrenome_var.set(contato.sobrenome)
        self.aniversario_var.set(contato.aniversario)
        self.email_var.set(contato.email)
        self.telefone_var.set(contato.telefone)
        self.descricao_var.set(contato.descricao)

    def limpar_entradas(self):
        self.nome_var.set('')
        self.sobrenome_var.set('')
        self.aniversario_var.set('')
        self.email_var.set('')
        self.telefone_var.set('')
        self.descricao_var.set('')

