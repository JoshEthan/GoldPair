from client import client
from binance import Client
from datetime import datetime
from pytz import timezone


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.candles = client.get_klines(symbol=self.symbol, interval=Client.KLINE_INTERVAL_1MINUTE)
        self.open_price = float(self.candles[499][1])
        self.close_price = float(self.candles[499][4])

        self.current_time = self.get_current_time()
        self.close_price_list = []
        self.list_size = 20
        self.dogeChange = ''

    '''
    UPDATE:
        Will update the stock information
    '''
    def update(self):
        self.candles = client.get_klines(symbol=self.symbol, interval=Client.KLINE_INTERVAL_1MINUTE)
        print(self.candles[499][1])
        self.open_price = self.candles[499][1]
        self.close_price = self.candles[499][4]
        self.current_time = self.get_current_time()
        self.update_close_price_list()

    '''
    UPDATE CLOSE PRICE LIST:
        ???
    '''
    def update_close_price_list(self):
        if len(self.close_price_list) == self.list_size:
            self.close_price_list.pop(0)
            self.close_price_list.append(self.close_price)
        else:
            self.close_price_list.append(self.close_price)

    '''
    CHANGE:
        Will get the change in price
    '''
    def change(self):
        #change = (self.close_price - self.open_price)   # / self.open_price
        #if (self.symbol == 'DOGE'):
            # print('{:.4f}'.format(change))
            #self.dogeChange = '{:.4f}'.format(change)
        return (float(self.close_price) - float(self.open_price))

    def BUY():
        amount = float(client.get_account()['balances'][2]['free'])
        order = client.order_market_buy(symbol='DOGEUSDT', quantity=amount)
        print(order)

    def SELL():
        amount = float(client.get_account()['balances'][21]['free'])
        order = client.order_market_sell(symbol='DOGEUSDT', quantity=amount)
        print(order)


    '''
    GET CURRENT TIME:
        Will get the current time
    '''
    def get_current_time(self):
        datetime_obj = datetime.now().replace(tzinfo=timezone('US/Arizona'))
        return datetime_obj.strftime("%H:%M:%S\n%m/%d/%Y")
    
    '''
    DISPLAY INFO:
        For Debugging
        Will display:
            Symbol
            Price
            Time
    '''
    def display_info(self):
        print('\tSymbol: {}'.format(self.symbol))
        print('\tPrice: {}'.format(self.open_price))
        print('\tTime: {}'.format(self.current_time))