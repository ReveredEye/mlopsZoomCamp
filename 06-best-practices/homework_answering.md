##### Q1) Refactoring
The predicted mean duration for march 2023 yellow taxi data is 14.203865642696083.

##### Q2) What should be the other test file?
__init__.py

##### Q3) How many rows in the expected dataframe?
With the data given, it should be 2 rows.

##### Q4) We should adjust commmands for localstack. What option to use for such purposes?
--endpoint-url. I have specified environment variables during this task;
```
export AWS_ACCESS_KEY_ID="test"
export AWS_SECRET_# ACCESS_KEY="test"
export AWS_DEFAULT_REGION="us-ea# st-1"
```

To create s3 buckets; `aws --endpoint-url=http://localhost:4566 s3 mb s3://nyc-duration`
To see s3 buckets; `aws --endpoint-url=http://localhost:4566 s3 ls` or `aws --endpoint-url=http://localhost:4566 s3api list-buckets`

More environs;
```
export INPUT_FILE_PATTERN="s3://nyc-duration/in/{year:04d}-{month:02d}.parquet"
export OUTPUT_FILE_PATTERN="s3://nyc-duration/out/{year:04d}-{month:02d}.parquet"
```