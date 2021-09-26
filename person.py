from client import client

class Person:
    def __init__(self, stock):
        self.money = float(client.get_account()['balances'][2]['free'])
        self.coin = float(client.get_account()['balances'][21]['free'])
        self.action = '-'
        self.price_diff = ''
        self.stock = None
        self.direction = None
        self.initial_buy = 0
        self.buyCounter = 0
        self.dogeCoin = stock

    '''
    RUN:
        Will execute persons action
    '''
    def run(self, stock, direction):
        self.stock = stock
        self.direction = direction
        self.set_action()
        self.get_price_difference()

    '''
    SET ACTION:
        The master piece!
    '''
    def set_action(self):
        if self.stock.change() > float(self.stock.close_price) * 0.003 and self.money > 0:
            self.buy(self.stock.close_price)
        elif self.direction == 'down' and self.coin > 0 and self.stock.change() < self.stock.close_price * -0.003:
            self.sell(self.stock.close_price)
        else:
            pass

    '''
    GET PRICE DIFFERENCE:
        Will set Price Difference when person buys or sells stock
    '''   
    def get_price_difference(self):
        if self.action == 'B':
            self.price_diff = '{:f}'.format(self.stock.change())
        elif self.action == 'S':
            self.price_diff = '{:f}'.format(self.stock.change())
        else:
            self.price_diff = ''

    '''
    BUY:
        Will
    '''   
    def buy(self, close):
        self.dogeCoin.BUY()
        self.action = 'B'
        self.coin = float(client.get_account()['balances'][21]['free'])
        self.money = float(client.get_account()['balances'][2]['free'])

    '''
    SELL:
        Will 
    '''   
    def sell(self, close):
        self.dogeCoin.SELL()
        self.money = float(client.get_account()['balances'][2]['free'])
        self.coin = float(client.get_account()['balances'][21]['free'])
        self.action = 'S'
    
    '''
    GET money:
        Will get the amount of money the person has
    '''   
    def get_money(self, close):
        if self.money == 0:
            return self.coin * close
        else:
            return self.money

    '''
    GET ACTION AND DIFFERENCE:
        Will return persons action and difference in price from action
    '''   
    def get_action_and_difference(self):
        if self.action == '-':
            return ''
        else:
            diff = ('{}: {}'.format(self.action, self.price_diff))
            self.action = '-'
            return diff

    '''
    DISPLAY INFO:
        For Debugging
        Will display:
            Money
            Coin
    '''   
    def display_info(self):
        print('Amount of money: ${}'.format(self.money))
        print('Amount of coin: ${}'.format(self.coin))