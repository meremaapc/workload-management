import time

import config
from connection import db_connection, remote_server_connection, workload_managment_db_connection
from util import logger, workload_service, pid_worker

CLIENT_BACKEND = 'client backend'


def workload_management_run():
    database_connection = db_connection.connect()
    host_connection = remote_server_connection.connect()
    wm_database_connection = workload_managment_db_connection.connect()
    workload_managment_db_connection.execute_init_sql(wm_database_connection)
    try:
        analyze(database_connection, host_connection, wm_database_connection)
    except Exception as error:
        print(error)
    finally:
        database_connection.close()
        host_connection.close()


def analyze(database_connection, host_connection, wm_database_connection):
    while True:
        processes = db_connection.get_data_from_pg_stat_activity(database_connection)
        critical_loading = workload_service.collect_cluster_workload(processes, wm_database_connection, host_connection)
        if not critical_loading:
            time.sleep(config.REQUEST_PAUSE_SEC)
        else:
            pid_for_kill = pid_worker.select_resource_intensive_process(processes, host_connection, wm_database_connection)
            pid_worker.kill_process_by_pid(pid_for_kill, database_connection)
            logger.log_message("Pid %s was killed" % pid_for_kill)
            time.sleep(config.RECALCULATE_SYSTEM_LOAD_PAUSE_SEC)


workload_management_run()
