from datetime import datetime

import psycopg2

from web.web import config
from web.wm import query_constant
from web.wm.models import Stat_Activity, Metric


def execute_init_sql(conn):
    try:
        cursor = conn.cursor()
        with open('sql/workload_management_create_table.sql') as script:
            cursor.execute(script.read())
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if conn:
            cursor.close()


def store_cluster_statistic(conn, cpu, ram):
    try:
        cursor = conn.cursor()
        cursor.execute(query_constant.INSERT_STATISTIC, (cpu, ram))
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if conn:
            cursor.close()


def get_data_from_pg_stat_activity(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(query_constant.SELECT_PG_STAT_ACTIVITY)
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


def get_metrics(wm_db_connection):
    metrics = []
    try:
        cursor = wm_db_connection.cursor()
        cursor.execute(query_constant.SELECT_METRICS)
        for value in cursor.fetchall():
            metric = Metric(value[0], value[1], value[2], value[3])
            metrics.append(metric)
    except Exception as error:
        print(error)
    finally:
        if wm_db_connection:
            cursor.close()
    return metrics


def store_current_workload(conn, value):
    try:
        cursor = conn.cursor()
        cursor.execute(query_constant.INSERT_WORKLOAD, (value,))
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if conn:
            cursor.close()


def create_wm_database(conn):
    try:
        cursor = conn.cursor()
        with open('sql/workload_management_create_database.sql') as script:
            cursor.execute(script.read())
        cursor.execute(query_constant.CREATE_DATABASE,
                       (config.MAIN_DB_CONFIG['user'], config.MAIN_DB_CONFIG['password']))
        conn.commit()
        conn.close()
    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
