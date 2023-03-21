import os
import pandas as pd
import datetime
from google.cloud import storage
from google.cloud import bigquery
from google.oauth2 import service_account
from dir_parameter import parameter,sql_create_table

servicer_account_file=parameter.servicer_account_file
bucket_name=parameter.bucket_name

def connect_gcs(servicer_account_file,bucket_name):
    credentials=service_account.Credentials.from_service_account_file(servicer_account_file)

    storage_client=storage.Client(credentials=credentials)
    bucket=storage_client.bucket(bucket_name)

    return storage_client,bucket,credentials


storage_client,bucket,credentials=connect_gcs(servicer_account_file,bucket_name)
client=bigquery.Client(credentials=credentials)