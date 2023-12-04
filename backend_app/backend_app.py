from tkinter import ttk, messagebox
from tkinter import *
import sqlite3



class Login:
    def __init__(self, root):
        self.janela = root
        self.janela.title('App Gestor - Luxury Wheels')
        self.janela.resizable(1,1)
        self.janela.wm_iconbitmap('recursos/Flying_car.ico')
        self.janela.geometry('400x400')

        # Criação do Frame principal e centralização no meio da janela
        frame = LabelFrame(self.janela, text='Login')
        frame.place(relx=0.5, rely=0.5, anchor='center')

        # Label usuario
        self.etiqueta_user = ttk.Label(frame, text='Usuário: ')
        self.etiqueta_user.grid(row=1, column=0)
        # Entry usuario
        self.user = ttk.Entry(frame)
        self.user.focus()
        self.user.grid(row=1, column=1)

        # Label senha
        self.etiqueta_senha = ttk.Label(frame, text='Senha: ')
        self.etiqueta_senha.grid(row=2, column=0)
        # Entry senha
        self.senha = ttk.Entry(frame, show='*')
        self.senha.grid(row=2, column=1)

        # Botão de Login
        self.botao_login = ttk.Button(frame, text='Login', command=self.verificar_login)
        self.botao_login.grid(row=3, columnspan=2, sticky=W+E)

    def verificar_login(self):
        usuario_digitado = self.user.get()
        senha_digitada = self.senha.get()

        # Verificação do usuario e senha digitada
        resultado = True if usuario_digitado == 'ADMIN' and senha_digitada == 'admin123' else False

        (self.limpar_janela(), Dashboard(self.janela)) if resultado else messagebox.showerror('Erro de Login', 'Usuário ou senha digitados não conferem!')

    def limpar_janela(self):
        # Eliminar os elementos do Frame Login
        [widget.destroy() for widget in self.janela.winfo_children()]


class Dashboard:
    def __init__(self, root):
        self.janela = root
        self.janela.title('Dashboard - Luxury Wheels')
        self.janela.geometry('600x400')
        self.janela.resizable(1, 1)
        # Botões para gerenciamento das tabelas no Banco de dados
        self.botao_veiculos = ttk.Button(self.janela, text='Gerir Veículos', command=self.gerir_veiculos)
        self.botao_veiculos.grid(row=0, column=0, padx=20)
        self.botao_usuarios = ttk.Button(self.janela, text='Gerir Usuários', command=self.iniciar_gerir_usuarios)
        self.botao_usuarios.grid(row=0, column=1, padx=20)
        # ... precisa ainda colocar outros elementos do Dashboard

    def iniciar_gerir_usuarios(self):
        GerirUsuarios(self.janela)  # Inicie a classe GerirUsuarios com a janela principal

    def gerir_veiculos(self):
        pass
        # implementar lógica para gerir veiculos


class GerirUsuarios:
    db = 'database/luxury_wheels.db'

    def __init__(self, root):
        self.janela = root
        self.on_back = on_back
        self.janela.title('Gestão Avançada de Usuários - Luxury Wheels')
        self.janela.geometry('800x500')
        self.janela.columnconfigure(0, weight=0)  # Ajusta a primeira coluna
        self.janela.columnconfigure(1, weight=0)  # Ajusta a segunda coluna
        self.janela.columnconfigure(2, weight=0)  # Ajusta a terceira coluna
        self.janela.columnconfigure(3, weight=1)  # Ajusta a quarta coluna

        # Botão de inclusão de usuario
        self.botao_incluir_user = ttk.Button(self.janela, text='Incluir Usuário', command=self.incluir_user, style='my.TButton')
        self.botao_incluir_user.grid(row=0, column=0)

        # Botão para apagar usuario
        self.botao_del_user = ttk.Button(self.janela, text='Apagar Usuário', command=self.del_user, style='my.TButton')
        self.botao_del_user.grid(row=0, column=1)

        # Botão para editar usuario
        self.botao_edit_user = ttk.Button(self.janela, text='Editar Usuário', command=self.edit_user, style='my.TButton')
        self.botao_edit_user.grid(row=0, column=2)

        # Botão para voltar à janela anterior (Dashboard)
        self.botao_voltar = ttk.Button(self.janela, text='Voltar', command=self.voltar_dashboard, style='my.TButton')
        self.botao_voltar.grid(row=0, column=3)

        # Tabela de Produtos
        # Estilo personalizado para a tabela
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 11))  # Modifica-se a fonte da tabela
        style.configure("mystyle.Treeview.Heading",
                        font=('Calibri', 13, 'bold'))  # Modifica - se a fonte das cabeceiras
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Eliminar as bordas
        # Estrutura da tabela
        self.tabela = ttk.Treeview(height=20, columns=5, style="mystyle.Treeview")
        self.tabela["columns"] = ("Nome", "User", "Email", "categoria")
        self.tabela.grid(row=4, column=0, columnspan=5)
        self.tabela.heading('#0', text='Nome', anchor=CENTER)  # Cabeçalho 0
        self.tabela.heading('#1', text='User', anchor=CENTER)  # Cabeçalho 1
        self.tabela.heading('#2', text='Email', anchor=CENTER)  # Cabeçalho 2
        self.tabela.heading('#3', text='Categoria', anchor=CENTER)  # Cabeçalho 3
        # Chamada ao método get_users() para obter a listagem de usuarios
        self.get_users()

    def voltar_dashboard(self):
        self.janela.destroy()  # Destrói a janela atual
        Dashboard(self.janela) # Cria uma nova instância do Dashboard

    def db_consulta(self, consulta, parametros=()):
        with sqlite3.connect(self.db) as con:  # Iniciamos uma conexão com a base de dados (alias con)
            cursor = con.cursor()   # criamos um cursor da conexão para poder operar na base de dados
            resultado = cursor.execute(consulta, parametros)  # Preparar a consulta SQL (com parametros se os há)
            con.commit()  # executar a consulta SQL, preparada anteriormente
            return resultado  # restituir o resultado da consulta SQL

    def get_users(self):
        # O primeiro, ao inicia a app, vamos limpar a tabela se tiver dados residuais ou antigos, de consultas
        registos_tabela = self.tabela.get_children()  # Obter todos os dados da tabela
        for linha in registos_tabela:
            self.tabela.delete(linha)

        # Consulta SQL
        query = 'SELECT * FROM users'
        registos_db = self.db_consulta(query)  # Faz-se a chamada ao método db_consultas

        # Escrever os dados no Ecrã
        for linha in registos_db:
            self.tabela.insert('', 'end', text=linha[1], values=(linha[2], linha[3], linha[5]))

    def incluir_user(self):
        pass

    def edit_user(self):
        pass

    def del_user(self):
        pass


if __name__ == '__main__':
    root = Tk()
    app = Login(root)
    root.mainloop()

