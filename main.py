import webbrowser
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QTableWidgetItem
import sqlite3
from bot import BinanceApi
import os
import cryptocode
import pandas as pd

class LoginInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginInterface, self).__init__()
        close_signal = pyqtSignal()
        
        self.login_window= uic.loadUi("Interfaces/Tela_Inicial.ui")
        self.clean_user_password()

        self.login_window.pushButton.clicked.connect(self.login)
        self.login_window.label_3.setText("")
        self.login_window.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.login_window.botao_git.clicked.connect(self.open_git_on_web)
        self.database = Database()
        self.verifier = Verifier()
        self.login_window.show()
        
    
    def login(self):
        password = self.login_window.lineEdit_2.text()
        username = self.login_window.lineEdit.text()
        database_password = self.database.colect_password_database(username)


        if self.verifier.verify_user_admin(username) == True and self.verifier.verify_password(password,database_password) == True:
            self.login_window.close()
            AdminInterface()
            
            
        else:
            if self.verifier.verify_password(password,database_password) == True:
                # self.login_window.close()
                HomeInterface(self).name_user_on_screen(username)
                
          
            else:
                self.show_dialog("username or password is invalid!")
                
            

    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)
            

    def open_git_on_web(self):
        webbrowser.open_new_tab(
        'https://github.com/vbsx'
        )

    
    def clean_user_password(self):
        self.login_window.lineEdit.setText("")
        self.login_window.lineEdit_2.setText("")
       

class HomeInterface(QtWidgets.QWidget):
    def __init__(self , *args, **kwargs):
        super(HomeInterface, self).__init__(*args, **kwargs)
        self.home_window = uic.loadUi('Interfaces/segunda_tela.ui')
        # self.home_window.pushButton.clicked.connect(self.logout)
        # self.home_window.botao_ver_saldo.clicked.connect(self.get_ballance_from_binance)
        # self.home_window.botao_api.clicked.connect(self.add_api_key)
        self.home_window.show()

    
    def close_me(self):
        self.home_window.close()


    def name_user_on_screen(self, username):
        self.home_window.nome_user.setText(f"{username}")
        
        
class AdminInterface(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(AdminInterface, self).__init__(*args, **kwargs)

        self.admin_window = uic.loadUi("Interfaces/tela_admin.ui")
        # self.admin_window.botao_deslogar.clicked.connect(self.logout)
        self.admin_window.botao_cadastrar.clicked.connect(RegisterInterface)
        self.admin_window.show()
     

class RegisterInterface(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(RegisterInterface, self).__init__(*args, **kwargs)
        
        self.verifier = Verifier()
        self.database = Database()
        
        self.registration_window = uic.loadUi("Interfaces/tela_cadastro.ui")
        self.registration_window.erro.setText("")
        self.registration_window.cadastrado.setText("")
        self.registration_window.botao_cadastro.clicked.connect(self.register_new_user)
        
        self.password_register = self.registration_window.senha.text()
        self.register_password_confirmation = self.registration_window.confirmar_senha.text()
        self.nome_cadastro = self.registration_window.nome.text()
        self.login_cadastro = self.registration_window.login.text()
        
        self.registration_window.show()
        
    def register_new_user(self):
        if self.verifier.verify_password_of_register(self.password_register, self.register_password_confirmation) == True:
            result = self.database.register_the_new_user_on_database(self.nome_cadastro, self.login_cadastro, self.password_register, self.register_password_confirmation)
            self.show_dialog(result)
    
    
    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)
            
        
class Database():
    def __init__(self):
        self.banco = sqlite3.connect(
            'banco_cadastro.db')
        self.cursor = self.banco.cursor()


    def colect_password_database(self, username):
        
        self.cursor.execute(
            "SELECT senha FROM cadastro WHERE login ='{}'".format(username)
            )
        
        database_password = self.cursor.fetchall()

        return database_password
    
    
    def close_db(self):
        self.banco.close()
        
    def register_the_new_user_on_database(self, nome_cadastro, login_cadastro, password_register, register_password_confirmation):
        senha_criptografada_do_cadastro = cryptocode.encrypt(
            f'{password_register}', 'senha@123'
            )
        senha_criptograda_confimacao_do_cadastro = cryptocode.encrypt(
            f'{register_password_confirmation}', 'senha@123'
            )
        
        
        try:
            self.banco = sqlite3.connect(
                'banco_cadastro.db') 
            self.cursor = self.banco.cursor()
            self.cursor.execute(
                "INSERT INTO cadastro VALUES ('"+nome_cadastro+"',"
                f"'"+login_cadastro+"','"+senha_criptografada_do_cadastro+"')")
            self.banco.commit()
            
            return f"User {nome_cadastro} registered with sucess!"
            
            
        except sqlite3.Error as erro:
            
            
            return erro


        
        
class Verifier():
    def __init__(self) -> None:
        pass
    
    def verify_user_admin(self, username):
        if username == "admin":
            
            
            return True

    def verify_password(self, password, database_password):        
        try:
                    
            decrypted_db_password = cryptocode.decrypt(
            f'{database_password[0][0]}','senha@123'
            )
        
            
            if password == decrypted_db_password:
                
                return True
            
            
        except:
            return False
    
       
    def validate_user(self):
        if self.verify_password() == True:
            
         
            # self.name_of_user_on_screen()
            pass
            
        else:
            
        
            return False
        
    def verify_password_of_register(self, password_register, register_password_confirmation):
        if password_register == register_password_confirmation:
            
            
            return True
        
    
        

class Interface:
    def __init__(
        self, first_window, second_window,
        register_window, admin_window, error_window,
        window_key, window_balance
        ):

        self.error_window = uic.loadUi(error_window)
        self.error_window.label.setText("")
        self.binance_data = BinanceApi()


        self.key_window = uic.loadUi(window_key)
        self.key_window.botao_config.clicked.connect(self.criar_env)

        
        self.balances_window = uic.loadUi(window_balance)
        self.lista_janelas = [
            self.home_window, self.registration_window,
            self.admin_window, self.error_window, self.key_window, self.balances_window
            ]
    
    
    def start_window(self, window):
        window.show()
    
    
    def close_window(self, window):
        window.close()
      
        
    def start_first_window(self):
        self.login_window.show()
   
    def show_error_pop_up_window(self, erro):
        self.close_window(self.error_window)
        self.start_window(self.error_window)
        self.error_window.label.setText(f"{erro}")


    def show_database_error_on_first_screen(self):
        self.login_window.label_3.setText(
            "Database ecxeption"
            )


    def erro_usuario_senha(self):
        self.login_window.label_3.setText(
            "username or password is invalid!"
            )


    def delete_env(self):
        if self.binance_data.verify_existence_of_env() == True:
            os.remove(".env")
    
    
    def criar_env(self):
        self.api = self.key_window.apy_key.text()
        self.secret = self.key_window.secret_key.text()
        api_text = (f'API_KEY = "{self.api}"\n')
        secret_text = (f'SECRET_KEY = "{self.secret}"')
        final_text = (api_text+secret_text)
        env = '.env'
        
        with open(env, 'w+') as writer:
            self.escritor = writer.writelines(final_text)
        
        self.close_window(self.key_window)
        self.start_window(self.error_window)
        self.show_error_pop_up_window(
            "Api e secret key set with sucess!"
            )


    def error_incorrect_user(self):
        self.login_window.label_3.setText(
            "Incorrect login data!"
            )

      

    def cadastro_tela(self):
        self.start_window(self.registration_window)
    
    
    def colect_data_from_excel(self):
        self.binance_data.coins_with_balance_on_account()
       
        
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
        self.balances_window.tableWidget.setRowCount(numero_linhas_df)
        self.balances_window.tableWidget.setColumnCount(df.shape[1])
        self.balances_window.tableWidget.setHorizontalHeaderLabels(df.columns)
        

        for row in df.iterrows():
            values = row[1]
            
            
            for col_index, value in enumerate(values):
                
                
                if isinstance(value, (float, int)):
                    value = '{0:0,.9f}'.format(value)
                    
                table_item = QTableWidgetItem(str(value))
                self.balances_window.tableWidget.setItem(row[0], col_index, table_item)
        
                    
    def get_ballance_from_binance(self):
        if  self.binance_data.verify_existence_of_env() == True:
            self.start_window(self.balances_window)
            
            if self.binance_data.test_env() == True:
                self.colect_data_from_excel()
                self.home_window.label_resultado.setText("")
                self.generate_info_ballance()
               
                
            else:
                self.show_error_pop_up_window(
                    'API or SECRET KEY was not set correctly, please do again the configuration'
                    )
                
                
        else:
            self.start_window(self.error_window)
            self.show_error_pop_up_window(
                "Please set your API_KEY and SECRET_KEY on the home screen before proceeding!!"
                )


    def add_api_key(self):
        if self.binance_data.verify_existence_of_env() == True:
            self.start_window(self.error_window)
            self.show_error_pop_up_window(
                "APY_KEY Already configured, logout and login again to add a new APY_KEY"
                )
            
            
        else:
            self.start_window(self.key_window)
        
        

            
    def admin_name_on_screen(self):
        self.admin_window.nome_user.setText(f"{self.username}")
        
        
    def name_of_user_on_screen(self):
        self.home_window.nome_user.setText(f"{self.username}")
        
        
    def close_all_windows(self):
        for window in self.lista_janelas:
            window.close()


    def logout(self):
        self.close_all_windows()
        self.start_window(self.login_window)
        self.clean_user_password()
        self.delete_env()


if __name__ == "__main__":   
    app=QtWidgets.QApplication([])
    # iniciar_interface = Interface(
    #     f ,
    # , "Interfaces/tela_erro.ui",
    # "Interfaces/tela_key.ui", "Interfaces/tela_saldo.ui"
    # )
    login = LoginInterface()

    app.exec()
    # iniciar_interface.ver_saldo()

