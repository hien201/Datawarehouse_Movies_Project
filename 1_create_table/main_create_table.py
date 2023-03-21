from google.cloud import bigquery
from dir_parameter import * 
from google.oauth2 import service_account
from sql_script import *
from dir_parameter import parameter,sql_create_table
from create_table import * 

servicer_account_file= parameter.servicer_account_file
project_id=parameter.project_id


"""#tạo bảng rating
table_id=sql_create_table.table_staging_rating_id
schema=sql_create_table.schema_staging_rating
create_table(table_id,schema,servicer_account_file,project_id)

# tạo bảng staging_movie:
table_id=sql_create_table.table_staging_movie_id
schema= sql_create_table.schema_staging_movie
create_table(table_id,schema,servicer_account_file,project_id)"""



list_create_table=sql_create_table.list_create_table
for i in list(list_create_table):
    create_table(i[0],i[1],servicer_account_file,project_id)
