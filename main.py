import webbrowser
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import sqlite3
from bot import Binance_bot
import os
import cryptocode
import pandas as pd


class Interface:
    def __init__(
        self, first_window, second_window,
        register_window, admin_window, error_window,
        window_key, window_balance
        ):
        
        
        self.primeira_tela= uic.loadUi(first_window)
        self.primeira_tela.pushButton.clicked.connect(self.login)
        self.primeira_tela.label_3.setText("")
        self.primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.primeira_tela.pushButton_2.clicked.connect(self.open_git_on_web)
        
        
        self.segunda_tela = uic.loadUi(second_window)
        self.segunda_tela.pushButton.clicked.connect(self.logout)
        self.segunda_tela.botao_ver_saldo.clicked.connect(self.get_ballance_from_binance)
        self.segunda_tela.botao_api.clicked.connect(self.add_api_key)
        

        self.tela_cadastro = uic.loadUi(register_window)
        self.tela_cadastro.erro.setText("")
        self.tela_cadastro.cadastrado.setText("")
        self.tela_cadastro.botao_cadastro.clicked.connect(self.register_new_user)


        self.tela_admin = uic.loadUi(admin_window)
        self.tela_admin.botao_deslogar.clicked.connect(self.logout)
        self.tela_admin.botao_cadastrar.clicked.connect(self.cadastro_tela)


        self.tela_erro = uic.loadUi(error_window)
        self.tela_erro.label.setText("")
        self.bot = Binance_bot()


        self.tela_key = uic.loadUi(window_key)
        self.tela_key.botao_config.clicked.connect(self.criar_env)

        
        self.tela_saldo = uic.loadUi(window_balance)
        self.lista_janelas = [
            self.segunda_tela, self.tela_cadastro,
            self.tela_admin, self.tela_erro, self.tela_key, self.tela_saldo
            ]
    
    
    def start_window(self, window):
        window.show()
    
    
    def close_window(self, window):
        window.close()
      
        
    def start_first_window(self):
        self.primeira_tela.show()
   
   
    def open_git_on_web(self):
        webbrowser.open_new_tab(
            'https://github.com/vbsx'
            )
    
    
    def show_error_pop_up_window(self, erro):
        self.start_window(self.tela_erro)
        self.tela_erro.label.setText(f"{erro}")


    def show_database_error_on_first_screen(self):
        self.primeira_tela.label_3.setText(
            "Database ecxeption"
            )


    def erro_usuario_senha(self):
        self.primeira_tela.label_3.setText(
            "username or password is invalid!"
            )


    def delete_env(self):
        if self.bot.verify_existence_of_env() == True:
            os.remove(".env")
    
    
    def criar_env(self):
        self.api = self.tela_key.apy_key.text()
        self.secret = self.tela_key.secret_key.text()
        api_text = (f'API_KEY = "{self.api}"\n')
        secret_text = (f'SECRET_KEY = "{self.secret}"')
        final_text = (api_text+secret_text)
        env = '.env'
        
        with open(env, 'w+') as writer:
            self.escritor = writer.writelines(final_text)
        
        self.close_window(self.tela_key)
        self.start_window(self.tela_erro)
        self.show_error_pop_up_window(
            "Api e secret key set with sucess!"
            )


    def colect_data_on_database(self):
        self.username = self.primeira_tela.lineEdit.text()
        self.banco = sqlite3.connect('banco_cadastro.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute(
            "SELECT senha FROM cadastro WHERE login ='{}'".format(self.username)
            )
        self.database_password = self.cursor.fetchall()
        self.banco.close()
    
    
    def error_incorrect_user(self):
        self.primeira_tela.label_3.setText(
            "Incorrect login data!"
            )


    def verify_user_admin(self):
        if self.username == "admin":
            
            
            return True
        
        
        else:
            
            
            return False


    def verify_password(self):
        password = self.primeira_tela.lineEdit_2.text()
        decrypted_db_password = cryptocode.decrypt(
            f'{self.database_password[0][0]}','senha@123'
            )
        
        
        try:
            
            
            if password == decrypted_db_password:
                return True
            
            
        except:
            return self.error_incorrect_user()
    
    def validate_user(self):
        if self.verify_password() == True:
            self.close_window(self.primeira_tela)
            self.start_window(self.segunda_tela)
            self.name_of_user_on_screen()
            
            
        else:
            
            
            return self.error_incorrect_user()

    def login(self):
        try:
            self.colect_data_on_database()
            
            
        except sqlite3.Error as erro:
            
            
            return erro

        if self.verify_user_admin() == True and self.verify_password() == True:
            self.start_window(self.tela_admin)
            self.admin_name_on_screen()
            self.close_window(self.primeira_tela)
            
            
        else:        
            self.validate_user()

    def register_new_user(self):
        self.verify_password_of_register()
        if self.verify_password_of_register() == True:
            self.register_the_new_user_on_database()
    
    
    def verify_password_of_register(self):
        self.senha_cadastro = self.tela_cadastro.senha.text()
        self.confimacao_senha_cadastro = self.tela_cadastro.confirmar_senha.text()

        
        if self.senha_cadastro == self.confimacao_senha_cadastro:
            return True
        
        
        else:
            self.tela_cadastro.erro.setText("The passwords are not the same!")
    
                
    def register_the_new_user_on_database(self):
        self.nome_cadastro = self.tela_cadastro.nome.text()
        self.login_cadastro = self.tela_cadastro.login.text()
        self.senha_criptografada_do_cadastro = cryptocode.encrypt(
            f'{self.senha_cadastro}', 'senha@123'
            )
        self.senha_criptograda_confimacao_do_cadastro = cryptocode.encrypt(
            f'{self.confimacao_senha_cadastro}', 'senha@123'
            )
        
        
        try:
            self.banco = sqlite3.connect('banco_cadastro.db') 
            self.cursor = self.banco.cursor()
            self.cursor.execute(
                "INSERT INTO cadastro VALUES ('"+self.nome_cadastro+"',"
                f"'"+self.login_cadastro+"','"+self.senha_criptografada_do_cadastro+"')")
            self.banco.commit() 
            self.banco.close()
            self.tela_cadastro.cadastrado.setText("User registered with sucess!")
            
            
        except sqlite3.Error as erro:
            
            
            return erro


    def cadastro_tela(self):
        self.start_window(self.tela_cadastro)
    
    
    def colect_data_from_excel(self):
        self.bot.coins_with_balance_on_account()
       
        
    def read_excel(self):
        self.colect_data_from_excel()
        reader = pd.read_excel('saldo.xlsx', index_col=0)
        
        
        return reader
    
    
    def get_number_of_lines_df(self, df):
        
        linhas = df.shape[0]
        
        
        return linhas
        
        
    def generate_info_ballance(self):
        
        self.read_excel()
        df = self.read_excel()
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
        
                    
    def get_ballance_from_binance(self):
        if  self.bot.verify_existence_of_env() == True:
            self.start_window(self.tela_saldo)
            
            if self.bot.test_env() == True:
                self.colect_data_from_excel()
                self.segunda_tela.label_resultado.setText("")
                self.generate_info_ballance()
               
                
            else:
                self.show_error_pop_up_window
                (
                    'API or SECRET KEY was not set correctly, please do again the configuration'
                    )
                
                
        else:
            self.start_window(self.tela_erro)
            self.show_error_pop_up_window
            (
                "Please set your API_KEY and SECRET_KEY on the home screen before proceeding!!"
                )


    def add_api_key(self):
        if self.bot.verify_existence_of_env() == True:
            self.start_window(self.tela_erro)
            self.show_error_pop_up_window
            (
                "APY_KEY Already configured, logout and login again to add a new APY_KEY"
                )
            
            
        else:
            self.start_window(self.tela_key)
        
        
    def clean_user_password(self):
        self.primeira_tela.lineEdit.setText("")
        self.primeira_tela.lineEdit_2.setText("")
       
            
    def admin_name_on_screen(self):
        self.tela_admin.nome_user.setText(f"{self.username}")
        
        
    def name_of_user_on_screen(self):
        self.segunda_tela.nome_user.setText(f"{self.username}")
        
        
    def close_all_windows(self):
        for window in self.lista_janelas:
            window.close()


    def logout(self):
        self.close_all_windows()
        self.start_window(self.primeira_tela)
        self.clean_user_password()
        self.delete_env()
        
        
app=QtWidgets.QApplication([])
iniciar_interface = Interface(
    f"Interfaces/Tela_Inicial.ui", "Interfaces/segunda_tela.ui", "Interfaces/tela_cadastro.ui",
  "Interfaces/tela_admin.ui", "Interfaces/tela_erro.ui",
  "Interfaces/tela_key.ui", "Interfaces/tela_saldo.ui"
  )
iniciar_interface.start_first_window()
app.exec()
# iniciar_interface.ver_saldo()

