import os
from google.cloud import storage
from google.cloud import bigquery
from google.oauth2 import service_account
from dir_parameter import parameter,sql_create_table
from GCS_TO_BIGQUERY import * 

servicer_account_file=parameter.servicer_account_file
bucket_name=parameter.bucket_name


# upload staging_movie_meta:
uri=parameter.uri_movie
table_id=sql_create_table.stage_movie_id
file_name=parameter.file_name_movie
load_to_bigquery(servicer_account_file,bucket_name,uri,table_id,file_name)


"""# upload stage_rating:
uri=parameter.uri_rating
table_id=sql_create_table.stage_rating_id
file_name=parameter.file_name_rating
load_to_bigquery(servicer_account_file,bucket_name,uri,table_id,file_name)

# update stage_cpi:
uri=parameter.uri_cpi
table_id=sql_create_table.stage_cpi_id
file_name=parameter.file_name_cpi
load_to_bigquery(servicer_account_file,bucket_name,uri,table_id,file_name)


"""