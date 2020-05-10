import time
import config
from connections import db_connection
from connections import module_run
from util import logger, workload_service, pid_worker


def workload_management_run():
    host_connection, wm_database_connection = module_run()
    while True:
        processes = db_connection.get_data_from_pg_stat_activity(wm_database_connection)
        critical_loading = workload_service.collect_cluster_workload(processes, wm_database_connection, host_connection)
        if not critical_loading:
            time.sleep(config.REQUEST_PAUSE_SEC)
        else:
            pid_for_kill = pid_worker.select_resource_intensive_process(processes, host_connection,
                                                                        wm_database_connection)
            pid_worker.kill_process_by_pid(pid_for_kill, wm_database_connection)
            logger.log_message("Pid %s was killed" % pid_for_kill)
            time.sleep(config.RECALCULATE_SYSTEM_LOAD_PAUSE_SEC)


workload_management_run()
