import time

import config
from conection import db_connection, remote_server_connection
from util import logger, system_load_statistic, pid_worker, metrics_collector

CLIENT_BACKEND = 'client backend'


def workload_management_run():
    database_connection = db_connection.connect()
    host_connection = remote_server_connection.connect()
    try:
        analyze(database_connection, host_connection)
    except Exception as error:
        print(error)
    finally:
        database_connection.close()
        host_connection.close()


def analyze(database_connection, host_connection):
    while True:
        processes = db_connection.get_data_from_pg_stat_activity(database_connection)
        # check to kill process
        critical_loading = system_load_statistic.collect_load_statistic(processes)
        if not critical_loading:
            time.sleep(config.REQUEST_PAUSE_SEC)
        else:
            # todo get from database
            pid_for_kill = pid_worker.select_resource_intensive_process(
                filter(lambda process: process.backend_type == CLIENT_BACKEND, processes))
            pid_worker.kill_process_by_pid(pid_for_kill)
            logger.log_message("Pid %s was killed" % pid_for_kill)
            time.sleep(config.RECALCULATE_SYSTEM_LOAD_PAUSE_SEC)


workload_management_run()
