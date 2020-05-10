import time

import config
from connections import db_connection
from connections import module_run
from util import workload_service


def workload_management_run():
    host_connection, wm_database_connection = module_run()
    while True:
        processes = db_connection.get_data_from_pg_stat_activity(wm_database_connection)
        critical_loading = workload_service.collect_cluster_workload(processes, wm_database_connection, host_connection)
        time.sleep(config.MONITORING_PAUSE)


workload_management_run()
