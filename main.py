import schedule, time
from stockList import StockList
from sheets import Sheets
from algo_data import Algo_data
from person import Person


list_of_stocks = StockList('symbols.txt')
m1 = Algo_data(list_of_stocks)
p1 = Person(list_of_stocks.list_of_stock[1])
sheet = Sheets()

def job():
    print('============================================================')
    for stock in list_of_stocks.list_of_stock:
        stock.update()
        # stock.display_info()
    m1.run()
    p1.run(m1.list_of_stock.list_of_stock[0], m1.direction)
    row = [
        m1.list_of_stock.list_of_stock[0].current_time, 
        m1.direction, 
        m1.list_of_stock.list_of_stock[0].close_price, 
        p1.get_money(m1.list_of_stock.list_of_stock[0].close_price), 
        p1.coin, 
    ]
    sheet.add_row(row)
    # m1.display_info()


schedule.every(1).minute.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)