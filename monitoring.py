import time

import config
from connection.workload_managment_db import get_data_from_pg_stat_activity
from connections import host_connect, database_connect
from util.monitoring_service import collect_statistic


def workload_management_run():
    host_connection = host_connect()
    wm_database_connection = database_connect()
    while True:
        processes = get_data_from_pg_stat_activity(wm_database_connection)
        collect_statistic(wm_database_connection, host_connection, processes)
        time.sleep(config.MONITORING_PAUSE)


workload_management_run()
