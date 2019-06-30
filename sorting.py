# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 17:19:51 2019

@author: Tobias
"""
import statsmodels.sandbox.distributions.extras as gh
def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


os.chdir('C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Returns')
with open('sp500prices.pickle', 'rb') as file:
       prices=pickle.load(file)
       
os.chdir('C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Returns')
indX=pd.read_csv('C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Returns\\sp500returns.csv')
              


os.chdir('C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Similarity\\NewsSim\\40')
os.chdir('C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Similarity\\40')

with open('ranking.pickle', 'rb') as file:
    tickers = pickle.load(file)
    
os.chdir('C:\\Users\\Tobias\\Dropbox\\Master\\TempFolder')
with open('ranking25news.pickle','rb') as file:
     tickers = pickle.load(file)
        


res1   = []
res2   = []
res3   = []
res4   = []
res5   = []
res6   = []
res7   = []
res8   = []
res9   = []
res10  = []
res11   = []
res12   = []
res13   = []
res14   = []
res15  = []
resind = []
resall = []
resff3= []

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
val       = None

for ii in range(len(dates)-1):
    data     = tickers.iloc[ii,:]
    data     = data.dropna()
    data     = data.sort_values(axis=0)
    uniques  = data.unique()
    
    lucky_ten = list(split(uniques,15))
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
    
    
    portfolio1_r =    np.sum(np.log(prices[d1].loc[dates[ii]:dates[ii+1]]+1))
    portfolio2_r =    np.sum(np.log(prices[d2].loc[dates[ii]:dates[ii+1]]+1))
    portfolio3_r =    np.sum(np.log(prices[d3].loc[dates[ii]:dates[ii+1]]+1))
    portfolio4_r =    np.sum(np.log(prices[d4].loc[dates[ii]:dates[ii+1]]+1))
    portfolio5_r =    np.sum(np.log(prices[d5].loc[dates[ii]:dates[ii+1]]+1))
    portfolio6_r =    np.sum(np.log(prices[d6].loc[dates[ii]:dates[ii+1]]+1))
    portfolio7_r =    np.sum(np.log(prices[d7].loc[dates[ii]:dates[ii+1]]+1))
    portfolio8_r =    np.sum(np.log(prices[d8].loc[dates[ii]:dates[ii+1]]+1))
    portfolio9_r =    np.sum(np.log(prices[d9].loc[dates[ii]:dates[ii+1]]+1))
    portfolio10_r=    np.sum(np.log(prices[d10].loc[dates[ii]:dates[ii+1]]+1))
    
    portfolio11_r =    np.sum(np.log(prices[d11].loc[dates[ii]:dates[ii+1]]+1))
    portfolio12_r =    np.sum(np.log(prices[d12].loc[dates[ii]:dates[ii+1]]+1))
    portfolio13_r =    np.sum(np.log(prices[d13].loc[dates[ii]:dates[ii+1]]+1))
    portfolio14_r =    np.sum(np.log(prices[d14].loc[dates[ii]:dates[ii+1]]+1))
    portfolio15_r =    np.sum(np.log(prices[d15].loc[dates[ii]:dates[ii+1]]+1))
    
    
    
    
    
    ret_ind      =    np.sum(np.log(indX.loc[dates[ii]:dates[ii+1]]+1))
    ret_all      =    np.sum(np.log(prices.loc[dates[ii]:dates[ii+1]]+1))
#    ret_ff3      =    np.sum(np.log(data3.loc[dates[ii]:dates[ii+1]]/100+1))
    
    
    
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

    

    ret_1 = np.sum(portfolio1_r*portfolio1_v)
    ret_2 = np.sum(portfolio2_r*portfolio2_v)
    ret_3 = np.sum(portfolio3_r*portfolio3_v)
    ret_4 = np.sum(portfolio4_r*portfolio4_v)
    ret_5 = np.sum(portfolio5_r*portfolio5_v)
    ret_6 = np.sum(portfolio6_r*portfolio6_v)
    ret_7 = np.sum(portfolio7_r*portfolio7_v)
    ret_8 = np.sum(portfolio8_r*portfolio8_v)
    ret_9 = np.sum(portfolio9_r*portfolio9_v)
    ret_10 = np.sum(portfolio10_r*portfolio10_v)   
    ret_11 = np.sum(portfolio11_r*portfolio11_v)
    ret_12 = np.sum(portfolio12_r*portfolio12_v)
    ret_13 = np.sum(portfolio13_r*portfolio13_v)
    ret_14 = np.sum(portfolio14_r*portfolio14_v)
    ret_15 = np.sum(portfolio15_r*portfolio15_v)    
    
    
    
    

    
    res1.append(ret_1)
    res2.append(ret_2)
    res3.append(ret_3)
    res4.append(ret_4)
    res5.append(ret_5)
    res6.append(ret_6)
    res7.append(ret_7)
    res8.append(ret_8)
    res9.append(ret_9)
    res10.append(ret_10)
    res11.append(ret_11)
    res12.append(ret_12)
    res13.append(ret_13)    
    res14.append(ret_14)
    res15.append(ret_15)
    resall.append(ret_all)
 #   resff3.append(ret_ff3)
    print(ret_2)
    #res5.append(ret_5)
    #res6.append(ret_6)
    #res7.append(ret_7)
    resind.append(ret_ind)


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

resall = pd.DataFrame(resall)
ff3    = pd.DataFrame(resff3)
ff3.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF5\ff5.csv')

w1 = pd.DataFrame(w1)
w2 = pd.DataFrame(w2)
w3 = pd.DataFrame(w3)
w4 = pd.DataFrame(w4)
w5 = pd.DataFrame(w5)
w6 = pd.DataFrame(w6)
w7 = pd.DataFrame(w7)
w8 = pd.DataFrame(w8)
w9 = pd.DataFrame(w9)
w10= pd.DataFrame(w10)

[np.mean(w1.mean()),
np.mean(w2.mean()),
np.mean(w3.mean()),
np.mean(w4.mean()),
np.mean(w5.mean()),
np.mean(w6.mean()),
np.mean(w7.mean()),
np.mean(w8.mean()),
np.mean(w9.mean()),
np.mean(w10.mean())]

[len(w1.var()),
 len(w2.var()),
 len(w3.var()),
 len(w4.var()),
 len(w5.var()),
 len(w6.var()),
 len(w7.var()),
 len(w8.var()),
 len(w9.var()),
 len(w10.var())]




#res6 = pd.DataFrame(res6)
#res7 = pd.DataFrame(res7)
resind = pd.DataFrame(resind)
res_ben=res10-res1
res_ben=pd.concat( [pd.Series([0]),res_ben] )
res_ben.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\10port.csv')
#resind.to_pickle(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\Returns\ReturnSPTRI.pickle')
res1.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\10port1.csv')
res2.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\10port2.csv')
res3.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\10port3.csv')
res4.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\10port4.csv')
res5.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\10port5.csv')
res6.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\10port6.csv')
res7.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\10port7.csv')
res8.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\10port8.csv')
res9.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\10port9.csv')
res10.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\10port10.csv')

res1['2'] = res2
res1['3'] = res3
res1['4'] = res4
res1['5'] = res5
res1['6'] = res6
res1['7'] = res7
res1['8'] = res8
res1['9'] = res9
res1['10'] = res10
resALLport = res1.rename(index=str, columns={0: 1})
resALLport.to_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\5portall.csv')


###############################################################################

a=res1.mean()
b=res2.mean()
c=res3.mean()
d=res4.mean()
e=res5.mean()
f=res6.mean()
g=res7.mean()
h=res8.mean()
i=res9.mean()
j=res10.mean()


[a,b,c,d,e,f,g,h,i,j]


k=res1.std()
l=res2.std()
m=res3.std()
n=res4.std()
o=res5.std()
p=res6.std()
q=res7.std()
r=res8.std()
s=res9.std()
t=res10.std()


[k,l,m,n,o,p,q,r,s,t]

u=res1.skew()
v=res2.skew()
w=res3.skew()
x=res4.skew()
y=res5.skew()
z=res6.skew()
aa=res7.skew()
bb=res8.skew()
cc=res9.skew()
dd=res10.skew()

[u,v,w,x,y,z,aa,bb,cc,dd]


ee=res1.kurtosis()
ff=res2.kurtosis()
gg=res3.kurtosis()
hh=res4.kurtosis()
ii=res5.kurtosis()
jj=res6.kurtosis()
kk=res7.kurtosis()
ll=res8.kurtosis()
mm=res9.kurtosis()
nn=res10.kurtosis()

[ee,ff,gg,hh,ii,jj,kk,ll,mm,nn]

longshort=res10-res1
longshort.mean()
longshort.std()
longshort.skew()
longshort.kurtosis()
longshort.mean()/longshort.std()




###############################################################################

###############################################################################


res1 = pd.DataFrame(res1)
res2 = pd.DataFrame(res2)
res3 = pd.DataFrame(res3)
res4 = pd.DataFrame(res4)
res5 = pd.DataFrame(res5)


a=res1.mean()
b=res2.mean()
c=res3.mean()
d=res4.mean()
e=res5.mean()




[a,b,c,d,e]


k=res1.std()
l=res2.std()
m=res3.std()
n=res4.std()
o=res5.std()


[k,l,m,n,o]

u=res1.skew()
v=res2.skew()
w=res3.skew()
x=res4.skew()
y=res5.skew()

[u,v,w,x,y]


ee=res1.kurtosis()
ff=res2.kurtosis()
gg=res3.kurtosis()
hh=res4.kurtosis()
ii=res5.kurtosis()


[ee,ff,gg,hh,ii]

longshort=res5-res1
longshort.mean()
longshort.std()
longshort.skew()
longshort.kurtosis()


w1 = pd.DataFrame(w1)
w2 = pd.DataFrame(w2)
w3 = pd.DataFrame(w3)
w4 = pd.DataFrame(w4)
w5 = pd.DataFrame(w5)


[np.mean(w1.mean()),
np.mean(w2.mean()),
np.mean(w3.mean()),
np.mean(w4.mean()),
np.mean(w5.mean())]

[len(w1.var()),
 len(w2.var()),
 len(w3.var()),
 len(w4.var()),
 len(w5.var())]

longshort=res5-res1
longshort.mean()
longshort.std()
longshort.skew()
longshort.kurtosis()
longshort.mean()/longshort.std()



plt.scatter([1,2,3,4,5],[a,b,c,d,e])
plt.xlabel('Portfolio')
plt.ylabel('Return')
plt.title('Value-Weighted Returns')

resind = pd.DataFrame(resind)
resind['ls'] = longshort
print('Sharpe:' +str(longshort.mean()/longshort.std()) + '\n' + 'Corr:' + str(resind.corr()))
###############################################################################

###############################################################################

a=res1.mean()
b=res2.mean()
c=res3.mean()
d=res4.mean()
e=res5.mean()
f=res6.mean()
g=res7.mean()
h=res8.mean()
i=res9.mean()
j=res10.mean()
f1=res11.mean()
g1=res12.mean()
h1=res13.mean()
i1=res14.mean()
j1=res15.mean()

[a,b,c,d,e,f,g,h,i,j,f1,g1,h1,i1,j1]


k=res1.std()
l=res2.std()
m=res3.std()
n=res4.std()
o=res5.std()
p=res6.std()
q=res7.std()
r=res8.std()
s=res9.std()
t=res10.std()
p1=res11.std()
q1=res12.std()
r1=res13.std()
s1=res14.std()
t1=res15.std()


[k,l,m,n,o,p,q,r,s,t,p1,q1,r1,s1,t1]

u=res1.skew()
v=res2.skew()
w=res3.skew()
x=res4.skew()
y=res5.skew()
z=res6.skew()
aa=res7.skew()
bb=res8.skew()
cc=res9.skew()
dd=res10.skew()
z1=res11.skew()
aa1=res12.skew()
bb1=res13.skew()
cc1=res14.skew()
dd1=res15.skew()


[u,v,w,x,y,z,aa,bb,cc,dd,z1,aa1,bb1,cc1,dd1]


ee=res1.kurtosis()
ff=res2.kurtosis()
gg=res3.kurtosis()
hh=res4.kurtosis()
ii=res5.kurtosis()
jj=res6.kurtosis()
kk=res7.kurtosis()
ll=res8.kurtosis()
mm=res9.kurtosis()
nn=res10.kurtosis()
jj1=res11.kurtosis()
kk1=res12.kurtosis()
ll1=res13.kurtosis()
mm1=res14.kurtosis()
nn1=res15.kurtosis()


[ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,jj1,kk1,ll1,mm1,nn1]

longshort=res15-res1
longshort.mean()
longshort.std()
longshort.skew()
longshort.kurtosis()
longshort.mean()/longshort.std()

resind = pd.DataFrame(resind)
resind['ls'] = longshort
print('Sharpe:' +str(longshort.mean()/longshort.std()) + '\n' + 'Corr:' + str(resind.corr()))


w1 = pd.DataFrame(w1)
w2 = pd.DataFrame(w2)
w3 = pd.DataFrame(w3)
w4 = pd.DataFrame(w4)
w5 = pd.DataFrame(w5)
w6 = pd.DataFrame(w6)
w7 = pd.DataFrame(w7)
w8 = pd.DataFrame(w8)
w9 = pd.DataFrame(w9)
w10= pd.DataFrame(w10)
w11 = pd.DataFrame(w11)
w12 = pd.DataFrame(w12)
w13 = pd.DataFrame(w13)
w14 = pd.DataFrame(w14)
w15= pd.DataFrame(w15)


[np.mean(w1.mean()),
np.mean(w2.mean()),
np.mean(w3.mean()),
np.mean(w4.mean()),
np.mean(w5.mean()),
np.mean(w6.mean()),
np.mean(w7.mean()),
np.mean(w8.mean()),
np.mean(w9.mean()),
np.mean(w10.mean()),
np.mean(w11.mean()),
np.mean(w12.mean()),
np.mean(w13.mean()),
np.mean(w14.mean()),
np.mean(w15.mean())]

[len(w1.var()),
 len(w2.var()),
 len(w3.var()),
 len(w4.var()),
 len(w5.var()),
 len(w6.var()),
 len(w7.var()),
 len(w8.var()),
 len(w9.var()),
 len(w10.var()),
 len(w11.var()),
 len(w12.var()),
 len(w13.var()),
 len(w14.var()),
 len(w15.var())]

plt.scatter([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[a,b,c,d,e,f,g,h,i,j,f1,g1,h1,i1,j1])
plt.xlabel('Portfolio')
plt.ylabel('Return')
plt.title('Equal-Weighted Returns')


###############################################################################

resind.mean()
resind.std()
resind.skew()
resind.kurtosis()

plt.subplot(210)

# equivalent but more general
ax1=plt.subplot(2, 2,1)

# add a subplot with no frame
ax2=plt.subplot(222, frameon=False)

# add a polar subplot
plt.subplot(223, projection='polar')

# add a red subplot that shares the x-axis with ax1
plt.subplot(224, sharex=ax1, facecolor='red')

# delete ax2 from the figure
plt.delaxes(ax2)

# add ax2 to the figure again
plt.subplot(ax2)





v=j-a

n=np.linspace(-3,3,10000)
sorting = []
indexob = []
pdf_sort = gh.pdf_mvsk( [res7.mean()[0],res7.std()[0]**2,res7.skew()[0],res7.kurt()[0]-3])
pdf_indx = gh.pdf_mvsk( [resind.mean()[0],resind.std()[0]**2,resind.skew()[0],resind.kurt()[0]-3])
for ii in n:
    sorting.append(pdf_sort(ii))
    indexob.append(pdf_indx(ii))
    
a=res1.std()
b=res2.std()
c=res3.std()
d=res4.std()
e=res5.std()
f=res6.std()
g=res7.std()
h=res8.std()
i=res9.std()
j=res10.std()



plt.scatter([1,2,3,4,5,6,7,8,9,10],[a,b,c,d,e,f,g,h,i,j])
plt.xlabel('Portfolio')
plt.ylabel('Return')
plt.title('Value-Weighted Returns')



res_ben1=pd.concat( [pd.Series([0]),res_ben] )
res_ben2=pd.concat( [pd.Series([0]),res_ben])
res_ind1=pd.concat( [pd.Series([0]),resind] )






with open(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\Returns\ReturnlongshortValueWWithNews.pickle', 'rb') as file:
       ValuWNews = pickle.load(file) 
       ValuWNews.index=range(39)
       
with open(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\Returns\ReturnlongshortEqualWWithNews.pickle', 'rb') as file:
       EqualWNews = pickle.load(file)
       EqualWNews.index=range(39)

with open(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\Returns\ReturnlongshortEqualWWithoutNews.pickle', 'rb') as file:
       EqualW = pickle.load(file)
       EqualW.index=range(39)
   
with open(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\Returns\ReturnlongshortValueWWithoutNews.pickle', 'rb') as file:
       ValueW = pickle.load(file)
       ValueW.index=range(1,39)



pIndex = np.exp(np.cumsum(resind))
p1     = np.exp(np.cumsum(ValuWNews))
p2     = np.exp(np.cumsum(EqualWNews))
ax = plt.subplot(1,1,1)
plot1, = ax.plot(pIndex, label="line 1")
plot2, = ax.plot(p1 , label="line 2")
plot3, = ax.plot(p2, label="line 3")
ax.legend(['S&P 500 Total Return Index','Value-Weighted Portfolios','Equal-Weighted Portfolios'])
plt.ylabel('Return')
plt.title('FOMC With News')
plt.savefig('FOMCWithNews.png')

p3     = np.exp(np.cumsum(EqualW))
p4     = np.exp(np.cumsum(ValueW))
ax = plt.subplot(1,1,1)
plot1, = ax.plot(pIndex, label="line 1")
plot2, = ax.plot(p3 , label="line 2")
plot3, = ax.plot(p4, label="line 3")
ax.legend(['S&P 500 Total Return Index','Value-Weighted Portfolios','Equal-Weighted Portfolios'])
plt.ylabel('Return')
plt.title('FOMC Without News')
plt.savefig('FOMCWithoutNews.png')


ValuWNews=ValuWNews.iloc[1:]
ValuWNews.index=resind.index
EqualWNews=EqualWNews.iloc[1:]
EqualWNews.index=resind.index
ValueW=ValueW.iloc[1:]
ValueW.index=resind.index
EqualW=EqualW.iloc[1:]
EqualW.index=resind.index
resind['ValueWNews'] = ValuWNews
resind['EqualWNews'] = EqualWNews
resind['ValueNNews'] = ValueW
resind['EqualNNews'] = EqualW







res1 = pd.DataFrame(res1)
res2 = pd.DataFrame(res2)
res3 = pd.DataFrame(res3)
res4 = pd.DataFrame(res4)
res5 = pd.DataFrame(res5)
res6 = pd.DataFrame(res6)
res7 = pd.DataFrame(res7)
res8 = pd.DataFrame(res8)
res9 = pd.DataFrame(res9)
res10= pd.DataFrame(res10)

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

p=resind
p['wport']=res_ben

ret_mean_an=p.mean()*2
vcov=p.cov()*2




## Identify mean-variance portfolio through simulation ##
risk_free   = web.get_data_fred('TB3MS',start=end,end=end)/100
### Identify GMVP by constrained optimization ###
rf = risk_free.values[0].tolist()
rf = rf[0]
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
print('.'*100)

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
p['spreadport'] = p['p15']-p['p1']

constant_reg = smf.ols(formula=' p1 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
f.summary()

constant_reg = smf.ols(formula=' p2 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
f.summary()

constant_reg = smf.ols(formula=' p3 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
f.summary()

constant_reg = smf.ols(formula=' p4 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
f.summary()

constant_reg = smf.ols(formula=' p5 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
f.summary()

constant_reg = smf.ols(formula=' p6 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
f.summary()

constant_reg = smf.ols(formula=' p7 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
f.summary()


constant_reg = smf.ols(formula=' p8 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
f.summary()


constant_reg = smf.ols(formula=' p9 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
f.summary()

constant_reg = smf.ols(formula=' p10 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
f.summary()

constant_reg = smf.ols(formula=' p11 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
f.summary()

constant_reg = smf.ols(formula=' p12 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
f.summary()


constant_reg = smf.ols(formula=' p13 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
f.summary()


constant_reg = smf.ols(formula=' p14 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
f.summary()

constant_reg = smf.ols(formula=' p15 ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
f.summary()


constant_reg = smf.ols(formula=' spreadport ~ 1', data=p).fit()
f=constant_reg.get_robustcov_results(cov_type='HAC',maxlags=6)
f.summary()





















