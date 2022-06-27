#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 
import numpy as np
import plotly.graph_objects as go


# In[5]:


data= pd.read_csv('S://DS-22//New Projects//ADBE.csv')


# In[6]:


print(data.head())


# In[7]:


figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                        open=data["Open"], high=data["High"],
                                        low=data["Low"], close=data["Close"])])
figure.update_layout(title = "Tata Motors Stock Price Analysis", xaxis_rangeslider_visible=False)
figure.show()


# In[8]:


print(data.corr())


# In[1]:


from autots import AutoTS


# In[8]:


model=AutoTS(forecast_length=5,frequency='infer',ensemble='simple')
model=model.fit('data',date_col='Date',value_col='Close',id_col='None')
Prediction=model.predict()
forecast=prediction.forecas
print(forecast)

