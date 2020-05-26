import time

from web.web import config
from web.wm.workload_management.connection.workload_managment_db import get_data_from_pg_stat_activity
from web.wm.workload_management.connections import host_connect, database_connect
from web.wm.workload_management.util.monitoring_service import collect_statistic


def workload_management_run():
    host_connection = host_connect()
    wm_database_connection = database_connect()
    while True:
        processes = get_data_from_pg_stat_activity(wm_database_connection)
        collect_statistic(wm_database_connection, host_connection, processes)
        time.sleep(config.MONITORING_PAUSE)


workload_management_run()
