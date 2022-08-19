import os
from time import sleep
from binance.client import Client
from binance.enums import *
import pandas as pd
from datetime import datetime


class BinanceApi():
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
            
            
            return False
    
    def get_realtime_price_of_coins(self, pair_of_coin):
        client = self.get_client()
        candles = client.get_historical_klines(pair_of_coin, Client.KLINE_INTERVAL_1MINUTE, "1 minute ago UTC")

        
        return candles[0][1]
      
    
    def get_avarage_price_coin(self, pair_of_coin):
        client = self.get_client()
        avg_price = client.get_avg_price(symbol=pair_of_coin)
        
        
        return avg_price
    
    
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
        client = self.get_client()
        informations_of_account = client.get_account()
        
        
        return informations_of_account
    
    
    def get_client(self):
        api_key = self.get_api_key()
        secret_key = self.get_secret_key()
        client = Client(api_key, secret_key)
        
        
        return client
    
    
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


class BinanceBot(BinanceApi):
    def __init__(self, pair_of_coins,how_much_to_buy, stop_loss, stop_gain):
        self.pair_of_coins = pair_of_coins
        self.how_much_to_buy = how_much_to_buy
        self.stop_loss = stop_loss
        self.stop_gain = stop_gain
    
    
    def price_to_stop_gain(self):
        actual_price = float(self.get_realtime_price_of_coins(self.pair_of_coins))
        percentage = self.get_percentage(self.stop_gain)
        price_to_stop = (actual_price*percentage)+actual_price
        
        
        return price_to_stop
      
        
    def price_to_start_trade(self, desired_price):
        actual_price = float(self.get_realtime_price_of_coins(self.pair_of_coins))
        
        
        if actual_price == desired_price:
            
            
            return True
      
        
    def percentage_to_stop_loss(self):
        actual_price = float(self.get_realtime_price_of_coins(self.pair_of_coins))
        percentage = self.get_percentage(self.stop_loss)
        price_with_percentage = (actual_price*percentage)
        price_to_stop_lose = actual_price-price_with_percentage
        
        
        return price_to_stop_lose
    
    
    def get_percentage(self, number):
        result = number/100
        
        
        return result
    
    
    def get_time(self):
        time = datetime.now()
        actual_hour = time.strftime('%d/%m/%Y %H:%M')
        
        
        return actual_hour


    def wait_price_to_buy(self, price_of_coin, desired_price):
        while price_of_coin > desired_price:
            sleep(10)
            print('\n desired price: ', desired_price, '\n')
            price_of_coin = float(bot.get_realtime_price_of_coins(pair_of_coin))
            print(f'\n price update: {price_of_coin} at {self.get_time()} \n')
            
            
        return price_of_coin
        

if __name__ == "__main__":
    
    pair_of_coin = 'BTCBRL'
    how_much_to_buy = 1
    bot = BinanceBot(pair_of_coin, how_much_to_buy, 1, 1)
    price_of_coin = float(bot.get_realtime_price_of_coins(pair_of_coin))
    print('this is the actual price: ', price_of_coin)
    percentage_to_buy = 0.1
    desired_price = price_of_coin-(bot.get_percentage(percentage_to_buy)*price_of_coin)
    print('this is the desired price to buy: ', desired_price)
    price_bought = bot.wait_price_to_buy(price_of_coin, desired_price)
    print('buy coin')
    print(f'coin buyed for {price_bought} at {bot.get_time()}')

    # bot.verify_content_of_env()
    # bot.moedas_com_saldo()

    # c = bot.test_env()
    # print(c)
   
    #bot.moedas_com_saldo()