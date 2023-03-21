from connect_BQ import *


# UPSERT TABLE MOVIE:
pro_upsert_movie= ("""
CREATE OR REPLACE PROCEDURE `project-1-373608.movies.movie`()
OPTIONS (strict_mode=false)
BEGIN 
MERGE movies.movie m
USING (select* from movies.stage_movie) sm
ON m.movie_id=sm.movie_id  

WHEN MATCHED THEN
UPDATE SET movie_id=sm.movie_id, is_adult=sm.is_adult, budget=sm.budget, genres=sm.genres, original_language=sm.original_language, title=sm.title, popularity=sm.popularity, 
release_date=sm.release_date,revenue=sm.revenue,vote_count=sm.vote_count,vote_average=sm.vote_average

WHEN NOT MATCHED THEN
INSERT ( movie_id, is_adult, budget, genres, original_language, title, popularity, release_date, revenue, vote_count, vote_average) 
VALUES(sm.movie_id, sm.is_adult, sm.budget, sm.genres, sm.original_language, sm.title, sm.popularity, sm.release_date, sm.revenue, sm.vote_count, sm.vote_average)
;
select * from movies.movie;



END;""")

upsert_movie=(""" call `project-1-373608.movies.movie`()""")

# UPSERT TABLE movie_genre:
pro_upsert_movie_genre= ("""
CREATE OR REPLACE PROCEDURE `project-1-373608.movies.movie_genre`()
OPTIONS(strict_mode=FALSE)
BEGIN 
MERGE `movies.movie_genre` mg
USING (select movie_id,json_extract_scalar(h,'$.id') as genre_id,json_extract_scalar(h,'$.name') as genre_name from movies.stage_movie left join unnest(json_extract_array(genres)) as h) mm
ON mm.movie_id=mg.movie_id and mm.

WHEN MATCHED THEN
UPDATE SET movie_id = mm.movie_id, genre_id = mm.genre_id, genre_name = mm.genre_name

WHEN NOT MATCHED THEN
INSERT (movie_id,genre_id,genre_name) VALUES(mm.movie_id,mm.genre_id,mm.genre_name)
;

END;
""")
upsert_movie_genre=("""call  `project-1-373608.movies.movie_genre`()""")

# upsert trable genres
pro_upsert_genres=("""
CREATE OR REPLACE PROCEDURE `project-1-373608.movies.genre`()
OPTIONS(strict_mode=FALSE)
BEGIN 
MERGE `movies.genres` g
USING `movies.movie_genre` mg
ON g.genre_id=mg.genre_id

WHEN NOT MATCHED THEN
INSERT (genre_id,genre_name) VALUES(mg.genre_id,mg.genre_name);

END;
""")
upsert_genres=(""" call `project-1-373608.movies.genre`()""")

# UPSERT TABLE RATING:

pro_upsert_rating=("""
CREATE OR REPLACE PROCEDURE `project-1-373608.movies.rating`()
OPTIONS(strict_mode=FALSE)
BEGIN 
MERGE `movies.rating` r
USING `movies.stage_rating` sr
ON r.user_id=sr.user_id and r.movie_id=sr.movie_id

WHEN MATCHED THEN 
UPDATE SET rating=sr.rating 

WHEN NOT MATCHED THEN
INSERT (user_id,movie_id,rating) VALUES(sr.user_id,sr.movie_id, sr.rating);

END;           
            """)

upsert_rating=("""call `project-1-373608.movies.rating`()""")

# UPSERT TABLE DATE:

pro_upsert_date=("""
CREATE OR REPLACE PROCEDURE `project-1-373608.movies.date`()
BEGIN

MERGE movies.date d
USING
  (select
  release_date, 
  EXTRACT(DAY FROM release_date) as day,
  EXTRACT(WEEK FROM release_date) as week,
  EXTRACT(MONTH FROM release_date) as month,
  EXTRACT(QUARTER FROM release_date) as quarter,
  EXTRACT(YEAR FROM release_date) as year
  from `movies.movie`) gd
ON d.release_date=gd.release_date

WHEN NOT MATCHED THEN
INSERT (release_date,day, week, month, quarter, year) VALUES(gd.release_date,gd.day, gd.week, gd.month, gd.quarter, gd.year);



END;

""")
upsert_date=("""call `project-1-373608.movies.date`()""")

# upsert table cpi

pro_upsert_cpi=("""
CREATE OR REPLACE PROCEDURE `project-1-373608.movies.cpi`()
BEGIN 
MERGE `movies.cpi` c
USING `movies.stage_cpi` sc
ON c.date_cd=sc.date_cd
WHEN MATCHED THEN
UPDATE SET date_cd=sc.date_cd, consumer_price_index=sc.consumer_price_index

WHEN NOT MATCHED THEN 
INSERT (date_cd,consumer_price_index) VALUES(sc.date_cd,sc.consumer_price_index);
TRUNCATE TABLE `project-1-373608.movies.stage_cpi`;
END;
""")
upsert_cpi=("""call `project-1-373608.movies.cpi`()""")


# PROCEDURE_LIST:
procedure_list= [pro_upsert_movie,pro_upsert_rating,pro_upsert_cpi,pro_upsert_movie_genre,pro_upsert_genres,pro_upsert_date]
upsert_list=[upsert_movie,upsert_rating,upsert_cpi,upsert_movie_genre,upsert_genres,upsert_date]

for i in zip(procedure_list,upsert_list):
    client.query(i[0])
    client.query(i[1])
    #print(i[0])
    


"""WHEN MATCHED THEN 
UPDATE SET release_date=gd.release_date, day=gd.day, week=gd.week, month=gd.month, quarter=gd.quarter, year=gd.year;"""