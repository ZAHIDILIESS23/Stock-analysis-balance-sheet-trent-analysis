#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import json
bs=requests.get('https://financialmodelingprep.com/api/v3/balance-sheet-statement/AAPL?limit=120&apikey=5440fa1b83055823728a35b8988f31eb').json()
bs=pd.DataFrame.from_dict(bs)
bs=bs.T
bs.columns=bs.iloc[0]
bs=bs.iloc[8:25,]
cols=bs.columns
bs[cols]=bs[cols].apply(pd.to_numeric,errors='coerce')## conver our data to numeric
## the pecentage from total asset
asseta1=bs.iloc[16,0]
asseta2=bs.iloc[16,1]
asseta3=bs.iloc[16,2]
asseta4=bs.iloc[16,3]
asseta5=bs.iloc[16,4]
allassets=[asseta1,asseta2,asseta3,asseta4,asseta5]
## divide by total assets
bs[cols]=(bs[cols]/allassets)*100
pd.options.display.float_format='{:.2f}%'.format


# In[2]:


bs


# In[ ]:




