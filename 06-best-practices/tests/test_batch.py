from datetime import datetime
import pandas as pd
import batch

def dt(hour, minute, second = 0):
    return datetime(2023, 1, 1, hour, minute, second)

def test_prepare_data():
    data = [
    (None, None, dt(1, 1), dt(1, 10)),
    (1, 1, dt(1, 2), dt(1, 10)),
    (1, None, dt(1, 2, 0), dt(1, 2, 59)),
    (3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
    ]

    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df = pd.DataFrame(data, columns=columns)
    categorical = ['PULocationID', 'DOLocationID']
    df_out = batch.prepare_data(df, categorical)

    data_expected = [('-1', '-1', '2023-01-01T01:01:00.000000000', '2023-01-01T01:10:00.000000000', 9.),
           ('1', '1', '2023-01-01T01:02:00.000000000', '2023-01-01T01:10:00.000000000', 8.)]
    df_expected = pd.DataFrame(data_expected, columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime'\
                                                     , 'tpep_dropoff_datetime', 'duration'])
    
    assert df_out.compare(df_expected).empty