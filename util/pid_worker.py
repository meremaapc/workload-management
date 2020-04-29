import domain.query_constant
from util.workload_service import calculate_process_workload,  get_metrics


def select_resource_intensive_process(processes, host_connection, wm_db_connection):
    max_process_workload = 0
    max_process_workload_process = processes[0]
    metrics = get_metrics(wm_db_connection)
    for process in processes:
        res = calculate_process_workload(process, metrics, host_connection)
        if res > max_process_workload:
            max_process_workload = res
            max_process_workload_process = process
    return max_process_workload_process.pid


KILL_PG_PROCESS = "SELECT pg_cancel_backend(%s)"


def kill_process_by_pid(pid, conn):
    try:
        cursor = conn.cursor()
        cursor.execute(domain.query_constant.PG_CANCEL_BACKEND % pid)
        print("Killed pid", pid, sep=" ")
    except Exception as error:
        print(error)
    finally:
        if conn and cursor:
            cursor.close()
