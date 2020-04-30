import psycopg2
import config


def connect():
    print('DB connecting...')
    conn = psycopg2.connect(dbname=config.WM_DB_CONFIG['dbname'],
                            user=config.WM_DB_CONFIG['user'],
                            host=config.WM_DB_CONFIG['host'],
                            port=config.WM_DB_CONFIG['port'],
                            password=config.WM_DB_CONFIG['password']
                            )
    print('DB connecting successfully')
    return conn


def execute_init_sql(conn):
    try:
        cursor = conn.cursor()
        with open('sql/workload_management_create_table.sql') as script:
            cursor.execute(script.read())
    except Exception as error:
        print(error)
    finally:
        if conn:
            cursor.close()
