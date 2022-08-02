from operator import ne
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
        
        
    def enviar_para_planilha(self, dados):
        dados.to_excel('saldo.xlsx', index = True)
        
        
    def adicionar_dados_para_linhas_excel(self, data_frame):
        df = pd.read_excel('saldo.xlsx', index_col=0)
        new_row = pd.DataFrame(data_frame)
      
        p = pd.concat([new_row, df]).reset_index(drop = True)
        
        return p
        
    
    def adicionar_legenda_xlsx(self):
        columns = {'nome moeda':[], 'saldo moeda':[]}
        data = pd.DataFrame(columns)
        data.to_excel('saldo.xlsx', index=True)
        
        
        
    def deletar_xlsx(self):
        if os.path.exists('saldo.xlsx'):
            os.remove('saldo.xlsx')
        
        
    def dados_xlsx(self):
        
        nome_moeda = self.cripto['asset']
        valor_da_moeda = str(self.cripto['free']).zfill(10)
        dados = {'nome moeda': [f'{nome_moeda}'], 'saldo moeda': [f'{valor_da_moeda}']}
        
        return dados
        
            
    def moedas_com_saldo(self):
        if self.verificar_existencia_env() == True:
            self.abrir_env()
            self.deletar_xlsx()
            self.adicionar_legenda_xlsx()
            for self.cripto in self.lista_saldos:
                if float(self.cripto["free"]) > 0:
                    
                    
                    dados = self.adicionar_dados_para_linhas_excel(self.dados_xlsx())
        
                    self.enviar_para_planilha(dados)
        else:
            print("erro sem env")

bot = Binance_bot()
#bot.verificar_conteudo_env()
# bot.moedas_com_saldo()


#bot.moedas_com_saldo()