# =========================== IMPORTANT ============================
# Get ready to change the variables in get_output_path(_, _) at the bottom before running this

import os
import pandas as pd
data_expected = [('-1', '-1', '2023-01-01T01:01:00.000000000', '2023-01-01T01:10:00.000000000', 9.),
           ('1', '1', '2023-01-01T01:02:00.000000000', '2023-01-01T01:10:00.000000000', 8.)]
df_expected = pd.DataFrame(data_expected, columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime'\
                                                    , 'tpep_dropoff_datetime', 'duration'])

# options = {
#     'client_kwargs': {
#         'endpoint_url': os.getenv('S3_ENDPOINT_URL')
#     }
# }
# def get_output_path(year, month):
#     default_output_pattern = 's3://nyc-duration-prediction-alexey/taxi_type=fhv/year={year:04d}/month={month:02d}/predictions.parquet'
#     output_pattern = os.getenv('OUTPUT_FILE_PATTERN', default_output_pattern)
#     return output_pattern.format(year=year, month=month)

# df_expected.to_parquet(
#     get_output_path(2023, 3),
#     engine='pyarrow',
#     compression=None,
#     index=False,
#     storage_options=options
# )

df_expected.to_parquet('./output_test/q3df.parquet', compression = None, index = False)