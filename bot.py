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
             
    def moedas_com_saldo(self):
        if self.verificar_existencia_env() == True:
            self.abrir_env()
            self.deletar_xlsx()
            self.adicionar_legenda_xlsx()
            informations = self.get_binance_data()
            lista_saldos = informations["balances"]
            
            
            for self.cripto in lista_saldos:
                
                
                if float(self.cripto["free"]) > 0:
                    
                    
                    dados = self.adicionar_dados_para_linhas_excel(self.dados_xlsx())
        
                    self.enviar_para_planilha(dados)
                    
                    
                    
        else:
            print("erro sem env")
            
    def verificar_existencia_env(self):
        if os.path.exists(self.env):
            
            return True
      
    def verify_api_key(self):
        c = self.abrir_env()[0]
        d = self.abrir_env()[1]
        if "API_KEY" in c and "SECRET_KEY" in d:
            
            
            return True
        
        
    def get_api_key(self):
        api_key = os.getenv("API_KEY")
        
        
        return api_key
    
    
    def get_secret_key(self):
        secret_key = os.getenv("SECRET_KEY")
        
        
        return secret_key
    
    
    def get_binance_data(self):
        api_key = self.get_api_key()
        secret_key = self.get_secret_key()
        
        client = Client(api_key, secret_key)
        informacoes = client.get_account()
        
        
        return informacoes
        
    def abrir_env(self):
        with open(self.env) as reader:
            self.leitor = reader.readlines()
            
            
        return self.leitor
    
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

    def test_env(self):
        if self.verify_api_key() == True:
            api_key = self.get_api_key()
            secret_key = self.get_secret_key()
            
            try:
                client = Client(api_key, secret_key)
                client.get_account()
                return True
                
            except:
                
                
                return False
            
            
        else:
            return False

bot = Binance_bot()
bot.verificar_conteudo_env()
bot.moedas_com_saldo()

# c = bot.test_env()
# print(c)


#bot.moedas_com_saldo()