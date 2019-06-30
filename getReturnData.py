# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:45:33 2019

Helping functions
"""
import pandas as pd
import pandas_datareader as web
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import pickle
import requests
import bs4 as bs
import sys
from scipy.optimize import minimize
import os

def get_sp500_tickers():
    '''
    Scraping function to get tickers from members of the S&P 500 index. 
    Inputs : NONE
    Output: 
     - tickers : The tickers of all members of the S&P 500 index
    '''
    resp    = requests.get('http://en.wikipedia.org/wiki/List_of_S%'+
                           '26P_500_companies')
    soup    = bs.BeautifulSoup(resp.text, 'lxml')
    table   = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[1].text
        tickers.append(ticker)
    tickers = [t.replace('\n','') for t in tickers]
   # with open('sp500tickers.pickle', 'wb') as f:
    #    pickle.dump(tickers, f)
    return tickers



path='C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Returns'
os.chdir(path)
with open('sp500tickers.pickle', 'rb') as file:
       tickers = pickle.load(file)


data   = pd.DataFrame()
start  = dt.datetime(1996, 1, 1)
end    = dt.datetime(2019,1,1)
for ticker in tickers:
    try:
        data[ticker] = web.get_data_yahoo(ticker,start=start,end=end)['Close']
        print(ticker)
    except: pass
        
with open('sp500prices.pickle', 'wb') as file:
       pickle.dump(data,file)
       
ret_daily    = np.log(data / data.shift(1))


