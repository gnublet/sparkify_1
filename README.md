# Sparkify

## Usage: 
* Run create tables.py, then etl.py. To test, you may use test.ipynb or your own database management tool (for example, adminer). To clean up, use drop_tables.py

## Files:
* create_tables.py to initialize postgres tables, replacing any that already exist.
* etl.py to extract transform and load data from song and log data to the tables: songs, users, artists, times, and songplays.
* drop_tables.py drops the database for clean_up when done.
* /data contains the data for both the song data and the log data.


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