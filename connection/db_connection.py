import psycopg2
import config
from domain.pg_stat_activity import Stat_Activity
import domain.query_constant


def connect():
    print('DB connecting...')
    conn = psycopg2.connect(dbname=config.DB_CONFIG['dbname'],
                            user=config.DB_CONFIG['user'],
                            host=config.DB_CONFIG['host'],
                            port=config.DB_CONFIG['port'],
                            password=config.DB_CONFIG['password']
                            )
    print('DB connecting successfully')
    return conn


def get_data_from_pg_stat_activity(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(domain.query_constant.SELECT_PG_STAT_ACTIVITY)
        rows = cursor.fetchall()
        objects_list = []
        for row in rows:
            result = Stat_Activity(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                   row[10], row[11],
                                   row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19])
            objects_list.append(result)
        return objects_list
    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        if conn:
            cursor.close()


def create_database():
    try:
        conn = connect()
        cursor = conn.cursor()
        with open('sql/workload_management_create_database.sql') as script:
            cursor.execute(script.read())
        cursor.execute(domain.query_constant.CREATE_DATABASE, (config.DB_CONFIG['user'], config.DB_CONFIG['password']))
        conn.commit()
        conn.close()
    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
