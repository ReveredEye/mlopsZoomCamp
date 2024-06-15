#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os
import pickle
import pandas as pd


# In[12]:


with open('./starterFiles/model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


# In[13]:


categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


# In[14]:


year = '2023'
month = '03'
df = read_data('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_' + year + '-'+ month + '.parquet')


# In[15]:


dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = model.predict(X_val)


# In[16]:


# Q1) What is the standard deviation of the predicted duration of this dataset?
print(f'The standard deviation of the predicated duration in this dataset is {y_pred.std()}.')


# In[19]:


df['ride_id'] = f'{int(year):04d}/{int(month):02d}_' + df.index.astype('str')


# In[23]:


output_file = f'./dataFrames/df_result_{year}_{month}.parquet'
df_result = pd.DataFrame({'ride_id' : df['ride_id'], 'predicted_duration' : y_pred})
df_result.to_parquet(
    output_file,
    engine='pyarrow',
    compression=None,
    index=False
)


# ##### Q2) What is the size of the above output file?
# Running the command `du df_result_2023_03.parquet`, in windows you can use `dir`, leaves `67 036` (or `66M` if you did 
# `du -h df_result_2023_03.parquet` instead).
# 
