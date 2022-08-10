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
             
    def coins_with_balance_on_account(self):
        if self.verify_existence_of_env() == True:
            self.open_the_env()
            self.delete_xlsx()
            self.add_column_index_to_xlsx()
            informations = self.get_binance_data()
            list_of_balances = informations["balances"]
            
            
            for self.cripto in list_of_balances:
                
                
                if float(self.cripto["free"]) > 0:
                    
                    
                    dados = self.send_data_to_rows(self.data_xlsx())
        
                    self.send_data_to_sheet(dados)
                    
                    
                    
        else:
            print("erro sem env")
            
    def verify_existence_of_env(self):
        if os.path.exists(self.env):
            
            return True
      
    def verify_api_key(self):
        c = self.open_the_env()[0]
        d = self.open_the_env()[1]
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
        informations_of_account = client.get_account()
        
        
        return informations_of_account
        
    def open_the_env(self):
        with open(self.env) as reader:
            self.leitor = reader.readlines()
            
            
        return self.leitor
    
    def verify_content_of_env(self):
        if self.verify_existence_of_env() == True:
            self.open_the_env()
            
            
        else:
  
  
            return False
        
        
    def send_data_to_sheet(self, dados):
        dados.to_excel('saldo.xlsx', index = True)
        
        
    def send_data_to_rows(self, data_frame):
        df = pd.read_excel('saldo.xlsx', index_col=0)
        new_row = pd.DataFrame(data_frame)
      
        p = pd.concat([new_row, df]).reset_index(drop = True)
        
        
        return p
        
    
    def add_column_index_to_xlsx(self):
        columns = {'nome moeda':[], 'saldo moeda':[]}
        data = pd.DataFrame(columns)
        data.to_excel('saldo.xlsx', index=True)
        
        
        
    def delete_xlsx(self):
        if os.path.exists('saldo.xlsx'):
            os.remove('saldo.xlsx')
        
        
    def data_xlsx(self):
        
        name_of_coin = self.cripto['asset']
        value_of_coin = str(self.cripto['free']).zfill(10)
        dados = {'nome moeda': [f'{name_of_coin}'], 'saldo moeda': [f'{value_of_coin}']}
        
        
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

# bot = Binance_bot()
# bot.verify_content_of_env()
# bot.moedas_com_saldo()

# c = bot.test_env()
# print(c)


#bot.moedas_com_saldo()