from dotenv import load_dotenv
import os
from binance.client import Client
from binance.enums import *
import pandas as pd
#from logon import Interface

class Binance_bot():
    def __init__(self):
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
        self.API_KEY = os.getenv("API_KEY")
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.client = Client(self.API_KEY, self.SECRET_KEY)
        self.informacoes = self.client.get_account()
        self.lista_saldos = self.informacoes["balances"]
        with open(self.env) as reader:
            self.leitor = reader.readlines()
         
    def verificar_conteudo_env(self):
        if self.verificar_existencia_env() == True:
            self.abrir_env()
        else:
            return False
    
    def dados_xlsx(self):
        # with pd.ExcelWriter("saldo.xlsx") as writer:
        s = self.cripto['asset']
        d = self.cripto['free']
        dados = {'nome moeda': [f'{s}','asdasjd'], 'saldo moeda': [f'{d}','asdjasd']}
        self.data_frame = pd.DataFrame(dados)
        print(dados)
        self.data_frame.to_excel('saldo.xlsx', index = False)
            
    def moedas_com_saldo(self):
        if self.verificar_existencia_env() == True:
            self.abrir_env()
            for self.cripto in self.lista_saldos:
                if float(self.cripto["free"]) > 0:
                    self.dados_xlsx()
        else:
            print("erro sem env")

bot = Binance_bot()
#bot.verificar_conteudo_env()
bot.moedas_com_saldo()


#bot.moedas_com_saldo()