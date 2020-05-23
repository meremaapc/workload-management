import domain.query_constant
from config import CLIENT_BACKEND, HINT, CPU_PARAM, RAM_PARAM, PID_PARAM
from util.workload_service import calculate_process_workload, get_metrics, get_info_about_all_pg_processes


def select_resource_intensive_process(processes, host_connection, wm_db_connection):
    processes = list(
        filter(lambda item: str(item.backend_type) == CLIENT_BACKEND and HINT not in str(item.query), processes))
    metrics = get_metrics(wm_db_connection)
    processes_info = get_info_about_all_pg_processes(host_connection, processes,
                                                     list(map(lambda metric: metric.name, metrics)))
    result = max(zip(
        map(lambda process: calculate_process_workload(
                {CPU_PARAM: float(process[CPU_PARAM]), RAM_PARAM: float(process[RAM_PARAM])}, metrics), processes_info),
        map(lambda process: process[PID_PARAM], processes_info))
    )
    return result[1]


def kill_process_by_pid(pid, conn):
    try:
        cursor = conn.cursor()
        cursor.execute(domain.query_constant.PG_CANCEL_BACKEND % pid)
        print("Killed pid", pid, sep=" ")
        cursor.close()
    except Exception as error:
        print(error)
    finally:
        if conn and cursor:
            cursor.close()
