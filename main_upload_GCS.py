from google.cloud import storage
from google.oauth2 import service_account
#from collections import Mapping 
from collections.abc import Mapping
from dir_parameter import parameter

from upload_to_GCS import * 

# GLOBAL:
servicer_account_file=parameter.servicer_account_file
bucket_name=parameter.bucket_name

# UPLOAD FILE MOVIE_META:
source_file_name = parameter.source_file_name_movie
destination_blob_name=parameter.destination_blob_name_movie

upload_blob(servicer_account_file,bucket_name, source_file_name, destination_blob_name)

"""# UPLOAD FILE RATING:

source_file_name=parameter.source_file_name_rating
destination_blob_name=parameter.destination_blob_name_rating
upload_blob(servicer_account_file,bucket_name, source_file_name, destination_blob_name)

# UPLOAD FILE CPI.CSV
source_file_name=parameter.source_file_name_cpi
destination_blob_name=parameter.destination_blob_name_cpi
upload_blob(servicer_account_file,bucket_name, source_file_name, destination_blob_name)
"""

