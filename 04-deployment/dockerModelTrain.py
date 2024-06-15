#!/usr/bin/env python
# coding: utf-8

"""
Use the script through `python yearMonthTrainScript.py <model-name> <year> <month>`
where `<model-name>` is the name of the model from the supplied `app` directory
and `<year>` is in the format `yyyy`
and `<month>` is in the format 'mm'
for example `python yearMonthTrainScript.py model2 2023 04`
"""

# In[11]:
import os, sys
import pickle
import pandas as pd

model_name = sys.argv[1]
year = sys.argv[2]
month = sys.argv[3]


# In[12]:
with open(f'./{model_name}.bin', 'rb') as f_in:
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
df = read_data('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_' + year + '-'+ month + '.parquet')


# In[15]:


dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = model.predict(X_val)


# In[16]:


# Q1) What is the standard deviation of the predicted duration of this dataset?
print(f'The standard deviation of the predicated duration in this dataset is {y_pred.std()}.')

# Q5) What is the mean predicted duration?
print(f'The mean predicted duration is {y_pred.mean()}.')

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
