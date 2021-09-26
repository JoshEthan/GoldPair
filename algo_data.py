class Algo_data:
    def __init__(self, list_of_stock):
        self.direction = None
        self.list_of_stock = list_of_stock
        self.up = 0
        self.down = 0
    
    '''
    RUN:
        Will get direction of of the market
    '''
    def run(self):
        self.get_direction()

    '''
    GET DIRECTION:
        Will determine if market is 'up', 'down',
            or 'neither' based on 'up' and 'down' percentages
    '''
    def get_direction(self):
        self.get_percentage()
        if self.up == 100:
            self.direction = 'up'
        elif self.down == 100:
            self.direction = 'down'
        else:
            self.direction = 'neither'

    '''
    GET PERCENTAGE:
        Will get the percentage 'up' and 'down'
    '''
    def get_percentage(self):
        self.up = 0
        self.down = 0
        for stocks in self.list_of_stock.list_of_stock:
            if stocks.change() > 0:
                self.up += 1
            elif stocks.change() < 0:
                self.down += 1
            else:
                self.up += 0
        self.up = (self.up/len(self.list_of_stock.list_of_stock)) * 100
        self.down = (self.down/len(self.list_of_stock.list_of_stock)) * 100
   
    '''
    DISPLAY INFO:
        For debugging
        Will print:
            Symbol File
            Direction
            Stocks
            Up %
            Down %
    '''
    def display_info(self):
        print('Direction: {}'.format(self.direction))
        # for x in range(len(self.list_of_stock.list_of_stock)):
        #     self.list_of_stock.list_of_stock[x].display_info()
        print('Up: {}'.format(self.up))
        print('Down: {}'.format(self.down))