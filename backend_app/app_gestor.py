from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter.ttk import Treeview
from datetime import date
import pandas as pd


class Funcs:
    def limpa_formulario(self):
        # Função para limpar os campos do formulário ao clicar no botão limpar campos
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.categoria_entry.delete(0, END)

    def limpa_formulario_veiculos(self):
        # Função para limpar os campos do formulário ao clicar no botão limpar campos
        self.id_veiculo_entry.delete(0, END)
        self.nome_veiculo_entry.delete(0, END)
        self.cat_veiculo_entry.delete(0, END)
        self.diaria_aluguer_entry.delete(0, END)
        self.imagem_veiculo_entry.delete(0, END)
        self.km_veiculo_entry.delete(0, END)
        self.km_manut_veiculo_entry.delete(0, END)
        self.data_inicio_manut_entry.delete(0, END)
        self.data_final_manut_entry.delete(0, END)
        self.data_licenciamento_entry.delete(0, END)
        self.disponibilidade_veic_entry.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect('C://Users//julio//PycharmProjects//LuxuryWheels_Project//backend_app//database//luxury_wheels.db')
        self.cursor = self.conn.cursor()

    def mostra_clientes_bd(self):
        self.lista_clientes.delete(*self.lista_clientes.get_children())
        self.conecta_bd()
        lista_users = self.cursor.execute(""" SELECT id, name, username, email, categoria FROM users ORDER BY name ASC;""")
        for i in lista_users:
            self.lista_clientes.insert("", END, values=(i[0], i[1], i[2], i[3], i[4]))
        self.conn.close()

    def mostra_veiculos_bd(self):
        self.lista_veiculos.delete(*self.lista_veiculos.get_children())
        self.conecta_bd()
        lista_veiculos_bd = self.cursor.execute(""" SELECT id, nome, categoria, preco, imagem, quilometragem, manutencao, 
                                                data_inicio_manut, data_final_manut, licenciamento, 
                                                disponibilidade FROM veiculos ORDER BY nome ASC;""")
        for i in lista_veiculos_bd:
            self.lista_veiculos.insert("", END, values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
        self.conn.close()

    def OnDoubleClick(self, event):
        for n in self.lista_clientes.selection():
            col1, col2, col3, col4, col5 = self.lista_clientes.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.username_entry.insert(END, col3)
            self.email_entry.insert(END, col4)
            self.categoria_entry.insert(END, col5)

    def OnDoubleClickVeiculo(self, event):
        for n in self.lista_veiculos.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11 = self.lista_veiculos.item(n, 'values')
            self.id_veiculo_entry.insert(END, col1)
            self.nome_veiculo_entry.insert(END, col2)
            self.cat_veiculo_entry.insert(END, col3)
            self.diaria_aluguer_entry.insert(END, col4)
            self.imagem_veiculo_entry.insert(END, col5)
            self.km_veiculo_entry.insert(END, col6)
            self.km_manut_veiculo_entry.insert(END, col7)
            self.data_inicio_manut_entry.insert(END, col8)
            self.data_final_manut_entry.insert(END, col9)
            self.data_licenciamento_entry.insert(END, col10)
            self.disponibilidade_veic_entry.insert(END, col11)

    def captura_dados_veiculos_entry(self):
        self.id_veic = self.id_veiculo_entry.get()
        self.nome_veic = self.nome_veiculo_entry.get()
        self.cat_veic = self.cat_veiculo_entry.get()
        self.diaria_veic = self.diaria_aluguer_entry.get()
        self.imagem_veic = self.imagem_veiculo_entry.get()
        self.km_veic = self.km_veiculo_entry.get()
        self.km_manut_veic = self.km_manut_veiculo_entry.get()
        self.inicio_manut_veic = self.data_inicio_manut_entry.get()
        self.final_manut_veic = self.data_final_manut_entry.get()
        self.licenc_veic = self.data_licenciamento_entry.get()
        self.dispon_veic = self.disponibilidade_veic_entry.get()

    def captura_dados_entry(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.username = self.username_entry.get()
        self.email = self.email_entry.get()
        self.categoria = self.categoria_entry.get()

    def deleta_cliente(self):
        self.captura_dados_entry()
        self.conecta_bd()
        self.cursor.execute(""" DELETE FROM users WHERE id = ? """, (self.codigo,))
        self.conn.commit()
        self.conn.close()
        self.mostra_clientes_bd()
        self.limpa_formulario()

    def deleta_veiculo(self):
        self.captura_dados_veiculos_entry()
        self.conecta_bd()
        self.cursor.execute(""" DELETE FROM veiculos WHERE id = ? """, (self.id_veic,))
        self.conn.commit()
        self.conn.close()
        self.mostra_veiculos_bd()
        self.limpa_formulario_veiculos()

    def altera_cliente(self):
        self.captura_dados_entry()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE users SET name = ?, username = ?, email = ?, categoria = ? WHERE id = ? """,
                            (self.nome, self.username, self.email, self.categoria, self.codigo))
        self.conn.commit()
        self.conn.close()
        self.mostra_clientes_bd()
        self.limpa_formulario()

    def altera_veiculo(self):
        self.captura_dados_veiculos_entry()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE veiculos SET nome = ?, categoria = ?, preco = ?, imagem = ?, 
        quilometragem = ?, manutencao = ?, data_inicio_manut = ?, data_final_manut = ?, licenciamento = ?, 
        disponibilidade = ? WHERE id = ? """, (self.nome_veic, self.cat_veic, self.diaria_veic,
                                               self.imagem_veic, self.km_veic, self.km_manut_veic,
                                               self.inicio_manut_veic, self.final_manut_veic, self.licenc_veic,
                                               self.dispon_veic, self.id_veic))
        self.conn.commit()
        self.conn.close()
        self.mostra_veiculos_bd()
        self.limpa_formulario_veiculos()
        self.update_disponibilidade_veic()

    def busca_cliente(self):
        self.conecta_bd()
        self.lista_clientes.delete(*self.lista_clientes.get_children())
        self.nome_entry.insert(END, '%')  # Inclusão do % nas pesquisas para aumentar abrangencia
        nome = self.nome_entry.get()
        self.cursor.execute(""" SELECT id, name, username, email, categoria FROM users WHERE name LIKE '%s' 
                            ORDER BY name ASC """ % nome)
        busca_nome_user = self.cursor.fetchall()
        for i in busca_nome_user:
            self.lista_clientes.insert("", END, values=i)
        self.limpa_formulario()
        self.conn.close()

    def busca_veiculo(self):
        self.conecta_bd()
        self.lista_veiculos.delete(*self.lista_veiculos.get_children())
        self.nome_veiculo_entry.insert(END, '%')  # Inclusão do % nas pesquisas para aumentar abrangencia
        nome_veiculo = self.nome_veiculo_entry.get()
        self.cursor.execute(""" SELECT id, nome, categoria, preco, imagem, quilometragem, manutencao, 
                            data_inicio_manut, data_final_manut, licenciamento, disponibilidade FROM veiculos 
                            WHERE nome LIKE '%s' ORDER BY nome ASC """ % nome_veiculo)
        busca_nome_veiculo = self.cursor.fetchall()
        for i in busca_nome_veiculo:
            self.lista_veiculos.insert("", END, values=i)
        self.limpa_formulario_veiculos()
        self.conn.close()

    def inclui_veiculo(self):
        self.captura_dados_veiculos_entry()
        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO veiculos (nome, categoria, preco, imagem, quilometragem, manutencao, 
                            data_inicio_manut, data_final_manut, licenciamento, disponibilidade) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (self.nome_veic, self.cat_veic,
                                                                       self.diaria_veic, self.imagem_veic, self.km_veic,
                                                                       self.km_manut_veic, self.inicio_manut_veic,
                                                                       self.final_manut_veic, self.licenc_veic,
                                                                       self.dispon_veic))
        self.conn.commit()
        self.conn.close()
        self.mostra_veiculos_bd()
        self.limpa_formulario_veiculos()
        self.update_disponibilidade_veic()

    def update_disponibilidade_veic(self):
        current_date = date.today().isoformat()
        self.conecta_bd()
        # Encontrar veiculos que estejam com quilometragem em manutencao ou entre as datas de manutencao
        query = """ UPDATE veiculos SET disponibilidade = 'nao' WHERE quilometragem = manutencao 
                    OR ? BETWEEN data_inicio_manut AND data_final_manut """
        self.cursor.execute(query, (current_date,))
        self.conn.commit()
        self.conn.close()


class Application(Funcs):
    def __init__(self, root):
        self.janela = root
        self.config_janela()
        self.configura_menu()
        self.update_disponibilidade_veic()
        self.executa_login()

    def config_janela(self):
        self.janela.title('App Gestor - Luxury Wheels')
        self.janela.configure(bg='#C5D4EB')
        self.janela.resizable(1, 1)
        self.janela.wm_iconbitmap('recursos/Flying_car.ico')
        self.janela.geometry('400x400')
        self.janela.minsize(width=400, height=300)
        self.janela.maxsize(width=1024, height=768)

    def configura_menu(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar)

        def sair_aplicativo():
            self.janela.destroy()

        menubar.add_cascade(label="Sair", menu=filemenu)
        filemenu.add_command(label="Sair", command=sair_aplicativo)

    def executa_login(self):
        # Criação do Frame Login
        self.frame1 = Frame(self.janela, bd=6, highlightthickness=2, highlightcolor='#6C85BD')
        self.frame1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
        self.etiqueta_login = Label(self.frame1, text='Fazer Login:', font=("roboto", 14))
        self.etiqueta_login.place(relx=0.33, rely=0.05)

        # Entry usuario
        self.label_user = Label(self.frame1, text='Usuário:')
        self.label_user.place(relx=0.1, rely=0.22)
        self.user = Entry(self.frame1)
        self.user.focus()
        self.user.place(relx=0.1, rely=0.28, relwidth=0.8)

        # Entry senha
        self.label_senha = Label(self.frame1, text='Senha:')
        self.label_senha.place(relx=0.1, rely=0.37)
        self.senha = Entry(self.frame1, show='*')
        self.senha.place(relx=0.1, rely=0.43, relwidth=0.8)

        def verificar_login():
            usuario_digitado = self.user.get()
            senha_digitada = self.senha.get()

            # Verificação do usuario e senha digitada
            resultado = True if usuario_digitado == 'ADMIN' and senha_digitada == 'admin123' else False
            print(resultado)
            self.mostra_dashboard() if resultado else messagebox.showerror('Erro de Login',
                                                                           'Usuário ou senha digitados não conferem!')

        # Botão de Login
        self.botao_login = Button(self.frame1, text='Login', font=('sans', 10, 'bold'), bd=2, background='#C5D4EB',
                                  command=verificar_login)
        self.botao_login.place(relx=0.33, rely=0.65, relwidth=0.3)

    def mostra_dashboard(self):
        [widget.destroy() for widget in self.janela.winfo_children()]
        self.configura_menu()
        self.janela.geometry('800x500')
        self.janela.minsize(width=800, height=500)
        self.janela.maxsize(width=1024, height=768)
        # Criação dos Frames da tela Dashboard
        self.frame2 = Frame(self.janela, bd=6, highlightthickness=2, highlightcolor='#6C85BD')
        self.frame2.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.12)
        self.frame3 = Frame(self.janela, bd=6, highlightthickness=2, highlightcolor='#6C85BD')
        self.frame3.place(relx=0.05, rely=0.23, relwidth=0.9, relheight=0.75)
        # Criação dos botões de gestão
        self.botao_veiculos = Button(self.frame2, text='Gerir Veículos', font=('sans', 10, 'bold'), bd=2, background='#C5D4EB', command=self.gerir_veiculos)
        self.botao_veiculos.place(relx=0.15, rely=0.15, relwidth=0.3)
        self.botao_usuarios = Button(self.frame2, text='Gerir Usuários', font=('sans', 10, 'bold'), bd=2, background='#C5D4EB', command=self.gerir_usuarios)
        self.botao_usuarios.place(relx=0.55, rely=0.15, relwidth=0.3)
        # Criação do Dashboard
        self.titulo_dashboard = Label(self.frame3, text='Dashboard', font=('verdana', 16))
        self.titulo_dashboard.place(relx=0.05, rely=0.05)

        # Indicador Próximo Veículo Manutenção
        def verifica_proxima_manut():
            self.conecta_bd()
            self.cursor.execute(""" SELECT id, nome, quilometragem, manutencao FROM veiculos """)
            self.veiculos_para_manut = self.cursor.fetchall()
            # variaveis iniciais para calculo
            veiculo_mais_proximo = None
            menor_diferenca_manut = float('inf')
            for veiculo in self.veiculos_para_manut:
                id, nome, quilometragem, manutencao = veiculo
                diferenca_manut = manutencao - quilometragem

                if diferenca_manut < menor_diferenca_manut:
                    menor_diferenca_manut = diferenca_manut
                    veiculo_mais_proximo = (id, nome)

            # Posicionamento do Label no Frame3 do Dashboard
            self.canva_label = Canvas(self.frame3, bd=2, bg='#DFE9F5', highlightbackground='#6C85BD', highlightthickness=3)
            self.canva_label.place(relx=0.10, rely=0.17, relwidth=0.39, relheight=0.17)
            self.label_proxima_manutencao = Label(self.frame3, text='Próximo Veículo a entrar em manutenção', background='#DFE9F5')
            self.label_proxima_manutencao.place(relx=0.13, rely=0.2)

            if veiculo_mais_proximo:
                id_proxima_manut, nome_proxima_manut = veiculo_mais_proximo
                self.label_proxima_manutencao.config(
                    text=f"Próximo Veículo a entrar em manutenção:\nID: {id_proxima_manut}, Nome: {nome_proxima_manut}")
            else:
                self.label_proxima_manutencao.config(text='Não há veículos para manutenção iminente')

            self.conn.close()
        verifica_proxima_manut()

        # Indicador Próximo Veículo Licenciamento
        def verifica_proximo_licenciamento():
            self.conecta_bd()
            self.cursor.execute(""" SELECT id, nome, licenciamento FROM veiculos """)
            self.veiculos_para_licenciar = self.cursor.fetchall()
            # variaveis iniciais para calculo
            veiculo_mais_proximo_licenc = None
            licenciamento_veiculo = "2050-01-01"

            for veiculo in self.veiculos_para_licenciar:
                id, nome, licenciamento = veiculo

                if licenciamento < licenciamento_veiculo:
                    licenciamento_veiculo = licenciamento
                    veiculo_mais_proximo_licenc = (id, nome, licenciamento)

            # Posicionamento do Label no Frame3 do Dashboard
            self.canva_label = Canvas(self.frame3, bd=2, bg='#DFE9F5', highlightbackground='#6C85BD',
                                      highlightthickness=3)
            self.canva_label.place(relx=0.50, rely=0.17, relwidth=0.39, relheight=0.17)
            self.label_proximo_licenciamento = Label(self.frame3, text='Próximo Veículo a ser licenciado:', background='#DFE9F5')
            self.label_proximo_licenciamento.place(relx=0.53, rely=0.2)

            if veiculo_mais_proximo_licenc:
                id_proximo_licenciamento, nome_proximo_licenciamento, licenciamento = veiculo_mais_proximo_licenc
                self.label_proximo_licenciamento.config(
                    text=f"Próximo Veículo a ser licenciado:\nID: {id_proximo_licenciamento}, Nome: {nome_proximo_licenciamento}, em: {licenciamento}")
            else:
                self.label_proximo_licenciamento.config(text='Não há veículos a serem licenciados')

            self.conn.close()
        verifica_proximo_licenciamento()

        def verifica_disponibilidade_veic():
            self.conecta_bd()
            # Labels por categoria
            self.canva_label = Canvas(self.frame3, bd=2, bg='#DFE9F5', highlightbackground='#6C85BD',
                                      highlightthickness=3)
            self.canva_label.place(relx=0.04, rely=0.47, relwidth=0.9, relheight=0.37)
            label_economico = Label(self.frame3, text='Veículos "Econômico" disponíveis:', background='#DFE9F5')
            label_economico.place(relx=0.07, rely=0.5)
            label_silver = Label(self.frame3, text='Veículos "SILVER" disponíveis:', background='#DFE9F5')
            label_silver.place(relx=0.38, rely=0.5)
            label_gold = Label(self.frame3, text='Veículos "GOLD" disponíveis:', background='#DFE9F5')
            label_gold.place(relx=0.68, rely=0.5)
            # Busca pelos veiculos disponiveis
            self.cursor.execute(""" SELECT id, nome, categoria FROM veiculos WHERE disponibilidade = 'sim' """)
            veiculos_disponiveis = self.cursor.fetchall()

            for veiculo in veiculos_disponiveis:
                id, nome, categoria = veiculo
                if categoria == 'Economico':
                    label_economico.config(text=label_economico.cget("text") + f"\n{nome}")
                elif categoria == 'SILVER':
                    label_silver.config(text=label_silver.cget("text") + f"\n{nome}")
                elif categoria == 'GOLD':
                    label_gold.config(text=label_gold.cget("text") + f"\n{nome}")

            self.conn.close()
        verifica_disponibilidade_veic()

    def gerir_usuarios(self):
        # Configuração da Janela
        [widget.destroy() for widget in self.janela.winfo_children()]
        self.janela.title('Gestão Avançada de Usuários - Luxury Wheels')
        self.janela.geometry('800x500')
        self.janela.minsize(width=800, height=500)
        self.janela.maxsize(width=1024, height=768)
        self.frame4 = Frame(self.janela)
        self.frame4.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.35)
        self.frame5 = Frame(self.janela)
        self.frame5.place(relx=0.05, rely=0.40, relwidth=0.9, relheight=0.55)
        # Botões do Frame 4
        self.canva_label = Canvas(self.frame4, bd=2, bg='#DFE9F5', highlightbackground='#6C85BD',
                                  highlightthickness=3)
        self.canva_label.place(relx=0.04, rely=0.02, relwidth=0.45, relheight=0.21)
        # Botão de limpar campos
        self.botao_limpar_campo = Button(self.frame4, text='Limpar Campos', command=self.limpa_formulario)
        self.botao_limpar_campo.place(relx=0.71, rely=0.05)
        # Botão para apagar usuario
        self.botao_del_user = Button(self.frame4, text='Apagar Usuário', command=self.deleta_cliente)
        self.botao_del_user.place(relx=0.05, rely=0.05, relwidth=0.13)
        # Botão para editar usuario
        self.botao_edit_user = Button(self.frame4, text='Editar Usuário', command=self.altera_cliente)
        self.botao_edit_user.place(relx=0.20, rely=0.05, relwidth=0.13)
        # Botão para buscar usuário
        self.botao_buscar = Button(self.frame4, text='Buscar Usuário', command=self.busca_cliente)
        self.botao_buscar.place(relx=0.35, rely=0.05, relwidth=0.13)
        # Botão para voltar à janela anterior (Dashboard)
        self.botao_voltar = Button(self.frame4, text='Voltar', command=self.mostra_dashboard)
        self.botao_voltar.place(relx=0.86, rely=0.05)
        # Labels e Entrys dos Dados dos Usuários no Frame 4
        # Label e Entry Código
        self.label_codigo = Label(self.frame4, text='Código:')
        self.label_codigo.place(relx=0.05, rely=0.25)
        self.codigo_entry = Entry(self.frame4)
        self.codigo_entry.place(relx=0.05, rely=0.35, relwidth=0.1)
        # Label e Entry Nome
        self.label_nome = Label(self.frame4, text='Nome:')
        self.label_nome.place(relx=0.20, rely=0.25)
        self.nome_entry = Entry(self.frame4)
        self.nome_entry.place(relx=0.20, rely=0.35, relwidth=0.72)
        # Label e Entry Username
        self.label_username = Label(self.frame4, text='Username:')
        self.label_username.place(relx=0.05, rely=0.50)
        self.username_entry = Entry(self.frame4)
        self.username_entry.place(relx=0.05, rely=0.60, relwidth=0.2)
        # Label e Entry email
        self.label_email = Label(self.frame4, text='Email:')
        self.label_email.place(relx=0.30, rely=0.50)
        self.email_entry = Entry(self.frame4)
        self.email_entry.place(relx=0.30, rely=0.60, relwidth=0.62)
        # Label e Entry categoria
        self.label_categoria = Label(self.frame4, text='Categoria:')
        self.label_categoria.place(relx=0.05, rely=0.75)
        self.categoria_entry = Entry(self.frame4)
        self.categoria_entry.place(relx=0.05, rely=0.85, relwidth=0.4)
        # Criação da Lista de Usuários - Treeview do Banco de Dados
        self.lista_clientes = Treeview(self.frame5, height=3, column=('col1', 'col2', 'col3', 'col4', 'col5'))
        # Headings das colunas
        self.lista_clientes.heading("#0", text='')
        self.lista_clientes.heading("#1", text='Código')
        self.lista_clientes.heading("#2", text='Nome')
        self.lista_clientes.heading("#3", text='Username')
        self.lista_clientes.heading("#4", text='Email')
        self.lista_clientes.heading("#5", text='Categoria')
        # Tamanho das colunas
        self.lista_clientes.column("#0", width=1)
        self.lista_clientes.column("#1", width=30)
        self.lista_clientes.column("#2", width=170)
        self.lista_clientes.column("#3", width=70)
        self.lista_clientes.column("#4", width=150)
        self.lista_clientes.column("#5", width=100)
        # Localização da lista
        self.lista_clientes.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        # Criação da Scrool Bar
        self.scrool_lista = Scrollbar(self.frame5, orient='vertical')
        self.lista_clientes.configure(yscrollcommand=self.scrool_lista.set)
        self.scrool_lista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        # Mostra a lista de clientes do Banco de Dados - Função da classe Funcs()
        self.mostra_clientes_bd()
        # Ativa função duplo clique para selecionar usuarios da lista
        self.lista_clientes.bind("<Double-1>", self.OnDoubleClick)
        # Menu suspenso para exportar a lista de Usuarios em XLS
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu2 = Menu(menubar)

        def exportar_lista_usuarios():
            self.conecta_bd()
            query = "SELECT * FROM users"
            data = pd.read_sql_query(query, self.conn)
            self.conn.close()
            lista_usuarios_xls = pd.DataFrame(data)
            lista_usuarios_xls.to_excel("lista_usuarios.xlsx", index=False)
            messagebox.showinfo('Atenção!', 'Arquivo exportado com sucesso em sua pasta raiz do App')

        menubar.add_cascade(label="Exportar", menu=filemenu2)
        filemenu2.add_command(label="Formato Excel", command=exportar_lista_usuarios)

    def gerir_veiculos(self):
        # Configuração da Janela
        [widget.destroy() for widget in self.janela.winfo_children()]
        self.janela.title('Gestão Avançada de Veículos - Luxury Wheels')
        self.janela.geometry('1600x900')
        self.janela.minsize(width=1600, height=900)
        self.janela.maxsize(width=1920, height=1080)
        self.frame6 = Frame(self.janela)
        self.frame6.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.30)
        self.frame7 = Frame(self.janela)
        self.frame7.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.65)
        # Botões do Frame 6
        self.canva_label = Canvas(self.frame6, bd=2, bg='#DFE9F5', highlightbackground='#6C85BD',
                                  highlightthickness=3)
        self.canva_label.place(relx=0.043, rely=0.02, relwidth=0.473, relheight=0.163)
        # Botão de limpar campos
        self.botao_limpar_campo_veiculo = Button(self.frame6, text='Limpar Campos', command=self.limpa_formulario_veiculos)
        self.botao_limpar_campo_veiculo.place(relx=0.78, rely=0.05)
        # Botão para incluir veiculo
        self.botao_incluir_veiculo = Button(self.frame6, text='Incluir Veículo', command=self.inclui_veiculo)
        self.botao_incluir_veiculo.place(relx=0.05, rely=0.05, relwidth=0.10)
        # Botão para apagar veiculo
        self.botao_del_veiculo = Button(self.frame6, text='Apagar Veículo', command=self.deleta_veiculo)
        self.botao_del_veiculo.place(relx=0.17, rely=0.05, relwidth=0.10)
        # Botão para editar veículo
        self.botao_edit_veiculo = Button(self.frame6, text='Editar Veículo', command=self.altera_veiculo)
        self.botao_edit_veiculo.place(relx=0.29, rely=0.05, relwidth=0.10)
        # Botão para buscar veiculo
        self.botao_buscar_veiculo = Button(self.frame6, text='Buscar Veículo', command=self.busca_veiculo)
        self.botao_buscar_veiculo.place(relx=0.41, rely=0.05, relwidth=0.10)
        # Botão para voltar à janela anterior (Dashboard)
        self.botao_voltar = Button(self.frame6, text='Voltar', command=self.mostra_dashboard)
        self.botao_voltar.place(relx=0.86, rely=0.05)
        # Labels e Entrys dos Dados dos Veiculos no Frame 6
        # Label e Entry Código
        self.label_id_veiculo = Label(self.frame6, text='Código:')
        self.label_id_veiculo.place(relx=0.05, rely=0.25)
        self.id_veiculo_entry = Entry(self.frame6)
        self.id_veiculo_entry.place(relx=0.05, rely=0.33, relwidth=0.05)
        # Label e Entry Nome
        self.label_nome_veiculo = Label(self.frame6, text='Nome:')
        self.label_nome_veiculo.place(relx=0.13, rely=0.25)
        self.nome_veiculo_entry = Entry(self.frame6)
        self.nome_veiculo_entry.place(relx=0.13, rely=0.33, relwidth=0.50)
        # Label e Entry Categoria
        self.label_cat_veiculo = Label(self.frame6, text='Categoria:')
        self.label_cat_veiculo.place(relx=0.66, rely=0.25)
        self.cat_veiculo_entry = Entry(self.frame6)
        self.cat_veiculo_entry.place(relx=0.66, rely=0.33, relwidth=0.15)
        # Label e Entry Preço
        self.label_diaria_aluguer = Label(self.frame6, text='Diária Aluguer:')
        self.label_diaria_aluguer.place(relx=0.84, rely=0.25)
        self.diaria_aluguer_entry = Entry(self.frame6)
        self.diaria_aluguer_entry.place(relx=0.84, rely=0.33, relwidth=0.07)
        # Label e Entry para Caminho da Imagem do veiculo
        self.label_imagem_veiculo = Label(self.frame6, text='Caminho Imagem:')
        self.label_imagem_veiculo.place(relx=0.05, rely=0.45)
        self.imagem_veiculo_entry = Entry(self.frame6)
        self.imagem_veiculo_entry.place(relx=0.05, rely=0.53, relwidth=0.4)
        # Label e Entry para quilometragem do veiculo
        self.label_km_veiculo = Label(self.frame6, text='Quilometragem atual:')
        self.label_km_veiculo.place(relx=0.48, rely=0.45)
        self.km_veiculo_entry = Entry(self.frame6)
        self.km_veiculo_entry.place(relx=0.48, rely=0.53, relwidth=0.1)
        # Label e Entry para quilometragem para manutenção do veiculo
        self.label_km_manut_veiculo = Label(self.frame6, text='Quilometragem para Manutenção:')
        self.label_km_manut_veiculo.place(relx=0.61, rely=0.45)
        self.km_manut_veiculo_entry = Entry(self.frame6)
        self.km_manut_veiculo_entry.place(relx=0.61, rely=0.53, relwidth=0.1)
        # Label e Entry para Data de inicio Manutenção
        self.label_data_inicio_manut = Label(self.frame6, text='Data Inicio da Manutenção:')
        self.label_data_inicio_manut.place(relx=0.74, rely=0.45)
        self.data_inicio_manut_entry = Entry(self.frame6)
        self.data_inicio_manut_entry.place(relx=0.74, rely=0.53, relwidth=0.07)
        # Label e Entry para Data de Final Manutenção
        self.label_data_final_manut = Label(self.frame6, text='Data Final da Manutenção:')
        self.label_data_final_manut.place(relx=0.84, rely=0.45)
        self.data_final_manut_entry = Entry(self.frame6)
        self.data_final_manut_entry.place(relx=0.84, rely=0.53, relwidth=0.07)
        # Label e Entry para Data de Licenciamento
        self.label_data_licenciamento = Label(self.frame6, text='Data para Licenciamento:')
        self.label_data_licenciamento.place(relx=0.05, rely=0.65)
        self.data_licenciamento_entry = Entry(self.frame6)
        self.data_licenciamento_entry.place(relx=0.05, rely=0.73, relwidth=0.1)
        # Label e Entry para Disponibilidade
        self.label_disponibilidade_veic = Label(self.frame6, text='Disponibilidade:')
        self.label_disponibilidade_veic.place(relx=0.18, rely=0.65)
        self.disponibilidade_veic_entry = Entry(self.frame6)
        self.disponibilidade_veic_entry.place(relx=0.18, rely=0.73, relwidth=0.07)
        # Criação da Lista de Veiculos - Treeview do Banco de Dados
        self.lista_veiculos = Treeview(self.frame7, height=3, column=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 'col11'))
        # Headings das colunas
        self.lista_veiculos.heading("#0", text='')
        self.lista_veiculos.heading("#1", text='Código')
        self.lista_veiculos.heading("#2", text='Nome')
        self.lista_veiculos.heading("#3", text='Categoria')
        self.lista_veiculos.heading("#4", text='Preço Diária')
        self.lista_veiculos.heading("#5", text='Imagem Veículo')
        self.lista_veiculos.heading("#6", text='Quilometragem Atual')
        self.lista_veiculos.heading("#7", text='Quilometragem Manutenção')
        self.lista_veiculos.heading("#8", text='Data Inicio Manutenção')
        self.lista_veiculos.heading("#9", text='Data Final Manutenção')
        self.lista_veiculos.heading("#10", text='Data Licenciamento')
        self.lista_veiculos.heading("#11", text='Disponibilidade')
        # Tamanho das colunas
        self.lista_veiculos.column("#0", width=1)
        self.lista_veiculos.column("#1", width=20)
        self.lista_veiculos.column("#2", width=100)
        self.lista_veiculos.column("#3", width=30)
        self.lista_veiculos.column("#4", width=30)
        self.lista_veiculos.column("#5", width=100)
        self.lista_veiculos.column("#6", width=40)
        self.lista_veiculos.column("#7", width=40)
        self.lista_veiculos.column("#8", width=10)
        self.lista_veiculos.column("#9", width=10)
        self.lista_veiculos.column("#10", width=10)
        self.lista_veiculos.column("#11", width=5)
        # Localização da lista
        self.lista_veiculos.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        # Criação da Scrool Bar
        self.scrool_lista_veiculos = Scrollbar(self.frame7, orient='vertical')
        self.lista_veiculos.configure(yscrollcommand=self.scrool_lista_veiculos.set)
        self.scrool_lista_veiculos.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        # Mostra a lista de veiculos do Banco de Dados - Função da classe Funcs()
        self.mostra_veiculos_bd()
        # Ativa função duplo clique para selecionar usuarios da lista
        self.lista_veiculos.bind("<Double-1>", self.OnDoubleClickVeiculo)
        # Menu suspenso para exportar a lista de veiculos em XLS
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu2 = Menu(menubar)

        def exportar_lista_veiculos():
            self.conecta_bd()
            query = "SELECT * FROM veiculos"
            data = pd.read_sql_query(query, self.conn)
            self.conn.close()
            lista_veic_xls = pd.DataFrame(data)
            lista_veic_xls.to_excel("lista_veiculos.xlsx", index=False)
            messagebox.showinfo('Atenção!','Arquivo exportado com sucesso em sua pasta raiz do App')

        menubar.add_cascade(label="Exportar", menu=filemenu2)
        filemenu2.add_command(label="Formato Excel", command=exportar_lista_veiculos)

if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()


"""

financeiro
valor final aluguel, apos confirmação, armazenado em bd, com data
grafico de acompanhamento diario de transações

"""
