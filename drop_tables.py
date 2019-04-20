import psycopg2


def drop_dbs(cur, db_list):
    for db_name in db_list:
        drop_db_query = f"DROP DATABASE IF EXISTS {db_name}"
        cur.execute(drop_db_query)

def drop_tables(cur, table_list):
    for table_name in table_list:
        drop_db_query = f"DROP TABLE IF EXISTS {table_name}"
        cur.execute(drop_db_query)

def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    dbs_to_drop = [
        'sparkifydb'
    ]
    tables_to_drop = [
        ''
    ]

    # drop given dbs
    drop_dbs(cur, dbs_to_drop)

    drop_tables(cur, tables_to_drop)

    conn.close()

if __name__ == '__main__':
    main()