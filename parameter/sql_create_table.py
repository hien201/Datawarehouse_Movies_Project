"""
- include schema to create table on BQ
"""

from google.cloud import bigquery

# PROJECT_ID :
project_id='project-1-373608'

# tạo bảng stage_movie:
stage_movie_id='project-1-373608.movies.stage_movie'
stage_movie_schema= [
        bigquery.SchemaField("movie_id", "INT64", mode="REQUIRED"),
        bigquery.SchemaField("is_adult", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("budget", "NUMERIC", mode="REQUIRED"),
        bigquery.SchemaField("genres", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("original_language", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("title", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("popularity", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("release_date", "DATE", mode="REQUIRED"),
        bigquery.SchemaField("revenue", "NUMERIC", mode="REQUIRED"),
        bigquery.SchemaField("vote_count", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("vote_average", "FLOAT64", mode="REQUIRED"),
        ]

# create table movie:
movie_id='project-1-373608.movies.movie'
movie_schema= [
        bigquery.SchemaField("movie_id", "INT64", mode="REQUIRED"),
        bigquery.SchemaField("is_adult", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("budget", "NUMERIC", mode="REQUIRED"),
        bigquery.SchemaField("genres", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("original_language", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("title", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("popularity", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("release_date", "DATE", mode="REQUIRED"),
        bigquery.SchemaField("revenue", "NUMERIC", mode="REQUIRED"),
        bigquery.SchemaField("vote_count", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("vote_average", "FLOAT64", mode="REQUIRED"),
        ]

# tạo bảng stage_rating:
project_id='project-1-373608'
stage_rating_id='project-1-373608.movies.stage_rating'
stage_rating_schema= [
        bigquery.SchemaField("user_id", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("movie_id", "INT64", mode="NULLABLE"), 
        bigquery.SchemaField("rating", "BIGNUMERIC", mode="NULLABLE"),
        ]

# create rating:
rating_id='project-1-373608.movies.rating'
rating_schema= [
        bigquery.SchemaField("user_id", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("movie_id", "INT64", mode="NULLABLE"), 
        bigquery.SchemaField("rating", "BIGNUMERIC", mode="NULLABLE"),
        ]
    
# tạo bảng stage_movie_genre
stage_movie_genre_id='project-1-373608.movies.stage_movie_genre'
stage_movie_genre_schema= [
        bigquery.SchemaField("movie_id", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("genre_id", "INT64", mode="NULLABLE"), 
        bigquery.SchemaField("genres_name", "STRING", mode="NULLABLE"),
        ]
# create table movie_genre 
movie_genre_id='project-1-373608.movies.movie_genre'
movie_genre_schema= [
        bigquery.SchemaField("movie_id", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("genre_id", "STRING", mode="NULLABLE"), 
        bigquery.SchemaField("genre_name", "STRING", mode="NULLABLE"),
        ]

#create table stage_genre 

stage_genre_id='project-1-373608.movies.stage_genre'
stage_genre_schema= [
        bigquery.SchemaField("genre_id", "INT64", mode="NULLABLE"), 
        bigquery.SchemaField("genres_name", "STRING", mode="NULLABLE"),
        ]


# create tbale genres
genres_id='project-1-373608.movies.genres'
genres_schema= [
        bigquery.SchemaField("genre_id", "STRING", mode="NULLABLE"), 
        bigquery.SchemaField("genre_name", "STRING", mode="NULLABLE"),
        ]

#create table stage_date 

stage_date_id='project-1-373608.movies.stage_date'
stage_date_schema= [
        bigquery.SchemaField("release_date", "DATE", mode="NULLABLE"), 
        bigquery.SchemaField("day", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("week", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("month", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("quarter", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("year", "INT64", mode="NULLABLE"),
        ]

#create date
date_id='project-1-373608.movies.date'
date_schema= [
        bigquery.SchemaField("release_date", "DATE", mode="NULLABLE"), 
        bigquery.SchemaField("day", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("week", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("month", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("quarter", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("year", "INT64", mode="NULLABLE"),
        ]

#create stage_cpi 
stage_cpi_id='project-1-373608.movies.stage_cpi'
stage_cpi_schema= [
        bigquery.SchemaField("date_cd", "DATE", mode="NULLABLE"), 
        bigquery.SchemaField("consumer_price_index", "FLOAT", mode="NULLABLE"),
        ]

#creta cpi :
cpi_id='project-1-373608.movies.cpi'
cpi_schema= [
        bigquery.SchemaField("date_cd", "DATE", mode="NULLABLE"), 
        bigquery.SchemaField("consumer_price_index", "FLOAT", mode="NULLABLE"),
        ]

############## LIST TABLE TO CREATE##########
list_table_id=[stage_movie_id,stage_rating_id,stage_movie_genre_id,stage_genre_id,stage_date_id,stage_cpi_id,movie_id,rating_id,movie_genre_id,genres_id,date_id,cpi_id]
list_schema=[stage_movie_schema,stage_rating_schema,stage_movie_genre_schema,stage_genre_schema,stage_date_schema,stage_cpi_schema,movie_schema,rating_schema,movie_genre_schema,genres_schema,date_schema,cpi_schema]

list_create_table=zip(list_table_id,list_schema)

"""bigquery.SchemaField("user_id ", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("movie_id ", "INT64", mode="NULLABLE"), REQUIRED
        bigquery.SchemaField("rating ", "BIGNUMERIC", mode="NULLABLE"),
    ]"""

''''

        bigquery.SchemaField("budget ", "INTERVAL", mode="REQUIRED"),
        bigquery.SchemaField("genres ", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("original_language ", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("title ", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("popularity  ", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("release_date ", "DATE", mode="REQUIRED"),
        bigquery.SchemaField("revenue ", "INTERVAL", mode="REQUIRED"),
        bigquery.SchemaField("vote_count ", "INT64", mode="REQUIRED"),
        bigquery.SchemaField("vote_average ", "FLOAT64", mode="REQUIRED"), '''