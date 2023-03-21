
# ACCOUNT & PROJECT INFO:
servicer_account_file="D:\DE\A_PROJECT_LIST/2_ETL_POSTGRES_TO_BIGQUERY\hien1.json"
bucket_name='movies_project_hien'
project_id='project-1-373608'

# meta_movie:
source_file_name_movie='D:\DE\A_PROJECT_LIST/3_DW_Movies\dir_csv_file\movie_meta.csv'
destination_blob_name_movie='movie_meta.csv'
file_name_movie='movie_meta'
uri_movie='gs://movies_project_hien/movie_meta.csv'

# rating: 

source_file_name_rating='D:\DE\A_PROJECT_LIST/3_DW_Movies\dir_csv_file/rating.csv'
destination_blob_name_rating='rating.csv'
file_name_rating='rating'
uri_rating='gs://movies_project_hien/rating.csv'


# cpi:
source_file_name_cpi='D:\DE\A_PROJECT_LIST/3_DW_Movies\dir_csv_file\cpi.csv'
destination_blob_name_cpi='cpi.csv'
file_name_cpi='cpi'
uri_cpi='gs://movies_project_hien/cpi.csv'