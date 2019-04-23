# Sparkify
The dataset contains song json files and log json files. The song files are a subset of the [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/), paritioned by the first 3 letters of each song's track id. The log dataset is generated from an event simulator [eventsim](https://github.com/Interana/eventsim) based on the songs above. Eventsim is a tool written in scala to generate event data for testing and demos.

## Usage: 
* Run create tables.py, then etl.py. To test, you may use test.ipynb or your own database management tool (for example, adminer). To clean up, use drop_tables.py

## Files:
* create_tables.py to initialize postgres tables, replacing any that already exist.
* sql_queries.py contains the sql queries used for creating, reading, inserting, and deleting.
* etl.py to extract transform and load data from song and log data to the tables: songs, users, artists, times, and songplays.
* drop_tables.py drops the database for clean_up when done.
* /data contains the data for both the song data and the log data.

## Processing
To ensure data integrity, we placed some constraints on the postgres tables. These tables have ON CONFLICT conditions to update things like paid level (in cases where users transition from free to paid levels) and location. We used the pandas library for data processing to load the json files into dataframes. We filter and transform the dataframes and load into the tables using the psycopg2 library.

## Screenshots of tables
Star Schema
![Image of Database Schema](https://github.com/gnublet/sparkify_1/blob/master/images/database_schema.png)
Artists
![Image of Artists Table](https://github.com/gnublet/sparkify_1/blob/master/images/artists.png)
Songplays
![Image of songplays Table](https://github.com/gnublet/sparkify_1/blob/master/images/songplays.png)
Songs
![Image of songs Table](https://github.com/gnublet/sparkify_1/blob/master/images/songs.png)
Users
![Image of users Table](https://github.com/gnublet/sparkify_1/blob/master/images/users.png)
Times
![Image of times Table](https://github.com/gnublet/sparkify_1/blob/master/images/times.png)

1. The purpose of this database is to store data in a star schema. We have the songplays fact table with several dimension tables: songs, users, artists, and times. Each dimension table has a primary key that corresponds to a foreign key in the songplays fact table.

2. Songplays change very frequently as different users play new songs, but the other information such as song and artist information are don't change. We use postgres as our data store since we're working with managable data sizes and want OLTP (since we're just logging data into tables). Any time we need to add songs, artists, or users, we just need to do an insert with very little data duplication.

3. Example Queries: To find all free levels in San Franciso-Oakland-Howard, CA, I used the query.

```sql
SELECT * FROM songplays 
WHERE 
location LIKE '%San Francisco-Oakland-Hayward, CA%'
AND level!='paid'
```

To get a feel of what proportion use what browser, I looked at user-agents counts within this population.
```sql
SELECT user_agent, COUNT(*) FROM songplays 
WHERE 
location LIKE '%San Francisco-Oakland-Hayward, CA%'
AND level!='paid'
GROUP BY user_agent
```

where we see that 41 use windows and 2 use Mac.

I also wanted to see if there is a difference between free and paid usage among these user agents in the Bay area.

```sql
SELECT user_agent, COUNT(*) FROM songplays 
WHERE 
location LIKE '%San Francisco-Oakland-Hayward, CA%'
AND level='paid'
GROUP BY user_agent
```
Strangely, there are 650 songplays from Windows and 0 from Macs.