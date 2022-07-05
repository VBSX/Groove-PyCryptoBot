import webbrowser
from PyQt5 import uic, QtWidgets
import sqlite3

class Interface:
    def __init__(self, primeira_tela, segunda_tela, tela_cadastro, tela_admin):
        self.primeira_tela= uic.loadUi(primeira_tela)
        self.primeira_tela.pushButton.clicked.connect(self.logar)
        self.primeira_tela.label_3.setText("")
        self.primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.primeira_tela.pushButton_2.clicked.connect(self.abrir_git)

        self.segunda_tela = uic.loadUi(segunda_tela)
        self.segunda_tela.pushButton.clicked.connect(self.logout)
        
        self.tela_cadastro = uic.loadUi(tela_cadastro)
        self.tela_cadastro.erro.setText("")
        self.tela_cadastro.cadastrado.setText("")
        self.tela_cadastro.botao_cadastro.clicked.connect(self.cadastrar)

        self.tela_admin = uic.loadUi(tela_admin)
        self.tela_admin.botao_deslogar.clicked.connect(self.logout)
        self.tela_admin.botao_cadastrar.clicked.connect(self.cadastro_tela)
        
    def iniciar_tela_admin(self):
        self.tela_admin.show()
    
    def fechar_tela_admin(self):
        self.tela_admin.close()

    def iniciar_primeira_tela(self):
        self.primeira_tela.show()
    
    def iniciar_segunda_tela(self):
        self.segunda_tela.show()

    def fechar_primeria_tela(self):
        self.primeira_tela.close()

    def fechar_segunda_tela(self):
        self.segunda_tela.close()
    
    def iniciar_tela_cadastro(self):
        self.tela_cadastro.show()

    def fechar_tela_cadastro(self):
        self.tela_cadastro.close()

    def fecha_primeira_tela_abre_segunda_tela(self):
        self.fechar_primeria_tela()
        self.iniciar_segunda_tela()

    def abrir_git(self):
        webbrowser.open_new_tab('https://github.com/vbsx')
    
    def mostrar_erro_banco_primeira_tela(self):
        self.primeira_tela.label_3.setText("Exeção banco de dados")

    def erro_usuario_senha(self):
        self.primeira_tela.label_3.setText("Usuário ou senha inválidos!")

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
        try:
            if self.senha == self.senha_db[0][0]:
                #self.fecha_primeira_tela_abre_segunda_tela()
                return True
        except:
            return self.erro_usuario_incorreto()
    
    def validar_usuario(self):
        if self.verificar_senha() == True:
            self.fecha_primeira_tela_abre_segunda_tela()
            
        else:
            return self.erro_usuario_incorreto()

    def logar(self):
        
        try:
            self.coleta_banco()
        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)

        if self.verificar_admin() == True and self.verificar_senha() == True:
            self.iniciar_tela_admin()
            self.admin_tela()
            self.fechar_primeria_tela()

        else:        
            self.validar_usuario()
            
    def cadastrar_user_banco(self):
        try:
            self.banco = sqlite3.connect('banco_cadastro.db') 
            self.cursor = self.banco.cursor()
            self.cursor.execute("INSERT INTO cadastro VALUES ('"+self.nome_cadastro+"','"+self.login_cadastro+"','"+self.senha_cadastro+"')")
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
        print('ja verificou a senha')

        if self.verificar_senha_cadastro() == True:
            print('abrindo o cadastro')
            self.cadastrar_user_banco()
        
    def cadastro_tela(self):
        self.iniciar_tela_cadastro()
        # self.tela_cadastro.senha.setEchoMode(QtWidgets.QLineEdit.Password)
        # self.tela_cadastro.confirmar_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.nome_cadastro = self.tela_cadastro.nome.text()
        self.login_cadastro = self.tela_cadastro.login.text()
        
    def limpar_user_senha(self):
        self.primeira_tela.lineEdit.setText("")
        self.primeira_tela.lineEdit_2.setText("")
            
    def admin_tela(self):
        self.tela_admin.label_2.setText(f"{self.nome_usuario}")

    def logout(self):
        self.fechar_segunda_tela()
        self.fechar_tela_admin()
        self.fechar_tela_cadastro()
        self.iniciar_primeira_tela()
        self.limpar_user_senha()

app=QtWidgets.QApplication([])
iniciar_interface = Interface(f"Tela_Inicial.ui", "segunda_tela.ui", "tela_cadastro.ui", "tela_admin.ui")
iniciar_interface.iniciar_primeira_tela()

app.exec()
