# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:52:58 2019

@author: Tobias
"""


os.chdir('C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Similarity\\NewsSim\\40')
#os.chdir('C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Similarity\\40')

with open('ranking.pickle', 'rb') as file:
    tickers = pickle.load(file)
    


res1   =  []
res2   =  []
res3   =  []
res4   =  []
res5   =[]
res6   =  []
res7   =  []
res8   = []
res9   = []
res10  =  []
res11   = []
res12   = []
res13   = []
res14   = []
res15  = []
resind = []
resall = []
resff3= []
l =pd.DataFrame()

w1   = []
w2   = []
w3   = []
w4   = []
w5   = [] 
w6   = []
w7   = []
w8   = []
w9   = []
w10  = []
w11  = []
w12  = []
w13  = []
w14  = []
w15  = []



prices    = pd.read_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\Returns\ReturnData.csv',index_col=[0])#return_data
value     = pd.read_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\Returns\ValueData.csv',index_col=[0])#value_data
indX      = pd.DataFrame()
start     = dt.datetime(1996, 1, 1)
end       = dt.datetime(2019,1,1)
indX['^SP500TR'] = web.get_data_yahoo('^SP500TR',dt.datetime(1996, 1, 1),end=dt.datetime(2019,1,1))['Close']
indX       = np.log(indX/indX.shift(1))
tickers   = tickers.loc['1999-07-22':]#tickers.loc[:]:'2010-02-24'
dates     = tickers.index.to_list()
available = list(prices.columns.values)
valids    = [v for v in list(tickers.columns.values) if v in available]
tickers   = tickers[valids]
val       = 1

for ii in range(len(dates)-1):
    data     = tickers.iloc[ii,:]
    data     = data.dropna()
    data     = data.sort_values(axis=0)
    uniques  = data.unique()
    
    lucky_ten = list(split(uniques,5))
    d1  = []
    d2  = []
    d3  = []
    d4  = []
    d5  = []
    d6  = []
    d7  = []
    d8  = []
    d9  = []
    d10  = []  
    d11 = []
    d12 = []
    d13 = []
    d14 = []
    d15 = []  
    for idx, m in enumerate(lucky_ten):
        if idx==0:
            for idy in range(len(m)):
                d1.append(data.loc[data==m[idy]].index.values[0])
            
        if idx==1:
            for idy in range(len(m)):
                d2.append(data.loc[data==m[idy]].index.values[0])
                
        if idx==2:
            for idy in range(len(m)):
                d3.append(data.loc[data==m[idy]].index.values[0])   
        if idx==3:
            for idy in range(len(m)):
                d4.append(data.loc[data==m[idy]].index.values[0])
        if idx==4:
            for idy in range(len(m)):
                d5.append(data.loc[data==m[idy]].index.values[0])
        if idx==5:
            for idy in range(len(m)):
                d6.append(data.loc[data==m[idy]].index.values[0])
        if idx==6:
            for idy in range(len(m)):
                d7.append(data.loc[data==m[idy]].index.values[0])
        if idx==7:
            for idy in range(len(m)):
                d8.append(data.loc[data==m[idy]].index.values[0])
        if idx==8:
             for idy in range(len(m)):
                d9.append(data.loc[data==m[idy]].index.values[0])   
        if idx==9:
            for idy in range(len(m)):
                d10.append(data.loc[data==m[idy]].index.values[0])
        if idx==10:
            for idy in range(len(m)):
                d11.append(data.loc[data==m[idy]].index.values[0])
        if idx==11:
            for idy in range(len(m)):
                d12.append(data.loc[data==m[idy]].index.values[0])
        if idx==12:
            for idy in range(len(m)):
                d13.append(data.loc[data==m[idy]].index.values[0])
        if idx==13:
             for idy in range(len(m)):
                d14.append(data.loc[data==m[idy]].index.values[0])   
        if idx==14:
            for idy in range(len(m)):
                d15.append(data.loc[data==m[idy]].index.values[0])                
    
    port       = np.log(prices[d1].loc[dates[ii]:dates[ii+1]]+1)
    date_ind   = port.index
    temp_ind   = range(len(date_ind))
    port.index = temp_ind
    x          = port.index
    
    portfolio1_r  = np.log(prices[d1].loc[dates[ii]:dates[ii+1]]+1)
    portfolio2_r  = np.log(prices[d2].loc[dates[ii]:dates[ii+1]]+1)
    portfolio3_r  = np.log(prices[d3].loc[dates[ii]:dates[ii+1]]+1)
    portfolio4_r  = np.log(prices[d4].loc[dates[ii]:dates[ii+1]]+1)
    portfolio5_r  = np.log(prices[d5].loc[dates[ii]:dates[ii+1]]+1)
    portfolio6_r  = np.log(prices[d6].loc[dates[ii]:dates[ii+1]]+1)
    portfolio7_r  = np.log(prices[d7].loc[dates[ii]:dates[ii+1]]+1)
    portfolio8_r  = np.log(prices[d8].loc[dates[ii]:dates[ii+1]]+1)
    portfolio9_r  = np.log(prices[d9].loc[dates[ii]:dates[ii+1]]+1)
    portfolio10_r = np.log(prices[d10].loc[dates[ii]:dates[ii+1]]+1)
    portfolio11_r = np.log(prices[d11].loc[dates[ii]:dates[ii+1]]+1)
    portfolio12_r = np.log(prices[d12].loc[dates[ii]:dates[ii+1]]+1)
    portfolio13_r = np.log(prices[d13].loc[dates[ii]:dates[ii+1]]+1)
    portfolio14_r = np.log(prices[d14].loc[dates[ii]:dates[ii+1]]+1)
    portfolio15_r = np.log(prices[d15].loc[dates[ii]:dates[ii+1]]+1)
    ret_index      =   np.log(indX.loc[dates[ii]:dates[ii+1]]+1)
    
    
    
    
    
    portfolio1_r       = portfolio1_r.groupby(x// 21).sum()
    portfolio2_r       = portfolio2_r.groupby(x// 21).sum()
    portfolio3_r       = portfolio3_r.groupby(x// 21).sum()
    portfolio4_r       = portfolio4_r.groupby(x// 21).sum()
    portfolio5_r       = portfolio5_r.groupby(x// 21).sum()
    portfolio6_r       = portfolio6_r.groupby(x// 21).sum()
    portfolio7_r       = portfolio7_r.groupby(x// 21).sum()
    portfolio8_r       = portfolio8_r.groupby(x// 21).sum()
    portfolio9_r       = portfolio9_r.groupby(x// 21).sum()
    portfolio10_r      = portfolio10_r.groupby(x// 21).sum()
    portfolio11_r      = portfolio11_r.groupby(x// 21).sum()
    portfolio12_r      = portfolio12_r.groupby(x// 21).sum()
    portfolio13_r      = portfolio13_r.groupby(x// 21).sum()
    portfolio14_r      = portfolio14_r.groupby(x// 21).sum()
    portfolio15_r      = portfolio15_r.groupby(x// 21).sum()
    ret_index           = ret_index.groupby(x// 21).sum()
    
    
    
    
 #   portfolio11_r =    np.sum(np.log(prices[d11].loc[dates[ii]:dates[ii+1]]+1))
 #   portfolio12_r =    np.sum(np.log(prices[d12].loc[dates[ii]:dates[ii+1]]+1))
 #   portfolio13_r =    np.sum(np.log(prices[d13].loc[dates[ii]:dates[ii+1]]+1))
 ##   portfolio14_r =    np.sum(np.log(prices[d14].loc[dates[ii]:dates[ii+1]]+1))
  #  portfolio15_r =    np.sum(np.log(prices[d15].loc[dates[ii]:dates[ii+1]]+1))
        
    
   
  # ret_ind      =    np.sum(np.log(indX.loc[dates[ii]:dates[ii+1]]+1))
   # ret_all      =    np.sum(np.log(prices.loc[dates[ii]:dates[ii+1]]+1))
   # ret_ff3      =    np.log(data3.loc[dates[ii]:dates[ii+1]]/100+1)
   # ret_ff3      = ret_ff3.groupby(x// 21).sum()
    
    if val:
        portfolio1_v  = value[d1].loc[dates[ii]]/value[d1].loc[dates[ii]].sum()
        portfolio2_v  = value[d2].loc[dates[ii]]/value[d2].loc[dates[ii]].sum()
        portfolio3_v  = value[d3].loc[dates[ii]]/value[d3].loc[dates[ii]].sum()
        portfolio4_v  = value[d4].loc[dates[ii]]/value[d4].loc[dates[ii]].sum()
        portfolio5_v  = value[d5].loc[dates[ii]]/value[d5].loc[dates[ii]].sum()
        portfolio6_v  = value[d6].loc[dates[ii]]/value[d6].loc[dates[ii]].sum()
        portfolio7_v  = value[d7].loc[dates[ii]]/value[d7].loc[dates[ii]].sum()
        portfolio8_v  = value[d8].loc[dates[ii]]/value[d8].loc[dates[ii]].sum()
        portfolio9_v  = value[d9].loc[dates[ii]]/value[d9].loc[dates[ii]].sum()
        portfolio10_v = value[d10].loc[dates[ii]]/value[d10].loc[dates[ii]].sum()
        portfolio11_v = value[d11].loc[dates[ii]]/value[d11].loc[dates[ii]].sum()
        portfolio12_v = value[d12].loc[dates[ii]]/value[d12].loc[dates[ii]].sum()
        portfolio13_v = value[d13].loc[dates[ii]]/value[d13].loc[dates[ii]].sum()
        portfolio14_v = value[d14].loc[dates[ii]]/value[d14].loc[dates[ii]].sum()
        portfolio15_v = value[d15].loc[dates[ii]]/value[d15].loc[dates[ii]].sum()
        if ii==0:
            print('CALCULATING VALUE-WEIGHTED RETURNS')
    
    
    else:
        try:
            portfolio1_v  = 1/len(d1)
            portfolio2_v  = 1/len(d2)
            portfolio3_v  = 1/len(d3)
            portfolio4_v  = 1/len(d4)
            portfolio5_v  = 1/len(d5)
            portfolio6_v  = 1/len(d6)
            portfolio7_v  = 1/len(d7)
            portfolio8_v  = 1/len(d8)
            portfolio9_v  = 1/len(d9)
            portfolio10_v = 1/len(d10)
            portfolio11_v = 1/len(d11)
            portfolio12_v = 1/len(d12)
            portfolio13_v = 1/len(d13)
            portfolio14_v = 1/len(d14)
            portfolio15_v = 1/len(d15)            
            if ii==0:
                print('CALCULATING EQUAL-WEIGHTED RETURNS')
        except: 
            print(ii)
            continue
  
    
    w1.append(value[d1].loc[dates[ii]])
    w2.append(value[d2].loc[dates[ii]])
    w3.append(value[d3].loc[dates[ii]])
    w4.append(value[d4].loc[dates[ii]])
    w5.append(value[d5].loc[dates[ii]])
    w6.append(value[d6].loc[dates[ii]])
    w7.append(value[d7].loc[dates[ii]])
    w8.append(value[d8].loc[dates[ii]])
    w9.append(value[d9].loc[dates[ii]])
    w10.append(value[d10].loc[dates[ii]])
    w11.append(value[d11].loc[dates[ii]])
    w12.append(value[d12].loc[dates[ii]])
    w13.append(value[d13].loc[dates[ii]])
    w14.append(value[d14].loc[dates[ii]])
    w15.append(value[d15].loc[dates[ii]])    

    
    
    ret_1 =   np.sum(portfolio1_r*portfolio1_v,axis=1)
    ret_2 =   np.sum(portfolio2_r*portfolio2_v,axis=1)
    ret_3 =   np.sum(portfolio3_r*portfolio3_v,axis=1)
    ret_4 =   np.sum(portfolio4_r*portfolio4_v,axis=1)
    ret_5 =   np.sum(portfolio5_r*portfolio5_v,axis=1)
    ret_6 =   np.sum(portfolio6_r*portfolio6_v,axis=1)
    ret_7 =   np.sum(portfolio7_r*portfolio7_v,axis=1)
    ret_8 =   np.sum(portfolio8_r*portfolio8_v,axis=1)
    ret_9 =   np.sum(portfolio9_r*portfolio9_v,axis=1)
    ret_10 = np.sum(portfolio10_r*portfolio10_v,axis=1)   
    ret_11 = np.sum(portfolio11_r*portfolio11_v,axis=1)
    ret_12 = np.sum(portfolio12_r*portfolio12_v,axis=1)
    ret_13 = np.sum(portfolio13_r*portfolio13_v,axis=1)
    ret_14 = np.sum(portfolio14_r*portfolio14_v,axis=1)
    ret_15 = np.sum(portfolio15_r*portfolio15_v,axis=1)    
    
    
    


    res1.extend(list(ret_1.values))
    res2.extend(list(ret_2.values))
    res3.extend(list(ret_3.values))
    res4.extend(list(ret_4.values))
    res5.extend(list(ret_5.values))
    res6.extend(list(ret_6.values))
    res7.extend(list(ret_7.values))
    res8.extend(list(ret_8.values))
    res9.extend(list(ret_9.values))
    res10.extend(list(ret_10.values))


    res11.extend(list(ret_11.values))
    res12.extend(list(ret_12.values))
    res13.extend(list(ret_13.values))    
    res14.extend(list(ret_14.values))
    res15.extend(list(ret_15.values))
 #   resall.append(ret_all)
 #   l=l.append(ret_ff3.iloc[:,:],ignore_index=True)
    resind.extend(list(ret_index.values))
    
    
    print(ii)
    #res5.append(ret_5)
    #res6.append(ret_6)
    #res7.append(ret_7)


res1  = pd.DataFrame(res1)
res2  = pd.DataFrame(res2)
res3  = pd.DataFrame(res3)
res4  = pd.DataFrame(res4)
res5  = pd.DataFrame(res5)
res6  = pd.DataFrame(res6)
res7  = pd.DataFrame(res7)
res8  = pd.DataFrame(res8)
res9  = pd.DataFrame(res9)
res10 = pd.DataFrame(res10)
res11 = pd.DataFrame(res11)
res12 = pd.DataFrame(res12)
res13 = pd.DataFrame(res13)
res14 = pd.DataFrame(res14)
res15 = pd.DataFrame(res15)
#resindex=pd.DataFrame(resind)
#resindex.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\index.csv')
#l.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF5\ff5ext.csv')


a=res1.sum()/(len(dates)-1)
b=res2.sum()/(len(dates)-1)
c=res3.sum()/(len(dates)-1)
d=res4.sum()/(len(dates)-1)
e=res5.sum()/(len(dates)-1)
f=res6.sum()/(len(dates)-1)
g=res7.sum()/(len(dates)-1)
h=res8.sum()/(len(dates)-1)
i=res9.sum()/(len(dates)-1)
j=res10.sum()/(len(dates)-1)

z = resindex.sum()/(len(dates)-1)
longshort=res10-res1
#longshort.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\10portvalext.csv')
[a,b,c,d,e,f,g,h,i,j]



p = pd.DataFrame({'p1':res1.iloc[:,0]})
p['p2'] = res2
p['p3'] = res3
p['p4'] = res4
p['p5'] = res5
p['p6'] = res6
p['p7'] = res7
p['p8'] = res8
p['p9'] = res9
p['p10'] = res10
p['p11'] = res11
p['p12'] = res12
p['p13'] = res13
p['p14'] = res14
p['p15'] = res15
p['spreadport'] = p['p5']-p['p1']

constant_reg = smf.ols(formula=' p1 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())

constant_reg = smf.ols(formula=' p2 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())


constant_reg = smf.ols(formula=' p3 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())


constant_reg = smf.ols(formula=' p4 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())



constant_reg = smf.ols(formula=' p5 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())


constant_reg = smf.ols(formula=' p6 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())


constant_reg = smf.ols(formula=' p7 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())


constant_reg = smf.ols(formula=' p8 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())


constant_reg = smf.ols(formula=' p9 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())


constant_reg = smf.ols(formula=' p10 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())


constant_reg = smf.ols(formula=' p11 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())



constant_reg = smf.ols(formula=' p12 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())


constant_reg = smf.ols(formula=' p13 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())


constant_reg = smf.ols(formula=' p14 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())



constant_reg = smf.ols(formula=' p15 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())


constant_reg = smf.ols(formula=' spreadport ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())


constant_reg = smf.ols(formula=' index ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
print(f.summary())
print(constant_reg.summary())





#p.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\5portallext.csv')

p = pd.read_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\5portallext.csv',index_col=[0])
p['index'] = resindex

del p['spreadport']


del p['p15']

del p['p14']

del p['p13']

del p['p12']

del p['p11']

del p['p10']

del p['p9']

del p['p8']

del p['p7']

del p['p6']


del p['p5']

del p['p1']

del p['p2']

del p['p3']

del p['p4']


ret_mean_an=p.mean()*2
vcov=p.cov()*2

rf=0

# Initial guesses
x0   = np.ones(len(p.var()))
x0  /= x0.sum()

# Run optimization routine, find GMVP
b    = (-1,1)
bnds = (b,)*len(p.var())
con  = {'type': 'eq', 'fun': constraint} 
gmvp = minimize(objective_gmvp,x0,args=(ret_mean_an,vcov,rf),constraints=con,
                bounds=bnds,options={'disp': True})
var_gmvp = np.matmul(np.matmul(gmvp.x,vcov),np.transpose(gmvp.x))
ret_gmvp = np.matmul(gmvp.x,ret_mean_an)
std_gmvp = var_gmvp**0.5
s_p_gmvp = (ret_gmvp-rf)/std_gmvp
print('.'*100)
print('\nGlobal Mean Variance portfolio:\n')
print('Return = ' + str(ret_gmvp) + '\n')
print('Standard deviation = ' +  str(std_gmvp) + '\n')
print('Sharpe ratio = ' + str(s_p_gmvp) + '\n')







