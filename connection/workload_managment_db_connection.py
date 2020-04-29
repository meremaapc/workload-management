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