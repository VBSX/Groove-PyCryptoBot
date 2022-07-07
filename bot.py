from dotenv import load_dotenv
import os
from binance.client import Client
from binance.enums import *
#from logon import Interface

class Binance_bot():
    def __init__(self):
        
        # self.API_KEY = os.getenv("API_KEY")
        # self.SECRET_KEY = os.getenv("SECRET_KEY")
        # self.client = Client(self.API_KEY, self.SECRET_KEY)
        # self.informacoes = self.client.get_account()
        # self.lista_saldos = self.informacoes["balances"]
        self.env = '.env'
    
    def verificar_existencia_env(self):
        if os.path.exists(self.env):
            return True
    
    def verificar_apy_key_existe(self):
        c = self.leitor[0]
        d = self.leitor[1]
        if "API_KEY" in c and "SECRET_KEY" in d:
            return True
        
    def abrir_env(self):
        with open(self.env) as reader:
            self.leitor = reader.readlines()
            
    
            
    def verificar_conteudo_env(self):
        if self.verificar_existencia_env() == True:
            self.API_KEY = os.getenv("API_KEY")
            self.SECRET_KEY = os.getenv("SECRET_KEY")
            self.client = Client(self.API_KEY, self.SECRET_KEY)
            self.informacoes = self.client.get_account()
            self.lista_saldos = self.informacoes["balances"]
            
            self.abrir_env()
        else:
            return False

    def moedas_com_saldo(self):
        for self.cripto in self.lista_saldos:
            if float(self.cripto['free']) > 0:
                print(self.cripto)


bot = Binance_bot()
#bot.verificar_conteudo_env()


#bot.moedas_com_saldo()