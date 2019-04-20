# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS times"

# CREATE TABLES
# The precision is the total number of digits, while the scale is the number of digits in the fraction part.
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS 
songplays
(
    songplay_id SERIAL PRIMARY KEY, 
    -- start_time TIMESTAMP,
    start_time TIMESTAMP REFERENCES times(start_time), 
    user_id INT REFERENCES users(user_id), 
    level VARCHAR, 
    song_id VARCHAR REFERENCES songs(song_id), 
    artist_id VARCHAR REFERENCES artists(artist_id), 
    session_id INT, 
    location VARCHAR, 
    user_agent VARCHAR
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS 
users
(
    user_id INT PRIMARY KEY, 
    first_name VARCHAR, 
    last_name VARCHAR, 
    gender VARCHAR, 
    level VARCHAR
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS
songs
(
    song_id VARCHAR PRIMARY KEY, 
    title VARCHAR, 
    artist_id VARCHAR, 
    year INT, 
    duration NUMERIC(9,5)
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS
artists
(
    artist_id VARCHAR PRIMARY KEY, 
    name VARCHAR, 
    location VARCHAR, 
    latitude NUMERIC(9,5), 
    longitude NUMERIC(9,5)
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS 
times
(
    start_time TIMESTAMP PRIMARY KEY, 
    -- start_time TIMESTAMP,
    hour INT NOT NULL, 
    day INT NOT NULL, 
    week VARCHAR NOT NULL, 
    month VARCHAR NOT NULL, 
    year INT NOT NULL, 
    weekday VARCHAR NOT NULL
)
""")

# GRANT PRIVILEGES (did manually through psql)
grant_privilege = ("""
GRANT ALL PRIVILEGES ON DATABASE sparkifydb to student;
""")

# INSERT RECORDS
# Note: psycopg2 will sanitize query under cur.execute(query, (input,))
songplay_table_insert = ("""
INSERT INTO 
songplays 
(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
INSERT INTO
users
(user_id, first_name, last_name, gender, level)
VALUES
(%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

song_table_insert = ("""
INSERT INTO
songs
(song_id, title, artist_id, year, duration)
VALUES
(%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO 
artists
(artist_id, name, location, latitude, longitude)
VALUES
(%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")


time_table_insert = ("""
INSERT INTO 
times
(start_time, hour, day, week, month, year, weekday)
VALUES
(%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

# FIND SONGS
# TODO: check duration decimal places, since match may not be exact
# song_select = ("""
# SELECT 
#     songs.song_id, artists.artist_id
# FROM 
#     songs, artists
# WHERE (
#     songs.title=%s
#     AND artists.name=%s
#     AND songs.duration=%s
# )
# """)

song_select = ("""
SELECT 
    songs.song_id, artists.artist_id 
FROM 
    songs 
JOIN 
    artists 
    ON songs.artist_id=artists.artist_id
WHERE (songs.title=%s AND artists.name=%s AND songs.duration=%s)
""")

# QUERY LISTS

create_table_queries = [
    user_table_create, 
    song_table_create, 
    artist_table_create, 
    time_table_create,
    songplay_table_create, 
]
drop_table_queries = [
    songplay_table_drop, 
    user_table_drop, 
    song_table_drop, 
    artist_table_drop, 
    time_table_drop
]

insert_row_queries = [
    song_table_insert,
    artist_table_insert,
    time_table_insert,
    songplay_table_insert
]