# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 21:07:35 2019

@author: Tobias
"""

import wrds
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv

db = wrds.Connection()
db.list_libraries()

db.list_tables(library='crsp')

data = db.raw_sql('SELECT * FROM crsp.stocknames', index_col='permco')
data.head()

ticker = data['ticker']
os.chdir('C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Ticker-PERMNO-mapping')
with open( 'permnoticker.pickle', 'wb') as file:
    pickle.dump(ticker, file)
    
uniques=ticker.index.unique()
out=pd.DataFrame()
permco=[]
tickerT=[]
for uni in uniques:
   temp = data.loc[uni]
   if temp is None:continue
   permco.append(uni)
   if isinstance(temp,str):
       tickerT.append(temp)         
        
        
#   if isinstance(temp,pd.DataFrame):
#       tickerT.append(temp.iloc[-1])   
   else:
       try:
           tickerT.append(temp.TICKER)
       except:
           tickerT.append(temp.iloc[-1].name)

ticker=pd.DataFrame({'permno':permno,'ticker':tickerT})
with open( 'permnotickerclean.pickle', 'wb') as file:
    pickle.dump(ticker, file)
    
    
    
    
    
    
    
f=crsp.set_index('TICKER')
vars=tickers.var()
vars=vars.index.get_values()
permco=[]
name  =[]
for v in vars:
    try:
        temp=f.loc[v]
        num=temp.PERMCO.unique()
        name.append(v)
        if len(num)==1: permco.append(num[0])
        else: permco.append(num[-1])
    except:print(v)

data_out=pd.DataFrame({'ticker':name,'permco':permco})
data_out=data_out.set_index('ticker')
with open( 'permcotickerclean.pickle', 'wb') as file:
    pickle.dump(data_out, file)
    
f=crsp
#f['dates']=f.index.get_values()
f=f.set_index('PERMCO')
ret=[]
val=[]
out_ret=pd.DataFrame({'MMM':ret.values})
out_ret.index = temp.index
out_val=pd.DataFrame({'MMM':val})
dates=temp.index
dates=[str(d)[0:4]+'-'+str(d)[4:6]+'-'+str(d)[6:8] for d in dates]
out_ret.index = dates
out_val.index = dates
for perm in permco:
    temp=f.loc[perm]
    temp=temp.set_index('dates')
    ret = np.log(temp.RET+1)
    val = temp.SHROUT*temp.PRC
    try:
        out_ret[temp.TICKER.iloc[-1]] = ret
        out_val[temp.TICKER.iloc[-1]] = val
    except:print(temp.TICKER.iloc[-1])
with open( 'returnsfiltered.pickle', 'wb') as file:
    pickle.dump(out_ret, file)
with open( 'valuefiltered.pickle', 'wb') as file:
    pickle.dump(out_val, file)
    
    
    
    
#comp_names=get_sp500_tickers()
c_n=comp_names[5]
c_n=c_n.upper()
try:
    f.loc[c_n]
except:
     try:
         c_n=c_n.rstrip('.')
         f.loc[c_n] 
     except:
         c_n=c_n.replace('COMPANY','CO')
         f.loc[c_n]
    
Ratio = fuzz.ratio(Str1.lower(),Str2.lower())

crsp_names=list(crsp.COMNAM.values)
crsp_names = set(crsp_names)
t=process.extractOne(c_n, crsp_names)
comp_names=pd.read_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\Returns\all_names.csv')
comp_names=comp_names.values.tolist()
comp_names=[c[0] for c in comp_names]
ln=[]
comp_names_clean=[c.replace('CORP','') for c in comp_names]
comp_names_clean=[c.replace('INC','') for c in comp_names_clean]
comp_names_clean=[c.replace('Inc','') for c in comp_names_clean]

crsp_names_clean=[c.replace('CORP','') for c in crsp_names]
crsp_names_clean=[c.replace('INC','') for c in crsp_names_clean]
crsp_names_clean=[c.replace('Inc','') for c in crsp_names_clean]
crsp_names=list(crsp_names)
for c,cccc in zip(comp_names_clean,comp_names):
    match = process.extractOne(c, crsp_names_clean)
    ind = [i for i, s in enumerate(crsp_names_clean) if match[0] in s]
    ln.append([cccc,crsp_names[ind[0]],match[1]])
    print([cccc,process.extractOne(c, crsp_names)[0],match[1]])
    
    
    
    
list_with_names=pd.DataFrame(ln)
list_with_names.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\Returns\namematching.csv', index = None, header=True)

pd.read_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\Returns\namematching.csv', index = None, header=True)
# Get PERMCO
list_with_names.values
comps = [c[1] for c in list_with_names.values]
couple=[]
single=[]


return_data=pd.DataFrame({crsp_temp.TICKER.iloc[-1]: pd.to_numeric(crsp_temp.RET,errors='coerce')})

v= crsp_temp.SHROUT*crsp_temp.PRC
value_data = pd.DataFrame({crsp_temp.TICKER.iloc[-1]:v.values})
return_data.index= crsp_temp.RET.index
value_data.index=v.index
for com in comps:
   crsp_temp = crsp[crsp.COMNAM == com]
   # single.append(crsp_temp.PERMCO.unique()[0])
   # couple.append([com,crsp_temp.PERMCO.unique()[0]])
   crsp_temp=crsp_temp.set_index('date')
   try:
       
      # return_data[crsp_temp.TICKER.iloc[-1]] =  pd.to_numeric(crsp_temp.RET,errors='coerce')
       value_data[crsp_temp.TICKER.iloc[-1]]  = crsp_temp.SHROUT*crsp_temp.PRC
   except: print(com)
   
# Save
dates=list(value_data.index.get_values())
dates=crsp_temp.date
dates=[str(d)[0:4]+'-'+str(d)[4:6]+'-'+str(d)[6:8] for d in dates]
return_data.index=dates
value_data.index =dates
return_data.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\Returns\'+ReturnData.csv', header=True)
value_data.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\Returns\ValueData.csv'  , header=True)



return_data=pd.read_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\Returns\ReturnData.csv')
value_data=pd.read_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\Returns\ValueData.csv' )







 0.028278
 0.039586
    