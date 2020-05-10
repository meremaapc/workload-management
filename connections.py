from connection import db_connection, remote_server_connection, workload_managment_db_connection

CLIENT_BACKEND = 'client backend'


def module_run():
    database_connection = db_connection.connect()
    host_connection = remote_server_connection.connect()
    wm_database_connection = workload_managment_db_connection.connect()
    workload_managment_db_connection.execute_init_sql(wm_database_connection)
    database_connection.close()
    return host_connection, wm_database_connection


module_run()
