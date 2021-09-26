from stock import Stock

class StockList:
    def __init__(self, symbols_file):
        self.symbols_file = symbols_file
        self.get_list_of_symbols()
        self.get_list_of_stocks()
        self.list_of_stock = self.get_list_of_stocks()

    '''
    GET LIST OF SYMBOLS:
        Will get a list of symbols
    '''
    def get_list_of_symbols(self):
        f = open(self.symbols_file, "r")
        self.symbols = f.read().splitlines()
        f.close()

    '''
    GET LIST OF STOCKS:
        Will create a list of stocks
    '''
    def get_list_of_stocks(self):
        stock_list = []
        for symbol in self.symbols:
            new_stock = Stock(symbol)
            stock_list.append(new_stock)
        return stock_list