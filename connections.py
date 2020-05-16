from config import WM_DB_CONFIG, MAIN_DB_CONFIG
from connection import db_connection, remote_server_connection, workload_managment_db
from connection.workload_managment_db import create_wm_database


def host_connect():
    return remote_server_connection.connect()


def database_connect():
    connection = db_connection.connect(MAIN_DB_CONFIG)
    create_wm_database(connection)
    wm_database_connection = db_connection.connect(WM_DB_CONFIG)
    workload_managment_db.execute_init_sql(wm_database_connection)
    connection.close()
    return wm_database_connection
