
import robin_stocks as r
import datetime
import time
from idlelib.multicall import r
from turtle import pd

username = 'marcusogutu430@gmail.com'
 password = 'password'

 login = r.login(username, password)

 r.build_holdings()

var = {'KMI': {'price': '13.990000',
               'quantity': '1.00000000',
               'average_buy_price': '0.000',
               'equity': '13.99',
               'percent_change': '0.00',
               'equity_change': '13.9900000',
               'type': 'stock',
               'name': 'Kinder Morgan',
               'id': '346c3dc3-2ef4-470f-aa67-0471cffeb299',
               'pe_ratio': '13.939700',
               'percentage': '100.00'}}

r.profiles.load_basic_profile()

def visualize_price(ticker_list, span= 'year', bounds= 'regular', ticket_list=None):
    for t in range(len(ticket_list)):
        name = str(r.get_name_by_symbol(ticker_list[t]))
        hist = r.stocks.get_historicals(ticker_list[t], span=span, bounds=bounds)

        hist_df = pd.DataFrame()
        for i in range(len(hist)):
            df = pd.DataFrame(hist[i], index= [i])
            hist_df = pd.concat( [hist_df,df] )
        hist_df.begins_at = pd.to_datetime(hist_df.begins_at, infer_datetime_format=True)

        hist_df.open_price = hist_df.open_price.astype('float32')
        hist_df.close_price = hist_df.close_price.astype('float32')
        hist_df.high_price = hist_df.high_price.astype('float32')
        hist_df.low_price = hist_df.low_price.astype('float32')


        ax = hist_df.plot(x = 'begins_at', y='open_price', figsize= (16.8))
        ax.fill_between(hist_df.begins_at, hist_df.low_price, hist_df.high_price, alpha=0.5)
        ax.set_xlabel('Date')
        ax.set_ylabel('Price (USD)')
        ax.legend([ticker_list[t]])
        ax.set_title(name)

def extract_list():
    ticker_list = list(r.build_holdings().keys())
    return ticker_list
ticker_list = extract_list()
visualize_price(ticker_list, span = 'year', bounds = 'regular')




