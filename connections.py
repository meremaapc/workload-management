from config import WM_DB_CONFIG, MAIN_DB_CONFIG
from connection import db_connection, remote_server_connection, workload_managment_db


def host_connect():
    return remote_server_connection.connect()


def database_connect():
    connection = db_connection.connect(MAIN_DB_CONFIG)
    wm_database_connection = workload_managment_db.connect(WM_DB_CONFIG)
    workload_managment_db.execute_init_sql(wm_database_connection)
    connection.close()
    return wm_database_connection
