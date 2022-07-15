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
        
    def enviar_para_planilha(self):
        self.data_frame.to_excel('saldo.xlsx', index = True )
        
    def adicionar_dados_para_linhas_excel(self):
        self.data_frame.loc[len(self.data_frame)] = [f'{self.nome_moeda}',f'{self.valor_da_moeda}']
        
    def dados_xlsx(self):
        
        self.nome_moeda = self.cripto['asset']
        self.valor_da_moeda = self.cripto['free']
        self.dados = {'nome moeda': [f'{self.nome_moeda}','asdasjd'], 'saldo moeda': [f'{self.valor_da_moeda}','asdjasd']}
        self.data_frame = pd.DataFrame(self.dados)
        print(self.dados)
        
            
    def moedas_com_saldo(self):
        if self.verificar_existencia_env() == True:
            self.abrir_env()
            for self.cripto in self.lista_saldos:
                if float(self.cripto["free"]) > 0:
                    self.dados_xlsx()
                    self.adicionar_dados_para_linhas_excel()
        
                    self.enviar_para_planilha()
        else:
            print("erro sem env")

bot = Binance_bot()
#bot.verificar_conteudo_env()
bot.moedas_com_saldo()


#bot.moedas_com_saldo()