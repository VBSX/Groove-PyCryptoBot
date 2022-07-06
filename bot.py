from dotenv import load_dotenv
import os
from binance.client import Client
from binance.enums import *
#from logon import Interface


class Binance_bot():
    def __init__(self):
        self.API_KEY = os.getenv("API_KEY")
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.client = Client(self.API_KEY, self.SECRET_KEY)
        self.informacoes = self.client.get_account()
        self.lista_saldos = self.informacoes["balances"]
        
    def moedas_com_saldo(self):
        for self.cripto in self.lista_saldos:
            if float(self.cripto['free']) > 0:
                print(self.cripto)

       

bot = Binance_bot()
bot.moedas_com_saldo()



