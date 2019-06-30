# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 12:24:57 2019

@author: Tobias

Working examples for fetching data:
    uk  = web.get_data_fred('DEXUSUK',start=start,end=end)
    mcd = web.get_data_yahoo(['MCD'],start=start,end=end)
    

"""

import bs4 as bs
import datetime as dt
import os
import pandas_datareader.data as web
import pickle
import requests
import fix_yahoo_finance as yf


# First, get an updated list of tickers from Wikipedia
def get_sp500_tickers():
    resp    = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup    = bs.BeautifulSoup(resp.text, 'lxml')
    table   = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[1].text
        tickers.append(ticker)
    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)
    return tickers

start = dt.datetime(2000,3, 3)
end   = dt.datetime(2018,1,1)

# Loop over tickers, get time series data
def get_data_from_yahoo(start, end, reload_sp500=False):
    if reload_sp500:
        tickers = get_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
    notfetchable = []
    for ticker in tickers:
        # just in case your connection breaks, we'd like to save our progress!
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            try:
                df = web.get_data_yahoo(ticker,start=start,end=end)
                df.reset_index(inplace=True)
                df.set_index("Date", inplace=True)
    #            df = df.drop("Symbol", axis=1)
                df.to_csv('stock_dfs/{}.csv'.format(ticker))
            except: 
                print('Could not fetch '+ ticker)
                notfetch = ticker
                notfetchable.append(notfetch)
        else:
            print('Already have {}'.format(ticker))
            
    if notfetchable:
        with open("notfetchable.pickle", "wb") as f:
            pickle.dump(tickers, f)
        
