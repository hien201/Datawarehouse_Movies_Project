"""
- KẾT NỐI GCS
- CHECK FILE TỒN TẠI TRÊN GCS CHƯA
- XÁC ĐỊNH HÌNH THỨC LOAD (WRITE_TRUNCATE ; WRITE_APPEND...) VÀ TIẾN HÀNH LOAD TỪ FILE CSV Ở GCS VÀO TABLE(BẢNG TẠM HOẶC BẢNG CHÍNH) Ở BIGQUERY


LOAD DỮ LIỆU VÀO 2 BẢNG MOVIE_META VÀ RATING TỪ GCS.
"""
import os
import pandas as pd
import datetime
from google.cloud import storage
from google.cloud import bigquery
from google.oauth2 import service_account
from dir_parameter import *




# function to connect GCS:
def connect_gcs(servicer_account_file,bucket_name):
    credentials=service_account.Credentials.from_service_account_file(servicer_account_file)

    storage_client=storage.Client(credentials=credentials)
    bucket=storage_client.bucket(bucket_name)

    return storage_client,bucket,credentials



def load_to_bigquery(servicer_account_file,bucket_name,uri,table_id,file_name):
    file_csv=f'{file_name}.csv'
    storage_client,bucket,credentials= connect_gcs(servicer_account_file,bucket_name)
    blobs=list(storage_client.list_blobs(bucket,start_offset=file_csv)) 
    print(file_csv)
    for blob in blobs:
        print(blob)

    if blobs:
        print(f'exists {file_csv} on GCS')
        client=bigquery.Client(credentials=credentials)
       
        job_config = bigquery.LoadJobConfig(
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            
        )

        load_job = client.load_table_from_uri(
            uri, table_id, job_config=job_config)
        load_job.result()  # Waits for the job to complete.
        print("ok")
        storage.Bucket.delete_blob(bucket,file_csv)

    else:
        print(f"{file_csv} doesn't exists on GCS")








