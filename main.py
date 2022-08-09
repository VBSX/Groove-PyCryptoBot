import webbrowser
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import sqlite3
from bot import Binance_bot
import os
import cryptocode
import pandas as pd

class Interface:
    def __init__(self, primeira_tela, segunda_tela, tela_cadastro, tela_admin, tela_erro, tela_key, tela_saldo):
        
        self.primeira_tela= uic.loadUi(primeira_tela)
        self.primeira_tela.pushButton.clicked.connect(self.logar)
        self.primeira_tela.label_3.setText("")
        self.primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.primeira_tela.pushButton_2.clicked.connect(self.abrir_git)
        

        self.segunda_tela = uic.loadUi(segunda_tela)
        self.segunda_tela.pushButton.clicked.connect(self.logout)
        self.segunda_tela.botao_ver_saldo.clicked.connect(self.ver_saldo)
        self.segunda_tela.botao_api.clicked.connect(self.adicionar_api_key)
        

        self.tela_cadastro = uic.loadUi(tela_cadastro)
        self.tela_cadastro.erro.setText("")
        self.tela_cadastro.cadastrado.setText("")
        self.tela_cadastro.botao_cadastro.clicked.connect(self.cadastrar)

        self.tela_admin = uic.loadUi(tela_admin)
        self.tela_admin.botao_deslogar.clicked.connect(self.logout)
        self.tela_admin.botao_cadastrar.clicked.connect(self.cadastro_tela)

        self.tela_erro = uic.loadUi(tela_erro)
        self.tela_erro.label.setText("")
        self.bot = Binance_bot()

        self.tela_key = uic.loadUi(tela_key)
        self.tela_key.botao_config.clicked.connect(self.criar_env)

        
        self.tela_saldo = uic.loadUi(tela_saldo)
        self.lista_janelas = [self.segunda_tela, self.tela_cadastro, self.tela_admin, self.tela_erro, self.tela_key, self.tela_saldo]
    
    def iniciar_tela_saldo(self):
        self.tela_saldo.show()    
    def iniciar_tela_key(self):
        self.tela_key.show()

    def iniciar_tela_admin(self):
        self.tela_admin.show()

    def iniciar_tela_erro(self):
        self.tela_erro.show()

    def fechar_tela_admin(self):
        self.tela_admin.close()

    def iniciar_primeira_tela(self):
        self.primeira_tela.show()
    
    def iniciar_segunda_tela(self):
        self.segunda_tela.show()

    def fechar_janela_erro(self):
        self.primeira_tela.close()

    def fechar_primeria_tela(self):
        self.primeira_tela.close()

    def fechar_segunda_tela(self):
        self.segunda_tela.close()
    
    def iniciar_tela_cadastro(self):
        self.tela_cadastro.show()

    def fechar_tela_cadastro(self):
        self.tela_cadastro.close()

    def fechar_tela_key(self):
        self.tela_key.close()
    def fecha_primeira_tela_abre_segunda_tela(self):
        self.fechar_primeria_tela()
        self.iniciar_segunda_tela()

    def abrir_git(self):
        webbrowser.open_new_tab('https://github.com/vbsx')
    
    def mostrar_erro_janela_pop_up(self, erro):
        self.tela_erro.label.setText(f"{erro}")

    def mostrar_erro_banco_primeira_tela(self):
        self.primeira_tela.label_3.setText("Exeção banco de dados")

    def erro_usuario_senha(self):
        self.primeira_tela.label_3.setText("Usuário ou senha inválidos!")

    def excluir_env(self):
        if self.bot.verificar_existencia_env() == True:
            os.remove(".env")

    def criar_env(self):
        self.api = self.tela_key.apy_key.text()
        self.secret = self.tela_key.secret_key.text()
        texto_api = (f'API_KEY = "{self.api}"\n')
        texto_secret = (f'SECRET_KEY = "{self.secret}"')
        texto_final = (texto_api+texto_secret)
        env = '.env'
        with open(env, 'w+') as writer:
            self.escritor = writer.writelines(texto_final)
        self.fechar_tela_key()
        self.iniciar_tela_erro()
        self.mostrar_erro_janela_pop_up("Api e secret key configurados com sucesso!")

    def coleta_banco(self):
        self.nome_usuario = self.primeira_tela.lineEdit.text()
        self.banco = sqlite3.connect('banco_cadastro.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute("SELECT senha FROM cadastro WHERE login ='{}'".format(self.nome_usuario))
        self.senha_db = self.cursor.fetchall()
        self.banco.close()
    
    def erro_usuario_incorreto(self):
        self.primeira_tela.label_3.setText("Dados de login incorretos!")

    def verificar_admin(self):
        if self.nome_usuario == "admin":
            return True
        else:
            return False

    def verificar_senha(self):
        self.senha = self.primeira_tela.lineEdit_2.text()
        self.senha_db_decriptada = cryptocode.decrypt(f'{self.senha_db[0][0]}','senha@123')
        try:
            if self.senha == self.senha_db_decriptada:
                return True
        except:
            return self.erro_usuario_incorreto()
    
    def validar_usuario(self):
        if self.verificar_senha() == True:
            self.fecha_primeira_tela_abre_segunda_tela()
            self.nome_na_tela_user()
        else:
            return self.erro_usuario_incorreto()

    def logar(self):
        try:
            self.coleta_banco()
        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)

        if self.verificar_admin() == True and self.verificar_senha() == True:
            self.iniciar_tela_admin()
            self.nome_na_tela_admin()
            self.fechar_primeria_tela()

        else:        
            self.validar_usuario()
            
    def cadastrar_user_banco(self):
        self.nome_cadastro = self.tela_cadastro.nome.text()
        self.login_cadastro = self.tela_cadastro.login.text()
        self.senha_criptografada_do_cadastro = cryptocode.encrypt(f'{self.senha_cadastro}', 'senha@123')
        self.senha_criptograda_confimacao_do_cadastro = cryptocode.encrypt(f'{self.confimacao_senha_cadastro}', 'senha@123')
        try:
            
            self.banco = sqlite3.connect('banco_cadastro.db') 
            self.cursor = self.banco.cursor()
            self.cursor.execute("INSERT INTO cadastro VALUES ('"+self.nome_cadastro+"','"+self.login_cadastro+"','"+self.senha_criptografada_do_cadastro+"')")
            self.banco.commit() 
            self.banco.close()
            self.tela_cadastro.cadastrado.setText("Usuario cadastrado com sucesso")
        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
            return erro

    def verificar_senha_cadastro(self):
        self.senha_cadastro = self.tela_cadastro.senha.text()
        self.confimacao_senha_cadastro = self.tela_cadastro.confirmar_senha.text()

        
        if self.senha_cadastro == self.confimacao_senha_cadastro:
            return True
        else:
            self.tela_cadastro.erro.setText("As senhas não conferem!")

    def cadastrar(self):
        self.verificar_senha_cadastro()

        if self.verificar_senha_cadastro() == True:
            self.cadastrar_user_banco()
    
    def cadastro_tela(self):
        self.iniciar_tela_cadastro()
    
    def coletar_excel(self):
        self.bot.moedas_com_saldo()
        
    def ler_excel(self):
        self.coletar_excel()
        leitor = pd.read_excel('saldo.xlsx', index_col=0)
        return leitor
    def get_number_of_lines_df(self, df):
        
        linhas = df.shape[0]
        return linhas
        
    def gerar_info_saldo(self):
        
        self.ler_excel()
        df = self.ler_excel()
        numero_linhas_df = self.get_number_of_lines_df(df)
        self.tela_saldo.tableWidget.setRowCount(numero_linhas_df)
        self.tela_saldo.tableWidget.setColumnCount(df.shape[1])
        self.tela_saldo.tableWidget.setHorizontalHeaderLabels(df.columns)

        for row in df.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.9f}'.format(value)
                table_item = QTableWidgetItem(str(value))
                self.tela_saldo.tableWidget.setItem(row[0], col_index, table_item)
                    
    def ver_saldo(self):
        if  self.bot.verificar_existencia_env() == True:
            self.iniciar_tela_saldo()
            self.coletar_excel()
            self.segunda_tela.label_resultado.setText("")
            self.gerar_info_saldo()
        else:
            self.iniciar_tela_erro()
            self.mostrar_erro_janela_pop_up("Favor configure seu o seu APY_KEY e SECRET_KEY na tela inicial antes de prosseguir!")

    def adicionar_api_key(self):
        if self.bot.verificar_existencia_env() == True:
            self.iniciar_tela_erro()
            self.mostrar_erro_janela_pop_up("APY_KEY Já configurado, deslogue e logue novamente para adicionar um novo APY_KEY")
        else:
            self.iniciar_tela_key()
        
    def limpar_user_senha(self):
        self.primeira_tela.lineEdit.setText("")
        self.primeira_tela.lineEdit_2.setText("")
            
    def nome_na_tela_admin(self):
        self.tela_admin.nome_user.setText(f"{self.nome_usuario}")
        
    def nome_na_tela_user(self):
        self.segunda_tela.nome_user.setText(f"{self.nome_usuario}")
    def fechar_todas_as_janelas(self):
        for janela in self.lista_janelas:
            janela.close()

    def logout(self):
        self.fechar_todas_as_janelas()
        self.iniciar_primeira_tela()
        self.limpar_user_senha()
        self.excluir_env()
        
app=QtWidgets.QApplication([])
iniciar_interface = Interface(f"Interfaces/Tela_Inicial.ui", "Interfaces/segunda_tela.ui", "Interfaces/tela_cadastro.ui",
  "Interfaces/tela_admin.ui", "Interfaces/tela_erro.ui", "Interfaces/tela_key.ui", "Interfaces/tela_saldo.ui")
iniciar_interface.iniciar_primeira_tela()
app.exec()
# iniciar_interface.gerar_info_saldo()