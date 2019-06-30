# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 15:43:45 2019

@author: Tobias
"""

import statsmodels.formula.api as smf 

data3 = pd.read_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\F-F_Research_Data_Factors_daily.csv',index_col='Date')
data5 = pd.read_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF5\F-F_Research_Data_5_Factors_2x3_daily.csv',index_col='Date') 

dates=data5.index
dates=[str(d)[0:4]+'-'+str(d)[4:6]+'-'+str(d)[6:8] for d in dates]
data5.index=dates

# Run through sorting
newsdata = pd.read_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\10portvalext.csv',index_col=[0])
ff3      = pd.read_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\ff3.csv',index_col=[0])
ff3      = pd.read_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF5\ff5ext.csv',index_col=[0])
dataset = pd.DataFrame({'fomc_e':newsdata['spreadport']-ff3['RF']})
dataset['marketexcess']   = ff3.iloc[:,0]
dataset['SMB'] = ff3.iloc[:,1]
dataset['HML'] = ff3.iloc[:,2]
dataset['RMW'] = ff3.iloc[:,3]
dataset['CMA'] = ff3.iloc[:,4]



FamaFrench3_model = smf.ols(formula='fomc_e ~ marketexcess+ SMB + HML', data=dataset).fit()
FamaFrench3_model.summary()
f=FamaFrench3_model.get_robustcov_results(cov_type='HAC',maxlags=3)
f.summary()

index = pd.read_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\index.csv',index_col=[0])
allport   = pd.read_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\5portall.csv',index_col=[0])
allport_e = pd.DataFrame({'p1':allport['p1']-ff3['RF'],
                                  'p2':allport['p2']-ff3['RF'],
                                  'p3':allport['p3']-ff3['RF'],
                                  'p4':allport['p4']-ff3['RF'],
                                  'p5':allport['p5']-ff3['RF'],
                                  'p6':allport['p6']-ff3['RF'],
                                  'p7':allport['p7']-ff3['RF'],
                                  'p8':allport['p8']-ff3['RF'],
                                  'p9':allport['p9']-ff3['RF'],
                                  'p10':allport['p10']-ff3['RF']})

allport_e['marketexcess']   = ff3.iloc[:,0]
allport_e['SMB'] = ff3.iloc[:,1]
allport_e['HML'] = ff3.iloc[:,2]
allport_e['RMW'] = ff3.iloc[:,3]
allport_e['CMA'] = ff3.iloc[:,4]


FamaFrench3_model = smf.ols(formula='p1~ marketexcess+ SMB + HML + RMW + CMA', data=allport_e).fit()
print(FamaFrench3_model.get_robustcov_results(cov_type='HAC',maxlags=6).summary())
FamaFrench3_model = smf.ols(formula='p2 ~ marketexcess+ SMB + HML + RMW + CMA', data=allport_e).fit()
print(FamaFrench3_model.get_robustcov_results(cov_type='HAC',maxlags=6).summary())
FamaFrench3_model = smf.ols(formula='p3 ~ marketexcess+ SMB + HML + RMW + CMA', data=allport_e).fit()
print(FamaFrench3_model.get_robustcov_results(cov_type='HAC',maxlags=6).summary())
FamaFrench3_model = smf.ols(formula='p4 ~ marketexcess+ SMB + HML + RMW + CMA', data=allport_e).fit()
print(FamaFrench3_model.get_robustcov_results(cov_type='HAC',maxlags=6).summary())
FamaFrench3_model = smf.ols(formula='p5 ~ marketexcess+ SMB + HML + RMW + CMA', data=allport_e).fit()
print(FamaFrench3_model.get_robustcov_results(cov_type='HAC',maxlags=6).summary())
FamaFrench3_model = smf.ols(formula='p6 ~ marketexcess+ SMB + HML + RMW + CMA', data=allport_e).fit()
print(FamaFrench3_model.get_robustcov_results(cov_type='HAC',maxlags=6).summary())
FamaFrench3_model = smf.ols(formula='p7 ~ marketexcess+ SMB + HML + RMW + CMA', data=allport_e).fit()
print(FamaFrench3_model.get_robustcov_results(cov_type='HAC',maxlags=6).summary())
FamaFrench3_model = smf.ols(formula='p8 ~ marketexcess+ SMB + HML + RMW + CMA', data=allport_e).fit()
print(FamaFrench3_model.get_robustcov_results(cov_type='HAC',maxlags=6).summary())
FamaFrench3_model = smf.ols(formula='p9 ~ marketexcess+ SMB + HML + RMW + CMA', data=allport_e).fit()
print(FamaFrench3_model.get_robustcov_results(cov_type='HAC',maxlags=6).summary())
FamaFrench3_model = smf.ols(formula='p10 ~ marketexcess+ SMB + HML + RMW + CMA', data=allport_e).fit()
print(FamaFrench3_model.get_robustcov_results(cov_type='HAC',maxlags=6).summary())


allport = pd.read_csv(r'C:\Users\Tobias\Dropbox\Master\U.S. Data\FF3\10portallext.csv',index_col=[0])
allport_e = pd.DataFrame({'p1':allport['p1']-ff3['RF'],
                                  'p2':allport['p2']-ff3['RF'],
                                  'p3':allport['p3']-ff3['RF'],
                                  'p4':allport['p4']-ff3['RF'],
                                  'p5':allport['p5']-ff3['RF']})

allport_e['marketexcess']   = ff3.iloc[:,0]
allport_e['SMB'] = ff3.iloc[:,1]
allport_e['HML'] = ff3.iloc[:,2]
allport_e['RMW'] = ff3.iloc[:,3]
allport_e['CMA'] = ff3.iloc[:,4]


FamaFrench3_model = smf.ols(formula='p1~ marketexcess+ SMB + HML + RMW + CMA', data=allport_e).fit()
print(FamaFrench3_model.summary())
print(FamaFrench3_model.get_robustcov_results(cov_type='HAC',maxlags=6).summary())
FamaFrench3_model = smf.ols(formula='p2 ~ marketexcess+ SMB + HML + RMW + CMA', data=allport_e).fit()
print(FamaFrench3_model.summary())
print(FamaFrench3_model.get_robustcov_results(cov_type='HAC',maxlags=6).summary())
FamaFrench3_model = smf.ols(formula='p3 ~ marketexcess+ SMB + HML + RMW + CMA', data=allport_e).fit()
print(FamaFrench3_model.summary())
print(FamaFrench3_model.get_robustcov_results(cov_type='HAC',maxlags=6).summary())
FamaFrench3_model = smf.ols(formula='p4 ~ marketexcess+ SMB + HML + RMW + CMA', data=allport_e).fit()
print(FamaFrench3_model.summary())
print(FamaFrench3_model.get_robustcov_results(cov_type='HAC',maxlags=6).summary())
FamaFrench3_model = smf.ols(formula='p5 ~ marketexcess+ SMB + HML + RMW + CMA', data=allport_e).fit()
print(FamaFrench3_model.summary())
print(FamaFrench3_model.get_robustcov_results(cov_type='HAC',maxlags=6).summary())



















