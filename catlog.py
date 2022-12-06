import requests
import pandas as pd
import numpy as np

def get_cat(year,season):
    url='https://mops.twse.com.tw/mops/web/ajax_t78sb04'
    parameter={'encodeURIComponent': '1',
'TYPEK': 'all',
'step': '1',
'run': 'Y',
'firstin': 'true',
'FUNTYPE': '02',
'year': year,
'season': season,
'fund_no': '0'}
    res=requests.post(url,data=parameter)
    #res.encoding='utf8'
    df=pd.read_html(res.text)[1]#,attrs={'class':'hasBorder'}) #first table
    return df


def p_to_float(x,data):
    l=[]
    for d in data[x]:
        l.append(float(d.split('%')[0]))
    data[x]=l


def get_hist(year,season):
    data=get_cat(year,season)
    data=data.iloc[:-4]
    p_to_float('持股比率',data)
    p_to_float('持股比率.1',data)
    cash={'股票種類':['--'],'股票代號':['--'],
       '股票名稱':['現金'],'持股比率':[100-sum(data['持股比率'])],
       '產業類別':['現金'],'持股比率.1':[100-sum(data['持股比率'])]}
    cash=pd.DataFrame(data=cash,index=[1])
    data=data.append(cash,ignore_index=True)
    print(data)
    return data

###main execution part####
his=get_hist('111','03') # get_hist(year in your favor,season in your favor), note that the input should be strings
his['year']=int(111+1911)*np.ones(his.shape[0]).astype(int)
pd.to_datetime(his.year,format='%Y')
for i in range(110,96,-1): # the range of year
    data=get_hist(str(i),'03') # you can change '03' into whatever season you want
    data['year']=int(i+1911)*np.ones(data.shape[0]).astype(int)
    pd.to_datetime(data.year,format='%Y')
    his=his.append(data,ignore_index=True)
    print(his)

his.to_excel('0050_Q3catlog'+'.xlsx')
